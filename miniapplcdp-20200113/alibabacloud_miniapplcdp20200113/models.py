# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataItemsModelDataValue(TeaModel):
    def __init__(self, id=None, model_id=None, model_name=None, model_status=None, model_type=None, sub_type=None,
                 module_id=None, content=None, app_id=None, linked=None, link_module_id=None, link_model_id=None,
                 schema_version=None, description=None, props=None, visibility=None, model_digest=None):
        self.id = id  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.sub_type = sub_type  # type: str
        self.module_id = module_id  # type: str
        self.content = content  # type: str
        self.app_id = app_id  # type: str
        self.linked = linked  # type: bool
        self.link_module_id = link_module_id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.schema_version = schema_version  # type: str
        self.description = description  # type: str
        self.props = props  # type: str
        self.visibility = visibility  # type: str
        self.model_digest = model_digest  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataItemsModelDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.content is not None:
            result['Content'] = self.content
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.description is not None:
            result['Description'] = self.description
        if self.props is not None:
            result['Props'] = self.props
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        return self


class DataItemsResourceDataValue(TeaModel):
    def __init__(self, resource_id=None, resource_name=None, resource_type=None, description=None,
                 schema_version=None, module_id=None, content=None, app_id=None, visibility=None):
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.description = description  # type: str
        self.schema_version = schema_version  # type: str
        self.module_id = module_id  # type: str
        self.content = content  # type: dict[str, any]
        self.app_id = app_id  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataItemsResourceDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.description is not None:
            result['Description'] = self.description
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.content is not None:
            result['Content'] = self.content
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchCreateModelRequest(TeaModel):
    def __init__(self, app_id=None, model_data_json=None, module_id=None, schema_version=None, source=None,
                 sub_type=None):
        self.app_id = app_id  # type: str
        self.model_data_json = model_data_json  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCreateModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_data_json is not None:
            result['ModelDataJson'] = self.model_data_json
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelDataJson') is not None:
            self.model_data_json = m.get('ModelDataJson')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class BatchCreateModelResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCreateModelResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchCreateModelResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[BatchCreateModelResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchCreateModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchCreateModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchCreateModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: BatchCreateModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchCreateModelResponseBody, self).to_map()
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
            temp_model = BatchCreateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchCreateModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchCreateModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchCreateModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteModelRequest(TeaModel):
    def __init__(self, app_id=None, model_id_list=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.model_id_list = model_id_list  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id_list is not None:
            result['ModelIdList'] = self.model_id_list
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelIdList') is not None:
            self.model_id_list = m.get('ModelIdList')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchDeleteModelResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteModelResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchDeleteModelResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[BatchDeleteModelResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchDeleteModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchDeleteModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchDeleteModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: BatchDeleteModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchDeleteModelResponseBody, self).to_map()
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
            temp_model = BatchDeleteModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteResourcesRequest(TeaModel):
    def __init__(self, app_id=None, module_id=None, resource_id_list=None, source=None):
        self.app_id = app_id  # type: str
        self.module_id = module_id  # type: str
        self.resource_id_list = resource_id_list  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id_list is not None:
            result['ResourceIdList'] = self.resource_id_list
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceIdList') is not None:
            self.resource_id_list = m.get('ResourceIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchDeleteResourcesResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_id=None, resource_name=None, resource_type=None, revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteResourcesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class BatchDeleteResourcesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[BatchDeleteResourcesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchDeleteResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchDeleteResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchDeleteResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: BatchDeleteResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchDeleteResourcesResponseBody, self).to_map()
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
            temp_model = BatchDeleteResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRestoreModelRequest(TeaModel):
    def __init__(self, app_id=None, model_id_list=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.model_id_list = model_id_list  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchRestoreModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id_list is not None:
            result['ModelIdList'] = self.model_id_list
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelIdList') is not None:
            self.model_id_list = m.get('ModelIdList')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchRestoreModelResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchRestoreModelResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchRestoreModelResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[BatchRestoreModelResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchRestoreModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchRestoreModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchRestoreModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: BatchRestoreModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchRestoreModelResponseBody, self).to_map()
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
            temp_model = BatchRestoreModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchRestoreModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchRestoreModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchRestoreModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchRestoreModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(self, app_id=None, domain=None, domain_type=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CheckDomainResponseBodyData(TeaModel):
    def __init__(self, valid=None):
        self.valid = valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CheckDomainResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckDomainResponseBody, self).to_map()
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
            temp_model = CheckDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, icon=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CloneAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CloneAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CloneAppResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloneAppResponseBody, self).to_map()
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
            temp_model = CloneAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModelFromCommitRequest(TeaModel):
    def __init__(self, model_id=None, source=None, source_commit_id=None, source_module_id=None, sub_type=None,
                 target_module_id=None, target_name=None, target_sub_type=None):
        self.model_id = model_id  # type: str
        self.source = source  # type: str
        self.source_commit_id = source_commit_id  # type: str
        self.source_module_id = source_module_id  # type: str
        self.sub_type = sub_type  # type: str
        self.target_module_id = target_module_id  # type: str
        self.target_name = target_name  # type: str
        self.target_sub_type = target_sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModelFromCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_commit_id is not None:
            result['SourceCommitId'] = self.source_commit_id
        if self.source_module_id is not None:
            result['SourceModuleId'] = self.source_module_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.target_module_id is not None:
            result['TargetModuleId'] = self.target_module_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_sub_type is not None:
            result['TargetSubType'] = self.target_sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceCommitId') is not None:
            self.source_commit_id = m.get('SourceCommitId')
        if m.get('SourceModuleId') is not None:
            self.source_module_id = m.get('SourceModuleId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('TargetModuleId') is not None:
            self.target_module_id = m.get('TargetModuleId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetSubType') is not None:
            self.target_sub_type = m.get('TargetSubType')
        return self


class CloneModelFromCommitResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModelFromCommitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CloneModelFromCommitResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CloneModelFromCommitResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloneModelFromCommitResponseBody, self).to_map()
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
            temp_model = CloneModelFromCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneModelFromCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneModelFromCommitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneModelFromCommitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModelFromCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModelInModuleRequest(TeaModel):
    def __init__(self, model_id=None, module_id=None, source=None, target_name=None, target_sub_type=None):
        self.model_id = model_id  # type: str
        self.module_id = module_id  # type: str
        self.source = source  # type: str
        self.target_name = target_name  # type: str
        self.target_sub_type = target_sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModelInModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_sub_type is not None:
            result['TargetSubType'] = self.target_sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetSubType') is not None:
            self.target_sub_type = m.get('TargetSubType')
        return self


class CloneModelInModuleResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModelInModuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CloneModelInModuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CloneModelInModuleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloneModelInModuleResponseBody, self).to_map()
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
            temp_model = CloneModelInModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneModelInModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneModelInModuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneModelInModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModelInModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None, app_type=None, asynchronous=None, category_id=None, client_token=None,
                 description=None, icon=None, platform_version=None, schema_version=None, source=None, source_commit_id=None,
                 template_id=None, templated=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.asynchronous = asynchronous  # type: bool
        self.category_id = category_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.platform_version = platform_version  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.source_commit_id = source_commit_id  # type: str
        self.template_id = template_id  # type: str
        self.templated = templated  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.asynchronous is not None:
            result['Asynchronous'] = self.asynchronous
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.source_commit_id is not None:
            result['SourceCommitId'] = self.source_commit_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.templated is not None:
            result['Templated'] = self.templated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Asynchronous') is not None:
            self.asynchronous = m.get('Asynchronous')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceCommitId') is not None:
            self.source_commit_id = m.get('SourceCommitId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Templated') is not None:
            self.templated = m.get('Templated')
        return self


class CreateAppResponseBodyDataCategories(TeaModel):
    def __init__(self, category_id=None, category_name=None, parent_category_id=None):
        self.category_id = category_id  # type: str
        self.category_name = category_name  # type: str
        self.parent_category_id = parent_category_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBodyDataCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, categories=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 platform_version=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.categories = categories  # type: list[CreateAppResponseBodyDataCategories]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.platform_version = platform_version  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = CreateAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateAppResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
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
            temp_model = CreateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommitRequest(TeaModel):
    def __init__(self, app_id=None, client_token=None, commit_log=None, commit_type=None,
                 main_module_commit_id=None, module_id=None, rollback_to_commit_id=None, rollback_type=None, schema_version=None,
                 source=None):
        self.app_id = app_id  # type: str
        self.client_token = client_token  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.module_id = module_id  # type: str
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateCommitResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_id=None, commit_log=None, commit_type=None, create_time=None,
                 main_module_commit_id=None, main_module_id=None, model_data_path=None, modified_time=None, module_id=None,
                 resource_data_path=None, resource_digest=None, rollback_to_commit_id=None, rollback_type=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.create_time = create_time  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.main_module_id = main_module_id  # type: str
        self.model_data_path = model_data_path  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_data_path = resource_data_path  # type: str
        self.resource_digest = resource_digest  # type: dict[str, str]
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCommitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class CreateCommitResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateCommitResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateCommitResponseBody, self).to_map()
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
            temp_model = CreateCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCommitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCommitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, app_id=None, client_token=None, domain=None, domain_type=None, env_id=None, path=None,
                 private_key=None, public_key=None, source=None, with_certificate=None):
        self.app_id = app_id  # type: str
        self.client_token = client_token  # type: str
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.path = path  # type: str
        self.private_key = private_key  # type: str
        self.public_key = public_key  # type: str
        self.source = source  # type: str
        self.with_certificate = with_certificate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.source is not None:
            result['Source'] = self.source
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class CreateDomainResponseBodyData(TeaModel):
    def __init__(self, app_id=None, applied=None, checked=None, cname=None, deleted=None, domain=None,
                 domain_type=None, env_id=None, path=None, with_certificate=None):
        self.app_id = app_id  # type: str
        self.applied = applied  # type: bool
        self.checked = checked  # type: bool
        self.cname = cname  # type: str
        self.deleted = deleted  # type: bool
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.path = path  # type: str
        self.with_certificate = with_certificate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.checked is not None:
            result['Checked'] = self.checked
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Checked') is not None:
            self.checked = m.get('Checked')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateDomainResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDomainResponseBody, self).to_map()
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
            temp_model = CreateDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLinkEntityAndAssociationRequest(TeaModel):
    def __init__(self, client_token=None, model_data=None, source=None):
        self.client_token = client_token  # type: str
        self.model_data = model_data  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLinkEntityAndAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.model_data is not None:
            result['ModelData'] = self.model_data
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ModelData') is not None:
            self.model_data = m.get('ModelData')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateLinkEntityAndAssociationResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLinkEntityAndAssociationResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateLinkEntityAndAssociationResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[CreateLinkEntityAndAssociationResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLinkEntityAndAssociationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = CreateLinkEntityAndAssociationResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class CreateLinkEntityAndAssociationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateLinkEntityAndAssociationResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateLinkEntityAndAssociationResponseBody, self).to_map()
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
            temp_model = CreateLinkEntityAndAssociationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLinkEntityAndAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLinkEntityAndAssociationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLinkEntityAndAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLinkEntityAndAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(self, app_id=None, client_token=None, content=None, description=None, encode_type=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_type=None,
                 module_id=None, schema_version=None, source=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.client_token = client_token  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.encode_type = encode_type  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_type = model_type  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateModelResponseBody, self).to_map()
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
            temp_model = CreateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleRequest(TeaModel):
    def __init__(self, client_token=None, description=None, icon=None, minimum_platform_version=None,
                 module_name=None, module_type=None, platform=None, source=None, source_module_id=None, target_app_source=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.platform = platform  # type: str
        self.source = source  # type: str
        self.source_module_id = source_module_id  # type: str
        self.target_app_source = target_app_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        if self.source_module_id is not None:
            result['SourceModuleId'] = self.source_module_id
        if self.target_app_source is not None:
            result['TargetAppSource'] = self.target_app_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceModuleId') is not None:
            self.source_module_id = m.get('SourceModuleId')
        if m.get('TargetAppSource') is not None:
            self.target_app_source = m.get('TargetAppSource')
        return self


class CreateModuleResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 module_type=None, owner_app_id=None, owner_user_id=None, platform=None, platform_version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.platform_version = platform_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class CreateModuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateModuleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateModuleResponseBody, self).to_map()
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
            temp_model = CreateModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModulePublishRequest(TeaModel):
    def __init__(self, client_token=None, description=None, module_id=None, publish_version=None, source=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.publish_version = publish_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModulePublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateModulePublishResponseBodyData(TeaModel):
    def __init__(self, commit_id=None, create_time=None, description=None, modified_time=None, module_id=None,
                 publish_id=None, version=None):
        self.commit_id = commit_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.publish_id = publish_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModulePublishResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateModulePublishResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateModulePublishResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateModulePublishResponseBody, self).to_map()
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
            temp_model = CreateModulePublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModulePublishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModulePublishResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModulePublishResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModulePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishRequest(TeaModel):
    def __init__(self, app_id=None, client_token=None, commit_id=None, description=None, env_type=None,
                 publish_type=None, source=None, version_number=None):
        self.app_id = app_id  # type: str
        self.client_token = client_token  # type: str
        self.commit_id = commit_id  # type: str
        self.description = description  # type: str
        self.env_type = env_type  # type: str
        self.publish_type = publish_type  # type: str
        self.source = source  # type: str
        self.version_number = version_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.source is not None:
            result['Source'] = self.source
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class CreatePublishResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_id=None, completion_time=None, create_time=None, description=None,
                 env_id=None, modified_time=None, publish_id=None, publish_status=None, publish_type=None, reason=None,
                 start_time=None, sub_tasks=None, version_number=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.completion_time = completion_time  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.env_id = env_id  # type: str
        self.modified_time = modified_time  # type: str
        self.publish_id = publish_id  # type: str
        self.publish_status = publish_status  # type: str
        self.publish_type = publish_type  # type: str
        self.reason = reason  # type: str
        self.start_time = start_time  # type: str
        self.sub_tasks = sub_tasks  # type: list[dict[str, str]]
        self.version_number = version_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePublishResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class CreatePublishResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreatePublishResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePublishResponseBody, self).to_map()
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
            temp_model = CreatePublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePublishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePublishResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePublishResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(self, app_id=None, client_token=None, content=None, description=None, module_id=None,
                 resource_id=None, resource_name=None, resource_type=None, schema_version=None, source=None, visibility=None):
        self.app_id = app_id  # type: str
        self.client_token = client_token  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateResourceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_digest=None, resource_id=None, resource_name=None, resource_type=None,
                 revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_digest = resource_digest  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateResourceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateResourceResponseBody, self).to_map()
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
            temp_model = CreateResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(self, app_id=None, source=None):
        self.app_id = app_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteAppResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
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
            temp_model = DeleteAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommitRequest(TeaModel):
    def __init__(self, app_id=None, commit_id=None, module_id=None, source=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.module_id = module_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteCommitResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_id=None, commit_log=None, commit_type=None, create_time=None,
                 main_module_commit_id=None, main_module_id=None, model_data_path=None, modified_time=None, module_id=None,
                 resource_data_path=None, resource_digest=None, rollback_to_commit_id=None, rollback_type=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.create_time = create_time  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.main_module_id = main_module_id  # type: str
        self.model_data_path = model_data_path  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_data_path = resource_data_path  # type: str
        self.resource_digest = resource_digest  # type: dict[str, str]
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class DeleteCommitResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteCommitResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteCommitResponseBody, self).to_map()
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
            temp_model = DeleteCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCommitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCommitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, app_id=None, domain=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.domain = domain  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteDomainResponseBodyData(TeaModel):
    def __init__(self, app_id=None, applied=None, deleted=None, domain=None, domain_type=None, env_id=None, path=None):
        self.app_id = app_id  # type: str
        self.applied = applied  # type: bool
        self.deleted = deleted  # type: bool
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteDomainResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteDomainResponseBody, self).to_map()
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
            temp_model = DeleteDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelRequest(TeaModel):
    def __init__(self, app_id=None, model_id=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.model_id = model_id  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteModelResponseBody, self).to_map()
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
            temp_model = DeleteModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModuleRequest(TeaModel):
    def __init__(self, module_id=None, source=None):
        self.module_id = module_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteModuleResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 owner_app_id=None, owner_user_id=None, platform=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DeleteModuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteModuleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteModuleResponseBody, self).to_map()
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
            temp_model = DeleteModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteModuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(self, app_id=None, module_id=None, resource_id=None, source=None):
        self.app_id = app_id  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteResourceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_id=None, resource_name=None, resource_type=None, revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteResourceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteResourceResponseBody, self).to_map()
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
            temp_model = DeleteResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAppUserPasswordRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None, user_name=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAppUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GenerateAppUserPasswordResponseBodyData(TeaModel):
    def __init__(self, password=None, user_name=None):
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAppUserPasswordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GenerateAppUserPasswordResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateAppUserPasswordResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateAppUserPasswordResponseBody, self).to_map()
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
            temp_model = GenerateAppUserPasswordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAppUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateAppUserPasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateAppUserPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAppUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAuthTokenRequest(TeaModel):
    def __init__(self, app_id=None, module_id=None, source=None):
        self.app_id = app_id  # type: str
        self.module_id = module_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAuthTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GenerateAuthTokenResponseBodyData(TeaModel):
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAuthTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GenerateAuthTokenResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateAuthTokenResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateAuthTokenResponseBody, self).to_map()
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
            temp_model = GenerateAuthTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAuthTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateAuthTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateAuthTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadTokenRequest(TeaModel):
    def __init__(self, app_id=None, material_id=None, module_id=None, source=None, upload_token_type=None):
        self.app_id = app_id  # type: str
        self.material_id = material_id  # type: str
        self.module_id = module_id  # type: str
        self.source = source  # type: str
        self.upload_token_type = upload_token_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        if self.upload_token_type is not None:
            result['UploadTokenType'] = self.upload_token_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UploadTokenType') is not None:
            self.upload_token_type = m.get('UploadTokenType')
        return self


class GenerateUploadTokenResponseBodyData(TeaModel):
    def __init__(self, key=None, oss_access_key_id=None, policy=None, server_url=None, signature=None,
                 x_amz_algorithm=None, x_amz_credential=None, x_amz_date=None, x_amz_signature=None):
        self.key = key  # type: str
        self.oss_access_key_id = oss_access_key_id  # type: str
        self.policy = policy  # type: str
        self.server_url = server_url  # type: str
        self.signature = signature  # type: str
        self.x_amz_algorithm = x_amz_algorithm  # type: str
        self.x_amz_credential = x_amz_credential  # type: str
        self.x_amz_date = x_amz_date  # type: str
        self.x_amz_signature = x_amz_signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.server_url is not None:
            result['ServerURL'] = self.server_url
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.x_amz_algorithm is not None:
            result['X-Amz-Algorithm'] = self.x_amz_algorithm
        if self.x_amz_credential is not None:
            result['X-Amz-Credential'] = self.x_amz_credential
        if self.x_amz_date is not None:
            result['X-Amz-Date'] = self.x_amz_date
        if self.x_amz_signature is not None:
            result['X-Amz-Signature'] = self.x_amz_signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServerURL') is not None:
            self.server_url = m.get('ServerURL')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('X-Amz-Algorithm') is not None:
            self.x_amz_algorithm = m.get('X-Amz-Algorithm')
        if m.get('X-Amz-Credential') is not None:
            self.x_amz_credential = m.get('X-Amz-Credential')
        if m.get('X-Amz-Date') is not None:
            self.x_amz_date = m.get('X-Amz-Date')
        if m.get('X-Amz-Signature') is not None:
            self.x_amz_signature = m.get('X-Amz-Signature')
        return self


class GenerateUploadTokenResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateUploadTokenResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateUploadTokenResponseBody, self).to_map()
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
            temp_model = GenerateUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateUploadTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateUploadTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(self, app_id=None, source=None):
        self.app_id = app_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppResponseBodyDataCategories(TeaModel):
    def __init__(self, category_id=None, category_name=None, parent_category_id=None):
        self.category_id = category_id  # type: str
        self.category_name = category_name  # type: str
        self.parent_category_id = parent_category_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyDataCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class GetAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, categories=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 platform_version=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.categories = categories  # type: list[GetAppResponseBodyDataCategories]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.platform_version = platform_version  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = GetAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetAppResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAppResponseBody, self).to_map()
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
            temp_model = GetAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppModelRequest(TeaModel):
    def __init__(self, app_id=None, schema_version=None, source=None, sub_type=None):
        self.app_id = app_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class GetAppModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class GetAppModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetAppModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAppModelResponseBody, self).to_map()
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
            temp_model = GetAppModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(self, app_id=None, source=None):
        self.app_id = app_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppSecretResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_secret=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSecretResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        return self


class GetAppSecretResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetAppSecretResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAppSecretResponseBody, self).to_map()
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
            temp_model = GetAppSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppSecretResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRequest(TeaModel):
    def __init__(self, app_id=None, artifact_id=None, source=None):
        self.app_id = app_id  # type: str
        self.artifact_id = artifact_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetArtifactResponseBodyData(TeaModel):
    def __init__(self, app_id=None, artifact_id=None, artifact_type=None, available=None, create_time=None,
                 modified_time=None, url=None):
        self.app_id = app_id  # type: str
        self.artifact_id = artifact_id  # type: str
        self.artifact_type = artifact_type  # type: str
        self.available = available  # type: bool
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.available is not None:
            result['Available'] = self.available
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetArtifactResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetArtifactResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetArtifactResponseBody, self).to_map()
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
            temp_model = GetArtifactResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetArtifactResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommitRequest(TeaModel):
    def __init__(self, app_id=None, commit_id=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetCommitResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_digest=None, commit_id=None, commit_log=None, commit_type=None,
                 create_time=None, main_module_commit_id=None, main_module_id=None, model_data_path=None, model_digest=None,
                 model_pack=None, modified_time=None, module_id=None, resource_data_path=None, resource_digest=None,
                 resource_pack=None, rollback_to_commit_id=None, rollback_type=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.commit_digest = commit_digest  # type: str
        self.commit_id = commit_id  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.create_time = create_time  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.main_module_id = main_module_id  # type: str
        self.model_data_path = model_data_path  # type: str
        self.model_digest = model_digest  # type: dict[str, str]
        self.model_pack = model_pack  # type: list[any]
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_data_path = resource_data_path  # type: str
        self.resource_digest = resource_digest  # type: dict[str, str]
        self.resource_pack = resource_pack  # type: list[dict[str, str]]
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_digest is not None:
            result['CommitDigest'] = self.commit_digest
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_pack is not None:
            result['ModelPack'] = self.model_pack
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_pack is not None:
            result['ResourcePack'] = self.resource_pack
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitDigest') is not None:
            self.commit_digest = m.get('CommitDigest')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelPack') is not None:
            self.model_pack = m.get('ModelPack')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourcePack') is not None:
            self.resource_pack = m.get('ResourcePack')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetCommitResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetCommitResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCommitResponseBody, self).to_map()
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
            temp_model = GetCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCommitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCommitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultAppUserRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultAppUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDefaultAppUserResponseBodyData(TeaModel):
    def __init__(self, has_password=None, user_name=None):
        self.has_password = has_password  # type: bool
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultAppUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetDefaultAppUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetDefaultAppUserResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDefaultAppUserResponseBody, self).to_map()
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
            temp_model = GetDefaultAppUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultAppUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDefaultAppUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultAppUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDefaultAppUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainCnameRequest(TeaModel):
    def __init__(self, app_id=None, domain=None, domain_type=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainCnameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDomainCnameResponseBodyData(TeaModel):
    def __init__(self, cname=None):
        self.cname = cname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainCnameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        return self


class GetDomainCnameResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetDomainCnameResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDomainCnameResponseBody, self).to_map()
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
            temp_model = GetDomainCnameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainCnameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainCnameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainCnameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainOverviewRequest(TeaModel):
    def __init__(self, app_id=None, domain=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.domain = domain  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDomainOverviewResponseBodyData(TeaModel):
    def __init__(self, app_id=None, applied=None, certificate=None, cname=None, deleted=None, domain=None,
                 domain_type=None, env_id=None, path=None, with_certificate=None):
        self.app_id = app_id  # type: str
        self.applied = applied  # type: bool
        self.certificate = certificate  # type: dict[str, str]
        self.cname = cname  # type: str
        self.deleted = deleted  # type: bool
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.path = path  # type: str
        self.with_certificate = with_certificate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainOverviewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class GetDomainOverviewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetDomainOverviewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDomainOverviewResponseBody, self).to_map()
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
            temp_model = GetDomainOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainOverviewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(self, account_ops_endpoint=None, app_id=None, create_time=None, current_publish_id=None,
                 endpoint=None, env_id=None, env_type=None, modified_time=None, publishing_id=None):
        self.account_ops_endpoint = account_ops_endpoint  # type: str
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: str
        self.current_publish_id = current_publish_id  # type: str
        self.endpoint = endpoint  # type: str
        self.env_id = env_id  # type: str
        self.env_type = env_type  # type: str
        self.modified_time = modified_time  # type: str
        self.publishing_id = publishing_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ops_endpoint is not None:
            result['AccountOpsEndpoint'] = self.account_ops_endpoint
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish_id is not None:
            result['CurrentPublishId'] = self.current_publish_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publishing_id is not None:
            result['PublishingId'] = self.publishing_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountOpsEndpoint') is not None:
            self.account_ops_endpoint = m.get('AccountOpsEndpoint')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublishId') is not None:
            self.current_publish_id = m.get('CurrentPublishId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishingId') is not None:
            self.publishing_id = m.get('PublishingId')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetEnvironmentResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponseBody, self).to_map()
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
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEnvironmentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryStatsRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, source=None, start_date=None):
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: str
        self.source = source  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistoryStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.source is not None:
            result['Source'] = self.source
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetHistoryStatsResponseBodyData(TeaModel):
    def __init__(self, history_pv=None, history_uv=None):
        self.history_pv = history_pv  # type: dict[str, str]
        self.history_uv = history_uv  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistoryStatsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_pv is not None:
            result['HistoryPv'] = self.history_pv
        if self.history_uv is not None:
            result['HistoryUv'] = self.history_uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HistoryPv') is not None:
            self.history_pv = m.get('HistoryPv')
        if m.get('HistoryUv') is not None:
            self.history_uv = m.get('HistoryUv')
        return self


class GetHistoryStatsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetHistoryStatsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHistoryStatsResponseBody, self).to_map()
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
            temp_model = GetHistoryStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistoryStatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHistoryStatsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHistoryStatsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHistoryStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestCommitRequest(TeaModel):
    def __init__(self, app_id=None, module_id=None, source=None):
        self.app_id = app_id  # type: str
        self.module_id = module_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLatestCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetLatestCommitResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_id=None, commit_log=None, commit_type=None, create_time=None,
                 main_module_commit_id=None, main_module_id=None, model_data_path=None, modified_time=None, module_id=None,
                 resource_data_path=None, resource_digest=None, rollback_to_commit_id=None, rollback_type=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.create_time = create_time  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.main_module_id = main_module_id  # type: str
        self.model_data_path = model_data_path  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_data_path = resource_data_path  # type: str
        self.resource_digest = resource_digest  # type: dict[str, str]
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLatestCommitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetLatestCommitResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetLatestCommitResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetLatestCommitResponseBody, self).to_map()
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
            temp_model = GetLatestCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLatestCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLatestCommitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLatestCommitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLatestCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelRequest(TeaModel):
    def __init__(self, app_id=None, model_id=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.model_id = model_id  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class GetModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetModelResponseBody, self).to_map()
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
            temp_model = GetModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleRequest(TeaModel):
    def __init__(self, module_id=None, module_type=None, source=None):
        self.module_id = module_id  # type: str
        self.module_type = module_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetModuleResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 owner_app_id=None, owner_user_id=None, platform=None, platform_version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.platform_version = platform_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class GetModuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetModuleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetModuleResponseBody, self).to_map()
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
            temp_model = GetModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishRequest(TeaModel):
    def __init__(self, app_id=None, publish_id=None, source=None):
        self.app_id = app_id  # type: str
        self.publish_id = publish_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetPublishResponseBodyData(TeaModel):
    def __init__(self, app_id=None, commit_id=None, completion_time=None, create_time=None, description=None,
                 env_id=None, modified_time=None, publish_id=None, publish_status=None, publish_type=None, reason=None,
                 start_time=None, sub_tasks=None, version_number=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.completion_time = completion_time  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.env_id = env_id  # type: str
        self.modified_time = modified_time  # type: str
        self.publish_id = publish_id  # type: str
        self.publish_status = publish_status  # type: str
        self.publish_type = publish_type  # type: str
        self.reason = reason  # type: str
        self.start_time = start_time  # type: str
        self.sub_tasks = sub_tasks  # type: list[dict[str, str]]
        self.version_number = version_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublishResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class GetPublishResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetPublishResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPublishResponseBody, self).to_map()
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
            temp_model = GetPublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPublishResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPublishResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeStatsRequest(TeaModel):
    def __init__(self, app_id=None, source=None):
        self.app_id = app_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRealtimeStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetRealtimeStatsResponseBodyData(TeaModel):
    def __init__(self, today_pv_count=None, today_uv_count=None, total_pv_count=None, total_uv_count=None):
        self.today_pv_count = today_pv_count  # type: dict[str, str]
        self.today_uv_count = today_uv_count  # type: dict[str, str]
        self.total_pv_count = total_pv_count  # type: dict[str, str]
        self.total_uv_count = total_uv_count  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRealtimeStatsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.today_pv_count is not None:
            result['TodayPvCount'] = self.today_pv_count
        if self.today_uv_count is not None:
            result['TodayUvCount'] = self.today_uv_count
        if self.total_pv_count is not None:
            result['TotalPvCount'] = self.total_pv_count
        if self.total_uv_count is not None:
            result['TotalUvCount'] = self.total_uv_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TodayPvCount') is not None:
            self.today_pv_count = m.get('TodayPvCount')
        if m.get('TodayUvCount') is not None:
            self.today_uv_count = m.get('TodayUvCount')
        if m.get('TotalPvCount') is not None:
            self.total_pv_count = m.get('TotalPvCount')
        if m.get('TotalUvCount') is not None:
            self.total_uv_count = m.get('TotalUvCount')
        return self


class GetRealtimeStatsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetRealtimeStatsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRealtimeStatsResponseBody, self).to_map()
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
            temp_model = GetRealtimeStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRealtimeStatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRealtimeStatsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRealtimeStatsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealtimeStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(self, app_id=None, image_process_parameter=None, module_id=None, resource_id=None, source=None):
        self.app_id = app_id  # type: str
        self.image_process_parameter = image_process_parameter  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetResourceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_digest=None, resource_id=None, resource_name=None, resource_type=None,
                 revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_digest = resource_digest  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetResourceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResourceResponseBody, self).to_map()
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
            temp_model = GetResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, modified_time=None, platform_version=None,
                 user_secret=None, user_status=None, user_type=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.platform_version = platform_version  # type: str
        self.user_secret = user_secret  # type: str
        self.user_status = user_status  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.user_secret is not None:
            result['UserSecret'] = self.user_secret
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('UserSecret') is not None:
            self.user_secret = m.get('UserSecret')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetUserResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
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
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppModulesRequest(TeaModel):
    def __init__(self, app_id=None, recursive=None, source=None):
        self.app_id = app_id  # type: str
        self.recursive = recursive  # type: bool
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppModulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListAppModulesResponseBodyDataItems(TeaModel):
    def __init__(self, commit_id=None, description=None, direct_dependency=None, icon=None,
                 minimum_platform_version=None, module_id=None, module_name=None, owner_user_id=None, platform=None, version=None):
        self.commit_id = commit_id  # type: str
        self.description = description  # type: str
        self.direct_dependency = direct_dependency  # type: bool
        self.icon = icon  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppModulesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.direct_dependency is not None:
            result['DirectDependency'] = self.direct_dependency
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectDependency') is not None:
            self.direct_dependency = m.get('DirectDependency')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppModulesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListAppModulesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppModulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListAppModulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListAppModulesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAppModulesResponseBody, self).to_map()
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
            temp_model = ListAppModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppModulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppModulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppModulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppTemplatesRequest(TeaModel):
    def __init__(self, app_type=None, source=None, template_type=None):
        self.app_type = app_type  # type: str
        self.source = source  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.source is not None:
            result['Source'] = self.source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAppTemplatesResponseBodyDataItems(TeaModel):
    def __init__(self, app_name=None, app_type=None, category_name=None, create_time=None, description=None,
                 icon=None, last_edit_time=None, main_module_id=None, modified_time=None, schema_version=None,
                 source=None, template_id=None, template_type=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.category_name = category_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppTemplatesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAppTemplatesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListAppTemplatesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppTemplatesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListAppTemplatesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponseBody, self).to_map()
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
            temp_model = ListAppTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppTemplatesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, custom_parent_id=None,
                 description=None, main_module_id=None, page_number=None, page_size=None, source=None, template=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.custom_parent_id = custom_parent_id  # type: str
        self.description = description  # type: str
        self.main_module_id = main_module_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source = source  # type: str
        self.template = template  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ListAppsResponseBodyDataItemsCategories(TeaModel):
    def __init__(self, category_id=None, category_name=None, parent_category_id=None):
        self.category_id = category_id  # type: str
        self.category_name = category_name  # type: str
        self.parent_category_id = parent_category_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsResponseBodyDataItemsCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListAppsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, categories=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 platform_version=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.categories = categories  # type: list[ListAppsResponseBodyDataItemsCategories]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.platform_version = platform_version  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = ListAppsResponseBodyDataItemsCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListAppsResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListAppsResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListAppsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAppsResponseBody, self).to_map()
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
            temp_model = ListAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactsRequest(TeaModel):
    def __init__(self, app_id=None, publish_id=None, source=None):
        self.app_id = app_id  # type: str
        self.publish_id = publish_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListArtifactsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, artifact_id=None, artifact_type=None, available=None, create_time=None,
                 modified_time=None, url=None):
        self.app_id = app_id  # type: str
        self.artifact_id = artifact_id  # type: str
        self.artifact_type = artifact_type  # type: str
        self.available = available  # type: bool
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.available is not None:
            result['Available'] = self.available
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListArtifactsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListArtifactsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListArtifactsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListArtifactsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListArtifactsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListArtifactsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListArtifactsResponseBody, self).to_map()
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
            temp_model = ListArtifactsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListArtifactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListArtifactsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListArtifactsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommitsRequest(TeaModel):
    def __init__(self, app_id=None, commit_log=None, custom_parent_id=None, module_id=None, page_number=None,
                 page_size=None, source=None):
        self.app_id = app_id  # type: str
        self.commit_log = commit_log  # type: str
        self.custom_parent_id = custom_parent_id  # type: str
        self.module_id = module_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListCommitsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, commit_digest=None, commit_id=None, commit_log=None, commit_type=None,
                 create_time=None, main_module_commit_id=None, main_module_id=None, model_data_path=None, model_digest=None,
                 modified_time=None, module_id=None, resource_data_path=None, resource_digest=None, rollback_to_commit_id=None,
                 rollback_type=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.commit_digest = commit_digest  # type: str
        self.commit_id = commit_id  # type: str
        self.commit_log = commit_log  # type: str
        self.commit_type = commit_type  # type: str
        self.create_time = create_time  # type: str
        self.main_module_commit_id = main_module_commit_id  # type: str
        self.main_module_id = main_module_id  # type: str
        self.model_data_path = model_data_path  # type: str
        self.model_digest = model_digest  # type: dict[str, str]
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_data_path = resource_data_path  # type: str
        self.resource_digest = resource_digest  # type: dict[str, str]
        self.rollback_to_commit_id = rollback_to_commit_id  # type: str
        self.rollback_type = rollback_type  # type: str
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommitsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_digest is not None:
            result['CommitDigest'] = self.commit_digest
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitDigest') is not None:
            self.commit_digest = m.get('CommitDigest')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListCommitsResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListCommitsResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommitsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListCommitsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommitsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListCommitsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCommitsResponseBody, self).to_map()
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
            temp_model = ListCommitsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCommitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCommitsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCommitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDomainsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, applied=None, checked=None, cname=None, deleted=None, domain=None,
                 domain_type=None, env_id=None, path=None, with_certificate=None):
        self.app_id = app_id  # type: str
        self.applied = applied  # type: bool
        self.checked = checked  # type: bool
        self.cname = cname  # type: str
        self.deleted = deleted  # type: bool
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.path = path  # type: str
        self.with_certificate = with_certificate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.checked is not None:
            result['Checked'] = self.checked
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Checked') is not None:
            self.checked = m.get('Checked')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class ListDomainsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListDomainsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDomainsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListDomainsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBody, self).to_map()
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
            temp_model = ListDomainsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDomainsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentOverviewsRequest(TeaModel):
    def __init__(self, app_id=None, source=None):
        self.app_id = app_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentOverviewsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListEnvironmentOverviewsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, config=None, create_time=None, current_publish=None, endpoint=None, env_id=None,
                 env_status=None, env_type=None, latest_app_access_time=None, modified_time=None, ops_record=None,
                 publishing=None):
        self.app_id = app_id  # type: str
        self.config = config  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.current_publish = current_publish  # type: dict[str, str]
        self.endpoint = endpoint  # type: str
        self.env_id = env_id  # type: str
        self.env_status = env_status  # type: str
        self.env_type = env_type  # type: str
        self.latest_app_access_time = latest_app_access_time  # type: str
        self.modified_time = modified_time  # type: str
        self.ops_record = ops_record  # type: dict[str, str]
        self.publishing = publishing  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentOverviewsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish is not None:
            result['CurrentPublish'] = self.current_publish
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_status is not None:
            result['EnvStatus'] = self.env_status
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.latest_app_access_time is not None:
            result['LatestAppAccessTime'] = self.latest_app_access_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.ops_record is not None:
            result['OpsRecord'] = self.ops_record
        if self.publishing is not None:
            result['Publishing'] = self.publishing
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublish') is not None:
            self.current_publish = m.get('CurrentPublish')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('LatestAppAccessTime') is not None:
            self.latest_app_access_time = m.get('LatestAppAccessTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OpsRecord') is not None:
            self.ops_record = m.get('OpsRecord')
        if m.get('Publishing') is not None:
            self.publishing = m.get('Publishing')
        return self


class ListEnvironmentOverviewsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListEnvironmentOverviewsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentOverviewsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListEnvironmentOverviewsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListEnvironmentOverviewsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListEnvironmentOverviewsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentOverviewsResponseBody, self).to_map()
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
            temp_model = ListEnvironmentOverviewsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnvironmentOverviewsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEnvironmentOverviewsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentOverviewsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentOverviewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(self, app_id=None, env_type=None, source=None):
        self.app_id = app_id  # type: str
        self.env_type = env_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListEnvironmentsResponseBodyDataItems(TeaModel):
    def __init__(self, account_ops_endpoint=None, app_id=None, create_time=None, current_publish_id=None,
                 endpoint=None, env_id=None, env_type=None, modified_time=None, publishing_id=None):
        self.account_ops_endpoint = account_ops_endpoint  # type: str
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: str
        self.current_publish_id = current_publish_id  # type: str
        self.endpoint = endpoint  # type: str
        self.env_id = env_id  # type: str
        self.env_type = env_type  # type: str
        self.modified_time = modified_time  # type: str
        self.publishing_id = publishing_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ops_endpoint is not None:
            result['AccountOpsEndpoint'] = self.account_ops_endpoint
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish_id is not None:
            result['CurrentPublishId'] = self.current_publish_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publishing_id is not None:
            result['PublishingId'] = self.publishing_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountOpsEndpoint') is not None:
            self.account_ops_endpoint = m.get('AccountOpsEndpoint')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublishId') is not None:
            self.current_publish_id = m.get('CurrentPublishId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishingId') is not None:
            self.publishing_id = m.get('PublishingId')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListEnvironmentsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListEnvironmentsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListEnvironmentsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBody, self).to_map()
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
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEnvironmentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequest(TeaModel):
    def __init__(self, app_id=None, model_id=None, model_name=None, model_type=None, module_id=None,
                 schema_version=None, source=None, sub_type=None, with_content=None):
        self.app_id = app_id  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_type = model_type  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModelsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ListModelsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListModelsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModelsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModelsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModelsResponseBody, self).to_map()
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
            temp_model = ListModelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsByPageRequest(TeaModel):
    def __init__(self, app_id=None, model_name=None, model_type=None, module_id=None, page_number=None,
                 page_size=None, schema_version=None, source=None, sub_type=None, with_content=None):
        self.app_id = app_id  # type: str
        self.model_name = model_name  # type: str
        self.model_type = model_type  # type: str
        self.module_id = module_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModelsByPageResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsByPageResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ListModelsByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListModelsByPageResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModelsByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModelsByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelsByPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModelsByPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModelsByPageResponseBody, self).to_map()
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
            temp_model = ListModelsByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModelsByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModelsByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModelsByPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModelsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleDependenciesRequest(TeaModel):
    def __init__(self, module_id=None, recursive=None, source=None):
        self.module_id = module_id  # type: str
        self.recursive = recursive  # type: bool
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleDependenciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModuleDependenciesResponseBodyDataItems(TeaModel):
    def __init__(self, commit_id=None, description=None, direct_dependency=None, icon=None,
                 minimum_platform_version=None, module_id=None, module_name=None, origin=None, owner_user_id=None, platform=None,
                 version=None):
        self.commit_id = commit_id  # type: str
        self.description = description  # type: str
        self.direct_dependency = direct_dependency  # type: bool
        self.icon = icon  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.origin = origin  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleDependenciesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.direct_dependency is not None:
            result['DirectDependency'] = self.direct_dependency
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectDependency') is not None:
            self.direct_dependency = m.get('DirectDependency')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListModuleDependenciesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListModuleDependenciesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModuleDependenciesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleDependenciesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleDependenciesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModuleDependenciesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModuleDependenciesResponseBody, self).to_map()
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
            temp_model = ListModuleDependenciesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleDependenciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModuleDependenciesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModuleDependenciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleDependenciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleModelsRequest(TeaModel):
    def __init__(self, module_list=None, source=None, sub_types=None, with_content=None):
        self.module_list = module_list  # type: str
        self.source = source  # type: str
        self.sub_types = sub_types  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleModelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_types is not None:
            result['SubTypes'] = self.sub_types
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubTypes') is not None:
            self.sub_types = m.get('SubTypes')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModuleModelsResponseBodyDataItems(TeaModel):
    def __init__(self, commit_id=None, model_data=None, model_data_path=None, model_digest=None, module_id=None,
                 resource_data=None, resource_data_path=None):
        self.commit_id = commit_id  # type: str
        self.model_data = model_data  # type: dict[str, list[DataItemsModelDataValue]]
        self.model_data_path = model_data_path  # type: dict[str, str]
        self.model_digest = model_digest  # type: dict[str, str]
        self.module_id = module_id  # type: str
        self.resource_data = resource_data  # type: dict[str, str]
        self.resource_data_path = resource_data_path  # type: dict[str, str]

    def validate(self):
        if self.model_data:
            for v in self.model_data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListModuleModelsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        result['ModelData'] = {}
        if self.model_data is not None:
            for k, v in self.model_data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['ModelData'][k] = l1
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data is not None:
            result['ResourceData'] = self.resource_data
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        self.model_data = {}
        if m.get('ModelData') is not None:
            for k, v in m.get('ModelData').items():
                l1 = []
                for k1 in v:
                    temp_model = DataItemsModelDataValue()
                    l1.append(temp_model.from_map(k1))
                self.model_data['k'] = l1
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceData') is not None:
            self.resource_data = m.get('ResourceData')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        return self


class ListModuleModelsResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListModuleModelsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModuleModelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleModelsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleModelsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModuleModelsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModuleModelsResponseBody, self).to_map()
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
            temp_model = ListModuleModelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleModelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModuleModelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModuleModelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulePublishVersionsRequest(TeaModel):
    def __init__(self, custom_parent_id=None, module_id=None, module_version=None, page_number=None, page_size=None,
                 source=None):
        self.custom_parent_id = custom_parent_id  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulePublishVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_version is not None:
            result['ModuleVersion'] = self.module_version
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleVersion') is not None:
            self.module_version = m.get('ModuleVersion')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulePublishVersionsResponseBodyDataItems(TeaModel):
    def __init__(self, commit_id=None, create_time=None, description=None, modified_time=None, module_id=None,
                 platform_version=None, publish_id=None, version=None):
        self.commit_id = commit_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.platform_version = platform_version  # type: str
        self.publish_id = publish_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulePublishVersionsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListModulePublishVersionsResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListModulePublishVersionsResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModulePublishVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulePublishVersionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModulePublishVersionsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModulePublishVersionsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModulePublishVersionsResponseBody, self).to_map()
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
            temp_model = ListModulePublishVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulePublishVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModulePublishVersionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModulePublishVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulePublishVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleResourcesRequest(TeaModel):
    def __init__(self, module_list=None, source=None, types=None, with_content=None):
        self.module_list = module_list  # type: str
        self.source = source  # type: str
        self.types = types  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.source is not None:
            result['Source'] = self.source
        if self.types is not None:
            result['Types'] = self.types
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModuleResourcesResponseBodyDataItems(TeaModel):
    def __init__(self, commit_id=None, model_data=None, model_data_path=None, module_id=None, resource_data=None,
                 resource_data_path=None):
        self.commit_id = commit_id  # type: str
        self.model_data = model_data  # type: dict[str, str]
        self.model_data_path = model_data_path  # type: dict[str, str]
        self.module_id = module_id  # type: str
        self.resource_data = resource_data  # type: dict[str, list[DataItemsResourceDataValue]]
        self.resource_data_path = resource_data_path  # type: dict[str, str]

    def validate(self):
        if self.resource_data:
            for v in self.resource_data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListModuleResourcesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.model_data is not None:
            result['ModelData'] = self.model_data
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        result['ResourceData'] = {}
        if self.resource_data is not None:
            for k, v in self.resource_data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['ResourceData'][k] = l1
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModelData') is not None:
            self.model_data = m.get('ModelData')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        self.resource_data = {}
        if m.get('ResourceData') is not None:
            for k, v in m.get('ResourceData').items():
                l1 = []
                for k1 in v:
                    temp_model = DataItemsResourceDataValue()
                    l1.append(temp_model.from_map(k1))
                self.resource_data['k'] = l1
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        return self


class ListModuleResourcesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListModuleResourcesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModuleResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModuleResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModuleResourcesResponseBody, self).to_map()
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
            temp_model = ListModuleResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModuleResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModuleResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesRequest(TeaModel):
    def __init__(self, description=None, has_owner_app=None, module_id=None, module_name=None, platform=None,
                 source=None):
        self.description = description  # type: str
        self.has_owner_app = has_owner_app  # type: bool
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.platform = platform  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulesResponseBodyDataItems(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 owner_app_id=None, owner_user_id=None, platform=None, platform_version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.platform_version = platform_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListModulesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListModulesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModulesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModulesResponseBody, self).to_map()
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
            temp_model = ListModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesByPageRequest(TeaModel):
    def __init__(self, custom_parent_id=None, description=None, has_owner_app=None, module_id=None,
                 module_name=None, module_type=None, page_number=None, page_size=None, platform=None, source=None):
        self.custom_parent_id = custom_parent_id  # type: str
        self.description = description  # type: str
        self.has_owner_app = has_owner_app  # type: bool
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.platform = platform  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulesByPageResponseBodyDataItems(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 module_type=None, owner_app_id=None, owner_user_id=None, platform=None, platform_version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.platform_version = platform_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesByPageResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListModulesByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListModulesByPageResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModulesByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulesByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModulesByPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListModulesByPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListModulesByPageResponseBody, self).to_map()
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
            temp_model = ListModulesByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulesByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModulesByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModulesByPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishVersionsRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishVersionsResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, commit_id=None, completion_time=None, create_time=None, description=None,
                 env_id=None, modified_time=None, publish_id=None, publish_status=None, publish_type=None, reason=None,
                 start_time=None, sub_tasks=None, version_number=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.completion_time = completion_time  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.env_id = env_id  # type: str
        self.modified_time = modified_time  # type: str
        self.publish_id = publish_id  # type: str
        self.publish_status = publish_status  # type: str
        self.publish_type = publish_type  # type: str
        self.reason = reason  # type: str
        self.start_time = start_time  # type: str
        self.sub_tasks = sub_tasks  # type: list[dict[str, str]]
        self.version_number = version_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishVersionsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class ListPublishVersionsResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListPublishVersionsResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublishVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishVersionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishVersionsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListPublishVersionsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPublishVersionsResponseBody, self).to_map()
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
            temp_model = ListPublishVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublishVersionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublishVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedModulesRequest(TeaModel):
    def __init__(self, description=None, exclude_app_id=None, exclude_module_id=None, has_owner_app=None,
                 module_id=None, module_name=None, module_type=None, page_number=None, page_size=None, platform=None,
                 source=None):
        self.description = description  # type: str
        self.exclude_app_id = exclude_app_id  # type: str
        self.exclude_module_id = exclude_module_id  # type: str
        self.has_owner_app = has_owner_app  # type: bool
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.platform = platform  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishedModulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_app_id is not None:
            result['ExcludeAppId'] = self.exclude_app_id
        if self.exclude_module_id is not None:
            result['ExcludeModuleId'] = self.exclude_module_id
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAppId') is not None:
            self.exclude_app_id = m.get('ExcludeAppId')
        if m.get('ExcludeModuleId') is not None:
            self.exclude_module_id = m.get('ExcludeModuleId')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishedModulesResponseBodyDataItems(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 module_type=None, owner_app_id=None, owner_user_id=None, platform=None, platform_version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.module_type = module_type  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str
        self.platform_version = platform_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishedModulesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListPublishedModulesResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListPublishedModulesResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublishedModulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishedModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishedModulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListPublishedModulesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPublishedModulesResponseBody, self).to_map()
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
            temp_model = ListPublishedModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishedModulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublishedModulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublishedModulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishedModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishesRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None, publish_status=None,
                 publish_type=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.publish_status = publish_status  # type: str
        self.publish_type = publish_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishesResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, commit_id=None, completion_time=None, create_time=None, description=None,
                 env_id=None, modified_time=None, publish_id=None, publish_status=None, publish_type=None, reason=None,
                 start_time=None, version_number=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.completion_time = completion_time  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.env_id = env_id  # type: str
        self.modified_time = modified_time  # type: str
        self.publish_id = publish_id  # type: str
        self.publish_status = publish_status  # type: str
        self.publish_type = publish_type  # type: str
        self.reason = reason  # type: str
        self.start_time = start_time  # type: str
        self.version_number = version_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class ListPublishesResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListPublishesResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublishesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListPublishesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPublishesResponseBody, self).to_map()
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
            temp_model = ListPublishesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublishesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublishesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, app_id=None, description=None, image_process_parameter=None, module_id=None,
                 resource_id=None, resource_name=None, resource_type=None, source=None, with_content=None):
        self.app_id = app_id  # type: str
        self.description = description  # type: str
        self.image_process_parameter = image_process_parameter  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.source = source  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListResourcesResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_digest=None, resource_id=None, resource_name=None, resource_type=None,
                 revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: any
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_digest = resource_digest  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListResourcesResponseBodyData(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[ListResourcesResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBody, self).to_map()
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
            temp_model = ListResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesByPageRequest(TeaModel):
    def __init__(self, app_id=None, description=None, image_process_parameter=None, module_id=None,
                 page_number=None, page_size=None, resource_id=None, resource_name=None, resource_type=None, source=None,
                 with_content=None):
        self.app_id = app_id  # type: str
        self.description = description  # type: str
        self.image_process_parameter = image_process_parameter  # type: str
        self.module_id = module_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.source = source  # type: str
        self.with_content = with_content  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListResourcesByPageResponseBodyDataItems(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_digest=None, resource_id=None, resource_name=None, resource_type=None,
                 revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_digest = resource_digest  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesByPageResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListResourcesByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, total_count=None):
        self.items = items  # type: list[ListResourcesByPageResponseBodyDataItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListResourcesByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesByPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListResourcesByPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListResourcesByPageResponseBody, self).to_map()
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
            temp_model = ListResourcesByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourcesByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesByPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppUserPasswordRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None, user_name=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAppUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ResetAppUserPasswordResponseBodyData(TeaModel):
    def __init__(self, password=None, user_name=None):
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAppUserPasswordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ResetAppUserPasswordResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ResetAppUserPasswordResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ResetAppUserPasswordResponseBody, self).to_map()
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
            temp_model = ResetAppUserPasswordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAppUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetAppUserPasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAppUserPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAppUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreModelRequest(TeaModel):
    def __init__(self, app_id=None, model_id=None, module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.model_id = model_id  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class RestoreModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_id=None, model_name=None, model_status=None,
                 model_type=None, modified_time=None, module_id=None, props=None, revision=None, schema_version=None,
                 sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class RestoreModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RestoreModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RestoreModelResponseBody, self).to_map()
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
            temp_model = RestoreModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestoreModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestoreModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunLogicModelRequest(TeaModel):
    def __init__(self, app_id=None, commit_id=None, content=None, encode_type=None, module_id=None, parameters=None,
                 schema_version=None, source=None, sub_type=None):
        self.app_id = app_id  # type: str
        self.commit_id = commit_id  # type: str
        self.content = content  # type: str
        self.encode_type = encode_type  # type: str
        self.module_id = module_id  # type: str
        self.parameters = parameters  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunLogicModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.content is not None:
            result['Content'] = self.content
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class RunLogicModelResponseBodyData(TeaModel):
    def __init__(self, body=None, headers=None, status=None):
        self.body = body  # type: str
        self.headers = headers  # type: dict[str, str]
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunLogicModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RunLogicModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RunLogicModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RunLogicModelResponseBody, self).to_map()
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
            temp_model = RunLogicModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunLogicModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RunLogicModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunLogicModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunLogicModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEnvironmentDefaultDomainRequest(TeaModel):
    def __init__(self, app_id=None, domain=None, domain_type=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.domain = domain  # type: str
        self.domain_type = domain_type  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEnvironmentDefaultDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SetEnvironmentDefaultDomainResponseBodyData(TeaModel):
    def __init__(self, config_changed=None, default_master_domain=None, default_static_domain=None,
                 master_domain=None, master_domain_applied=None, static_domain=None, static_domain_applied=None):
        self.config_changed = config_changed  # type: bool
        self.default_master_domain = default_master_domain  # type: str
        self.default_static_domain = default_static_domain  # type: str
        self.master_domain = master_domain  # type: str
        self.master_domain_applied = master_domain_applied  # type: bool
        self.static_domain = static_domain  # type: str
        self.static_domain_applied = static_domain_applied  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEnvironmentDefaultDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_changed is not None:
            result['ConfigChanged'] = self.config_changed
        if self.default_master_domain is not None:
            result['DefaultMasterDomain'] = self.default_master_domain
        if self.default_static_domain is not None:
            result['DefaultStaticDomain'] = self.default_static_domain
        if self.master_domain is not None:
            result['MasterDomain'] = self.master_domain
        if self.master_domain_applied is not None:
            result['MasterDomainApplied'] = self.master_domain_applied
        if self.static_domain is not None:
            result['StaticDomain'] = self.static_domain
        if self.static_domain_applied is not None:
            result['StaticDomainApplied'] = self.static_domain_applied
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigChanged') is not None:
            self.config_changed = m.get('ConfigChanged')
        if m.get('DefaultMasterDomain') is not None:
            self.default_master_domain = m.get('DefaultMasterDomain')
        if m.get('DefaultStaticDomain') is not None:
            self.default_static_domain = m.get('DefaultStaticDomain')
        if m.get('MasterDomain') is not None:
            self.master_domain = m.get('MasterDomain')
        if m.get('MasterDomainApplied') is not None:
            self.master_domain_applied = m.get('MasterDomainApplied')
        if m.get('StaticDomain') is not None:
            self.static_domain = m.get('StaticDomain')
        if m.get('StaticDomainApplied') is not None:
            self.static_domain_applied = m.get('StaticDomainApplied')
        return self


class SetEnvironmentDefaultDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: SetEnvironmentDefaultDomainResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SetEnvironmentDefaultDomainResponseBody, self).to_map()
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
            temp_model = SetEnvironmentDefaultDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetEnvironmentDefaultDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetEnvironmentDefaultDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetEnvironmentDefaultDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetEnvironmentDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAppServerRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAppServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class StartAppServerResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_server_status=None, env_id=None):
        self.app_id = app_id  # type: str
        self.app_server_status = app_server_status  # type: str
        self.env_id = env_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAppServerResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_server_status is not None:
            result['AppServerStatus'] = self.app_server_status
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppServerStatus') is not None:
            self.app_server_status = m.get('AppServerStatus')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StartAppServerResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: StartAppServerResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartAppServerResponseBody, self).to_map()
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
            temp_model = StartAppServerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAppServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartAppServerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartAppServerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppServerRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, source=None):
        self.app_id = app_id  # type: str
        self.env_id = env_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class StopAppServerResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_server_status=None, env_id=None):
        self.app_id = app_id  # type: str
        self.app_server_status = app_server_status  # type: str
        self.env_id = env_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppServerResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_server_status is not None:
            result['AppServerStatus'] = self.app_server_status
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppServerStatus') is not None:
            self.app_server_status = m.get('AppServerStatus')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StopAppServerResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: StopAppServerResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopAppServerResponseBody, self).to_map()
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
            temp_model = StopAppServerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopAppServerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAppServerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, icon=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateAppResponseBodyDataCategories(TeaModel):
    def __init__(self, category_id=None, category_name=None, parent_category_id=None):
        self.category_id = category_id  # type: str
        self.category_name = category_name  # type: str
        self.parent_category_id = parent_category_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppResponseBodyDataCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class UpdateAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None, app_type=None, categories=None, create_time=None,
                 description=None, icon=None, is_template=None, last_edit_time=None, main_module_id=None, modified_time=None,
                 schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_status = app_status  # type: str
        self.app_type = app_type  # type: str
        self.categories = categories  # type: list[UpdateAppResponseBodyDataCategories]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.is_template = is_template  # type: bool
        self.last_edit_time = last_edit_time  # type: str
        self.main_module_id = main_module_id  # type: str
        self.modified_time = modified_time  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = UpdateAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateAppResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateAppResponseBody, self).to_map()
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
            temp_model = UpdateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppModelRequest(TeaModel):
    def __init__(self, app_id=None, content=None, encode_type=None, schema_version=None, source=None, sub_type=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: str
        self.encode_type = encode_type  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class UpdateAppModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class UpdateAppModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateAppModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateAppModelResponseBody, self).to_map()
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
            temp_model = UpdateAppModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelRequest(TeaModel):
    def __init__(self, app_id=None, content=None, description=None, encode_type=None, model_id=None, model_name=None,
                 module_id=None, schema_version=None, source=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.encode_type = encode_type  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.module_id = module_id  # type: str
        self.schema_version = schema_version  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateModelResponseBodyData(TeaModel):
    def __init__(self, app_id=None, attributes=None, content=None, create_time=None, description=None, id=None,
                 link_model_id=None, link_module_id=None, linked=None, model_digest=None, model_id=None, model_name=None,
                 model_status=None, model_type=None, modified_time=None, module_id=None, props=None, revision=None,
                 schema_version=None, sub_type=None, visibility=None):
        self.app_id = app_id  # type: str
        self.attributes = attributes  # type: list[dict[str, str]]
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.link_model_id = link_model_id  # type: str
        self.link_module_id = link_module_id  # type: str
        self.linked = linked  # type: bool
        self.model_digest = model_digest  # type: str
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: str
        self.model_type = model_type  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.props = props  # type: dict[str, str]
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str
        self.sub_type = sub_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class UpdateModelResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateModelResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateModelResponseBody, self).to_map()
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
            temp_model = UpdateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleRequest(TeaModel):
    def __init__(self, description=None, module_id=None, module_name=None, source=None):
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateModuleResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, icon=None, latest_published_commit=None,
                 latest_published_version=None, minimum_platform_version=None, modified_time=None, module_id=None, module_name=None,
                 owner_app_id=None, owner_user_id=None, platform=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.latest_published_commit = latest_published_commit  # type: str
        self.latest_published_version = latest_published_version  # type: str
        self.minimum_platform_version = minimum_platform_version  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.module_name = module_name  # type: str
        self.owner_app_id = owner_app_id  # type: str
        self.owner_user_id = owner_user_id  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class UpdateModuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateModuleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateModuleResponseBody, self).to_map()
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
            temp_model = UpdateModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(self, app_id=None, content=None, description=None, module_id=None, resource_id=None,
                 resource_name=None, source=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_digest=None, resource_id=None, resource_name=None, resource_type=None,
                 revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_digest = resource_digest  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateResourceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateResourceResponseBody, self).to_map()
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
            temp_model = UpdateResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceContentRequest(TeaModel):
    def __init__(self, app_id=None, content=None, module_id=None, resource_id=None, source=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceContentResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_id=None, resource_name=None, resource_type=None, revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceContentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceContentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateResourceContentResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateResourceContentResponseBody, self).to_map()
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
            temp_model = UpdateResourceContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceContentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceInfoRequest(TeaModel):
    def __init__(self, app_id=None, description=None, module_id=None, resource_id=None, resource_name=None,
                 source=None):
        self.app_id = app_id  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceInfoResponseBodyData(TeaModel):
    def __init__(self, app_id=None, content=None, create_time=None, description=None, modified_time=None,
                 module_id=None, resource_id=None, resource_name=None, resource_type=None, revision=None, schema_version=None):
        self.app_id = app_id  # type: str
        self.content = content  # type: dict[str, str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.module_id = module_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.revision = revision  # type: int
        self.schema_version = schema_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceInfoResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateResourceInfoResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateResourceInfoResponseBody, self).to_map()
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
            temp_model = UpdateResourceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


