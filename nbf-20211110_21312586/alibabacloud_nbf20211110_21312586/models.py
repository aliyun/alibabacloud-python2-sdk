# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApiTestRequest(TeaModel):
    def __init__(self, test_cmd=None):
        self.test_cmd = test_cmd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApiTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.test_cmd is not None:
            result['testCmd'] = self.test_cmd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('testCmd') is not None:
            self.test_cmd = m.get('testCmd')
        return self


class ApiTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApiTestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class BuildSdkRequest(TeaModel):
    def __init__(self, build_cmd=None):
        self.build_cmd = build_cmd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuildSdkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_cmd is not None:
            result['buildCmd'] = self.build_cmd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildCmd') is not None:
            self.build_cmd = m.get('buildCmd')
        return self


class BuildSdkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuildSdkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateAndReleaseApiRequest(TeaModel):
    def __init__(self, creat_api_cmd=None):
        self.creat_api_cmd = creat_api_cmd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAndReleaseApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creat_api_cmd is not None:
            result['creatApiCmd'] = self.creat_api_cmd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatApiCmd') is not None:
            self.creat_api_cmd = m.get('creatApiCmd')
        return self


class CreateAndReleaseApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAndReleaseApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateSdkVersionRequest(TeaModel):
    def __init__(self, create_sdk_cmd=None):
        self.create_sdk_cmd = create_sdk_cmd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSdkVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_sdk_cmd is not None:
            result['createSdkCmd'] = self.create_sdk_cmd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createSdkCmd') is not None:
            self.create_sdk_cmd = m.get('createSdkCmd')
        return self


class CreateSdkVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSdkVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DeleteApiRequest(TeaModel):
    def __init__(self, api_external_id=None):
        self.api_external_id = api_external_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_external_id is not None:
            result['apiExternalId'] = self.api_external_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiExternalId') is not None:
            self.api_external_id = m.get('apiExternalId')
        return self


class DeleteApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetResultRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class OpenApiGenericProxyResponseBody(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenApiGenericProxyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class OpenApiGenericProxyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenApiGenericProxyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenApiGenericProxyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenApiGenericProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreCheckRequest(TeaModel):
    def __init__(self, api_schema_dto=None, group_version_extra_info=None, namespace_external_id=None):
        self.api_schema_dto = api_schema_dto  # type: str
        self.group_version_extra_info = group_version_extra_info  # type: str
        self.namespace_external_id = namespace_external_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_schema_dto is not None:
            result['apiSchemaDTO'] = self.api_schema_dto
        if self.group_version_extra_info is not None:
            result['groupVersionExtraInfo'] = self.group_version_extra_info
        if self.namespace_external_id is not None:
            result['namespaceExternalId'] = self.namespace_external_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiSchemaDTO') is not None:
            self.api_schema_dto = m.get('apiSchemaDTO')
        if m.get('groupVersionExtraInfo') is not None:
            self.group_version_extra_info = m.get('groupVersionExtraInfo')
        if m.get('namespaceExternalId') is not None:
            self.namespace_external_id = m.get('namespaceExternalId')
        return self


class PreCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreCheckResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PublishSdkRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishSdkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class PublishSdkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishSdkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class SerializeApiRequest(TeaModel):
    def __init__(self, api_schema_dto=None, type=None):
        self.api_schema_dto = api_schema_dto  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SerializeApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_schema_dto is not None:
            result['apiSchemaDTO'] = self.api_schema_dto
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiSchemaDTO') is not None:
            self.api_schema_dto = m.get('apiSchemaDTO')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SerializeApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SerializeApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateAndReleaseApiRequest(TeaModel):
    def __init__(self, update_api_cmd=None):
        self.update_api_cmd = update_api_cmd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAndReleaseApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_api_cmd is not None:
            result['updateApiCmd'] = self.update_api_cmd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('updateApiCmd') is not None:
            self.update_api_cmd = m.get('updateApiCmd')
        return self


class UpdateAndReleaseApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAndReleaseApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


