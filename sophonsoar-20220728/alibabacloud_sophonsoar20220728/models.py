# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchModifyInstanceStatusRequest(TeaModel):
    def __init__(self, active=None, lang=None, playbook_uuid=None):
        self.active = active  # type: int
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchModifyInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class BatchModifyInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchModifyInstanceStatusResponseBody, self).to_map()
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


class BatchModifyInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchModifyInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchModifyInstanceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchModifyInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComparePlaybooksRequest(TeaModel):
    def __init__(self, lang=None, new_playbook_release_id=None, old_playbook_release_id=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.new_playbook_release_id = new_playbook_release_id  # type: int
        self.old_playbook_release_id = old_playbook_release_id  # type: int
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComparePlaybooksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_playbook_release_id is not None:
            result['NewPlaybookReleaseId'] = self.new_playbook_release_id
        if self.old_playbook_release_id is not None:
            result['OldPlaybookReleaseId'] = self.old_playbook_release_id
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewPlaybookReleaseId') is not None:
            self.new_playbook_release_id = m.get('NewPlaybookReleaseId')
        if m.get('OldPlaybookReleaseId') is not None:
            self.old_playbook_release_id = m.get('OldPlaybookReleaseId')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ComparePlaybooksResponseBodyCompareResult(TeaModel):
    def __init__(self, description=None, new=None, same=None):
        self.description = description  # type: str
        self.new = new  # type: bool
        self.same = same  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComparePlaybooksResponseBodyCompareResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.new is not None:
            result['New'] = self.new
        if self.same is not None:
            result['Same'] = self.same
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('New') is not None:
            self.new = m.get('New')
        if m.get('Same') is not None:
            self.same = m.get('Same')
        return self


class ComparePlaybooksResponseBody(TeaModel):
    def __init__(self, compare_result=None, request_id=None):
        self.compare_result = compare_result  # type: ComparePlaybooksResponseBodyCompareResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.compare_result:
            self.compare_result.validate()

    def to_map(self):
        _map = super(ComparePlaybooksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_result is not None:
            result['CompareResult'] = self.compare_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareResult') is not None:
            temp_model = ComparePlaybooksResponseBodyCompareResult()
            self.compare_result = temp_model.from_map(m['CompareResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ComparePlaybooksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ComparePlaybooksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ComparePlaybooksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ComparePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePlaybookRequest(TeaModel):
    def __init__(self, description=None, display_name=None, lang=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class CreatePlaybookResponseBodyData(TeaModel):
    def __init__(self, playbook_uuid=None):
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class CreatePlaybookResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreatePlaybookResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePlaybookResponseBody, self).to_map()
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
            temp_model = CreatePlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugPlaybookRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None, record=None, taskflow=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.record = record  # type: str
        self.taskflow = taskflow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebugPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.record is not None:
            result['Record'] = self.record
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class DebugPlaybookResponseBody(TeaModel):
    def __init__(self, request_id=None, request_uuid=None):
        self.request_id = request_id  # type: str
        self.request_uuid = request_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebugPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DebugPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DebugPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DebugPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DebugPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentAssetRequest(TeaModel):
    def __init__(self, asset_id=None, lang=None):
        self.asset_id = asset_id  # type: long
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteComponentAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteComponentAssetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteComponentAssetResponseBody, self).to_map()
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


class DeleteComponentAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteComponentAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteComponentAssetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePlaybookRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DeletePlaybookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePlaybookResponseBody, self).to_map()
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


class DeletePlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiListRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeApiListResponseBodyApiList(TeaModel):
    def __init__(self, doc_url=None, pop_code=None, product_name=None):
        self.doc_url = doc_url  # type: str
        self.pop_code = pop_code  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiListResponseBodyApiList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class DescribeApiListResponseBody(TeaModel):
    def __init__(self, api_list=None, request_id=None):
        self.api_list = api_list  # type: list[DescribeApiListResponseBodyApiList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.api_list:
            for k in self.api_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiList'] = []
        if self.api_list is not None:
            for k in self.api_list:
                result['ApiList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k in m.get('ApiList'):
                temp_model = DescribeApiListResponseBodyApiList()
                self.api_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentAssetFormRequest(TeaModel):
    def __init__(self, component_name=None, lang=None):
        self.component_name = component_name  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentAssetFormRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentAssetFormResponseBody(TeaModel):
    def __init__(self, component_asset_form=None, request_id=None):
        self.component_asset_form = component_asset_form  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentAssetFormResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_form is not None:
            result['ComponentAssetForm'] = self.component_asset_form
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentAssetForm') is not None:
            self.component_asset_form = m.get('ComponentAssetForm')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentAssetFormResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentAssetFormResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentAssetFormResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentAssetFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentAssetsRequest(TeaModel):
    def __init__(self, component_name=None, lang=None):
        self.component_name = component_name  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentAssetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentAssetsResponseBodyComponentAssets(TeaModel):
    def __init__(self, asset_uuid=None, componentname=None, gmt_create=None, gmt_modified=None, id=None, name=None,
                 params=None):
        self.asset_uuid = asset_uuid  # type: str
        self.componentname = componentname  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentAssetsResponseBodyComponentAssets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_uuid is not None:
            result['AssetUuid'] = self.asset_uuid
        if self.componentname is not None:
            result['Componentname'] = self.componentname
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetUuid') is not None:
            self.asset_uuid = m.get('AssetUuid')
        if m.get('Componentname') is not None:
            self.componentname = m.get('Componentname')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class DescribeComponentAssetsResponseBody(TeaModel):
    def __init__(self, component_assets=None, request_id=None):
        self.component_assets = component_assets  # type: list[DescribeComponentAssetsResponseBodyComponentAssets]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.component_assets:
            for k in self.component_assets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeComponentAssetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentAssets'] = []
        if self.component_assets is not None:
            for k in self.component_assets:
                result['ComponentAssets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component_assets = []
        if m.get('ComponentAssets') is not None:
            for k in m.get('ComponentAssets'):
                temp_model = DescribeComponentAssetsResponseBodyComponentAssets()
                self.component_assets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentAssetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentAssetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentAssetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentListRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeComponentListResponseBody(TeaModel):
    def __init__(self, components=None, request_id=None):
        self.components = components  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components is not None:
            result['Components'] = self.components
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentPlaybookRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeComponentPlaybookResponseBodyPlaybooks(TeaModel):
    def __init__(self, description=None, display_name=None, input_params=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.input_params = input_params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentPlaybookResponseBodyPlaybooks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        return self


class DescribeComponentPlaybookResponseBody(TeaModel):
    def __init__(self, playbooks=None, request_id=None):
        self.playbooks = playbooks  # type: list[DescribeComponentPlaybookResponseBodyPlaybooks]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.playbooks:
            for k in self.playbooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeComponentPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k in self.playbooks:
                result['Playbooks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k in m.get('Playbooks'):
                temp_model = DescribeComponentPlaybookResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentsJsRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentsJsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentsJsResponseBody(TeaModel):
    def __init__(self, components_js=None, request_id=None):
        self.components_js = components_js  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentsJsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components_js is not None:
            result['ComponentsJs'] = self.components_js
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentsJs') is not None:
            self.components_js = m.get('ComponentsJs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentsJsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentsJsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentsJsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentsJsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistinctReleasesRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None, taskflow_md_5=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.taskflow_md_5 = taskflow_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDistinctReleasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribeDistinctReleasesResponseBodyRecords(TeaModel):
    def __init__(self, description=None, taskflow_md_5=None):
        self.description = description  # type: str
        self.taskflow_md_5 = taskflow_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDistinctReleasesResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribeDistinctReleasesResponseBody(TeaModel):
    def __init__(self, records=None, request_id=None):
        self.records = records  # type: list[DescribeDistinctReleasesResponseBodyRecords]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDistinctReleasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDistinctReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDistinctReleasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDistinctReleasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDistinctReleasesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDistinctReleasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnumItemsRequest(TeaModel):
    def __init__(self, enum_type=None, lang=None):
        self.enum_type = enum_type  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnumItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enum_type is not None:
            result['EnumType'] = self.enum_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnumType') is not None:
            self.enum_type = m.get('EnumType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeEnumItemsResponseBodyData(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnumItemsResponseBodyData, self).to_map()
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


class DescribeEnumItemsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[DescribeEnumItemsResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnumItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEnumItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnumItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEnumItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEnumItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEnumItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExecutePlaybooksRequest(TeaModel):
    def __init__(self, lang=None, param_type=None, playbook_name=None, uuid=None):
        self.lang = lang  # type: str
        self.param_type = param_type  # type: str
        self.playbook_name = playbook_name  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExecutePlaybooksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeExecutePlaybooksResponseBodyPlaybookMetrics(TeaModel):
    def __init__(self, description=None, display_name=None, param_config=None, param_type=None, uuid=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.param_config = param_config  # type: str
        self.param_type = param_type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExecutePlaybooksResponseBodyPlaybookMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.param_config is not None:
            result['ParamConfig'] = self.param_config
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParamConfig') is not None:
            self.param_config = m.get('ParamConfig')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeExecutePlaybooksResponseBody(TeaModel):
    def __init__(self, playbook_metrics=None, request_id=None):
        self.playbook_metrics = playbook_metrics  # type: list[DescribeExecutePlaybooksResponseBodyPlaybookMetrics]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.playbook_metrics:
            for k in self.playbook_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExecutePlaybooksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PlaybookMetrics'] = []
        if self.playbook_metrics is not None:
            for k in self.playbook_metrics:
                result['PlaybookMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.playbook_metrics = []
        if m.get('PlaybookMetrics') is not None:
            for k in m.get('PlaybookMetrics'):
                temp_model = DescribeExecutePlaybooksResponseBodyPlaybookMetrics()
                self.playbook_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExecutePlaybooksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExecutePlaybooksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExecutePlaybooksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeExecutePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFieldRequest(TeaModel):
    def __init__(self, lang=None, query_key=None):
        self.lang = lang  # type: str
        self.query_key = query_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        return self


class DescribeFieldResponseBody(TeaModel):
    def __init__(self, fields=None, name=None, request_id=None):
        self.fields = fields  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFieldResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFieldResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLatestRecordSchemaRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLatestRecordSchemaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema(TeaModel):
    def __init__(self, action_name=None, component_name=None, node_name=None, output_fields=None):
        self.action_name = action_name  # type: str
        self.component_name = component_name  # type: str
        self.node_name = node_name  # type: str
        self.output_fields = output_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.output_fields is not None:
            result['OutputFields'] = self.output_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OutputFields') is not None:
            self.output_fields = m.get('OutputFields')
        return self


class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema(TeaModel):
    def __init__(self, node_schema=None):
        self.node_schema = node_schema  # type: list[DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema]

    def validate(self):
        if self.node_schema:
            for k in self.node_schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeSchema'] = []
        if self.node_schema is not None:
            for k in self.node_schema:
                result['NodeSchema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_schema = []
        if m.get('NodeSchema') is not None:
            for k in m.get('NodeSchema'):
                temp_model = DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema()
                self.node_schema.append(temp_model.from_map(k))
        return self


class DescribeLatestRecordSchemaResponseBody(TeaModel):
    def __init__(self, playbook_node_schema=None, request_id=None):
        self.playbook_node_schema = playbook_node_schema  # type: DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema
        self.request_id = request_id  # type: str

    def validate(self):
        if self.playbook_node_schema:
            self.playbook_node_schema.validate()

    def to_map(self):
        _map = super(DescribeLatestRecordSchemaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_node_schema is not None:
            result['PlaybookNodeSchema'] = self.playbook_node_schema.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookNodeSchema') is not None:
            temp_model = DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema()
            self.playbook_node_schema = temp_model.from_map(m['PlaybookNodeSchema'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLatestRecordSchemaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLatestRecordSchemaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLatestRecordSchemaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLatestRecordSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeParamTagsRequest(TeaModel):
    def __init__(self, lang=None, node_name=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.node_name = node_name  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeParamTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeNodeParamTagsResponseBodyParamReferredPaths(TeaModel):
    def __init__(self, param_name=None, referred_path=None):
        self.param_name = param_name  # type: str
        self.referred_path = referred_path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeParamTagsResponseBodyParamReferredPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.referred_path is not None:
            result['ReferredPath'] = self.referred_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ReferredPath') is not None:
            self.referred_path = m.get('ReferredPath')
        return self


class DescribeNodeParamTagsResponseBody(TeaModel):
    def __init__(self, param_referred_paths=None, request_id=None):
        self.param_referred_paths = param_referred_paths  # type: list[DescribeNodeParamTagsResponseBodyParamReferredPaths]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.param_referred_paths:
            for k in self.param_referred_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNodeParamTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParamReferredPaths'] = []
        if self.param_referred_paths is not None:
            for k in self.param_referred_paths:
                result['ParamReferredPaths'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.param_referred_paths = []
        if m.get('ParamReferredPaths') is not None:
            for k in m.get('ParamReferredPaths'):
                temp_model = DescribeNodeParamTagsResponseBodyParamReferredPaths()
                self.param_referred_paths.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeParamTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeParamTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeParamTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeParamTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeUsedInfosRequest(TeaModel):
    def __init__(self, lang=None, node_name=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.node_name = node_name  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeUsedInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeNodeUsedInfosResponseBody(TeaModel):
    def __init__(self, node_used_infos=None, request_id=None):
        self.node_used_infos = node_used_infos  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeUsedInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_used_infos is not None:
            result['NodeUsedInfos'] = self.node_used_infos
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeUsedInfos') is not None:
            self.node_used_infos = m.get('NodeUsedInfos')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeUsedInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeUsedInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeUsedInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeUsedInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookRequest(TeaModel):
    def __init__(self, debug_flag=None, lang=None, playbook_uuid=None, taskflow_md_5=None):
        self.debug_flag = debug_flag  # type: int
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.taskflow_md_5 = taskflow_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_flag is not None:
            result['DebugFlag'] = self.debug_flag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebugFlag') is not None:
            self.debug_flag = m.get('DebugFlag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribePlaybookResponseBodyPlaybook(TeaModel):
    def __init__(self, creator=None, description=None, display_name=None, fail_exe_num=None, gmt_create=None,
                 gmt_modified=None, input_params=None, last_exe_time=None, modifier=None, online_active=None,
                 online_release_taskflow_md_5=None, own_type=None, playbook_uuid=None, success_exe_num=None, taskflow=None):
        self.creator = creator  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.fail_exe_num = fail_exe_num  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.input_params = input_params  # type: str
        self.last_exe_time = last_exe_time  # type: long
        self.modifier = modifier  # type: str
        self.online_active = online_active  # type: bool
        self.online_release_taskflow_md_5 = online_release_taskflow_md_5  # type: str
        self.own_type = own_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.success_exe_num = success_exe_num  # type: int
        self.taskflow = taskflow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookResponseBodyPlaybook, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.fail_exe_num is not None:
            result['FailExeNum'] = self.fail_exe_num
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.last_exe_time is not None:
            result['LastExeTime'] = self.last_exe_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.online_active is not None:
            result['OnlineActive'] = self.online_active
        if self.online_release_taskflow_md_5 is not None:
            result['OnlineReleaseTaskflowMd5'] = self.online_release_taskflow_md_5
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.success_exe_num is not None:
            result['SuccessExeNum'] = self.success_exe_num
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FailExeNum') is not None:
            self.fail_exe_num = m.get('FailExeNum')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('LastExeTime') is not None:
            self.last_exe_time = m.get('LastExeTime')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('OnlineActive') is not None:
            self.online_active = m.get('OnlineActive')
        if m.get('OnlineReleaseTaskflowMd5') is not None:
            self.online_release_taskflow_md_5 = m.get('OnlineReleaseTaskflowMd5')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('SuccessExeNum') is not None:
            self.success_exe_num = m.get('SuccessExeNum')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class DescribePlaybookResponseBody(TeaModel):
    def __init__(self, playbook=None, request_id=None):
        self.playbook = playbook  # type: DescribePlaybookResponseBodyPlaybook
        self.request_id = request_id  # type: str

    def validate(self):
        if self.playbook:
            self.playbook.validate()

    def to_map(self):
        _map = super(DescribePlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook is not None:
            result['Playbook'] = self.playbook.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Playbook') is not None:
            temp_model = DescribePlaybookResponseBodyPlaybook()
            self.playbook = temp_model.from_map(m['Playbook'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookInputOutputRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookInputOutputRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookInputOutputResponseBodyConfig(TeaModel):
    def __init__(self, input_params=None, output_params=None, param_type=None, playbook_uuid=None):
        self.input_params = input_params  # type: str
        self.output_params = output_params  # type: str
        self.param_type = param_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookInputOutputResponseBodyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookInputOutputResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        self.config = config  # type: DescribePlaybookInputOutputResponseBodyConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(DescribePlaybookInputOutputResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribePlaybookInputOutputResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookInputOutputResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookInputOutputResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookInputOutputResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookInputOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookMetricsRequest(TeaModel):
    def __init__(self, lang=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookMetricsResponseBodyMetrics(TeaModel):
    def __init__(self, active=None, description=None, display_name=None, fail_num=None, gmt_create=None,
                 history_md_5=None, last_runtime=None, own_type=None, playbook_uuid=None, succ_num=None):
        self.active = active  # type: int
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.fail_num = fail_num  # type: int
        self.gmt_create = gmt_create  # type: long
        self.history_md_5 = history_md_5  # type: int
        self.last_runtime = last_runtime  # type: long
        self.own_type = own_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.succ_num = succ_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookMetricsResponseBodyMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.fail_num is not None:
            result['FailNum'] = self.fail_num
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.history_md_5 is not None:
            result['HistoryMd5'] = self.history_md_5
        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.succ_num is not None:
            result['SuccNum'] = self.succ_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HistoryMd5') is not None:
            self.history_md_5 = m.get('HistoryMd5')
        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('SuccNum') is not None:
            self.succ_num = m.get('SuccNum')
        return self


class DescribePlaybookMetricsResponseBody(TeaModel):
    def __init__(self, metrics=None, request_id=None):
        self.metrics = metrics  # type: DescribePlaybookMetricsResponseBodyMetrics
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super(DescribePlaybookMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = DescribePlaybookMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookNodesOutputRequest(TeaModel):
    def __init__(self, lang=None, node_name=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.node_name = node_name  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookNodesOutputRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput(TeaModel):
    def __init__(self, node_name=None, node_output=None):
        self.node_name = node_name  # type: str
        self.node_output = node_output  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_output is not None:
            result['NodeOutput'] = self.node_output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')
        return self


class DescribePlaybookNodesOutputResponseBody(TeaModel):
    def __init__(self, playbook_nodes_output=None, request_id=None):
        self.playbook_nodes_output = playbook_nodes_output  # type: DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput
        self.request_id = request_id  # type: str

    def validate(self):
        if self.playbook_nodes_output:
            self.playbook_nodes_output.validate()

    def to_map(self):
        _map = super(DescribePlaybookNodesOutputResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_nodes_output is not None:
            result['PlaybookNodesOutput'] = self.playbook_nodes_output.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookNodesOutput') is not None:
            temp_model = DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput()
            self.playbook_nodes_output = temp_model.from_map(m['PlaybookNodesOutput'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookNodesOutputResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookNodesOutputResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookNodesOutputResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookNodesOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookNumberMetricsRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookNumberMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribePlaybookNumberMetricsResponseBodyMetrics(TeaModel):
    def __init__(self, start_up_num=None, total_num=None):
        self.start_up_num = start_up_num  # type: int
        self.total_num = total_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookNumberMetricsResponseBodyMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_up_num is not None:
            result['StartUpNum'] = self.start_up_num
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartUpNum') is not None:
            self.start_up_num = m.get('StartUpNum')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class DescribePlaybookNumberMetricsResponseBody(TeaModel):
    def __init__(self, metrics=None, request_id=None):
        self.metrics = metrics  # type: DescribePlaybookNumberMetricsResponseBodyMetrics
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super(DescribePlaybookNumberMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = DescribePlaybookNumberMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookNumberMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookNumberMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookNumberMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookNumberMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookReleasesRequest(TeaModel):
    def __init__(self, lang=None, page_number=None, page_size=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookReleasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookReleasesResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookReleasesResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePlaybookReleasesResponseBodyRecords(TeaModel):
    def __init__(self, creator=None, description=None, gmt_create=None, gmt_modified=None, id=None,
                 taskflow_md_5=None):
        self.creator = creator  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: int
        self.taskflow_md_5 = taskflow_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybookReleasesResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribePlaybookReleasesResponseBody(TeaModel):
    def __init__(self, page=None, records=None, request_id=None):
        self.page = page  # type: DescribePlaybookReleasesResponseBodyPage
        self.records = records  # type: list[DescribePlaybookReleasesResponseBodyRecords]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page:
            self.page.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePlaybookReleasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribePlaybookReleasesResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribePlaybookReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookReleasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybookReleasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybookReleasesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookReleasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybooksRequest(TeaModel):
    def __init__(self, active=None, end_millis=None, lang=None, name=None, own_type=None, page_number=None,
                 page_size=None, playbook_uuid=None, start_millis=None):
        self.active = active  # type: int
        self.end_millis = end_millis  # type: long
        self.lang = lang  # type: str
        self.name = name  # type: str
        self.own_type = own_type  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.start_millis = start_millis  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybooksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')
        return self


class DescribePlaybooksResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybooksResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePlaybooksResponseBodyPlaybooks(TeaModel):
    def __init__(self, active=None, display_name=None, gmt_create=None, last_runtime=None, own_type=None,
                 playbook_uuid=None):
        self.active = active  # type: int
        self.display_name = display_name  # type: str
        self.gmt_create = gmt_create  # type: long
        self.last_runtime = last_runtime  # type: long
        self.own_type = own_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlaybooksResponseBodyPlaybooks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybooksResponseBody(TeaModel):
    def __init__(self, page=None, playbooks=None, request_id=None):
        self.page = page  # type: DescribePlaybooksResponseBodyPage
        self.playbooks = playbooks  # type: list[DescribePlaybooksResponseBodyPlaybooks]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page:
            self.page.validate()
        if self.playbooks:
            for k in self.playbooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePlaybooksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k in self.playbooks:
                result['Playbooks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribePlaybooksResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k in m.get('Playbooks'):
                temp_model = DescribePlaybooksResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybooksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlaybooksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlaybooksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePopApiRequest(TeaModel):
    def __init__(self, api_name=None, api_version=None, env=None, pop_code=None):
        self.api_name = api_name  # type: str
        self.api_version = api_version  # type: str
        self.env = env  # type: str
        self.pop_code = pop_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.env is not None:
            result['Env'] = self.env
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        return self


class DescribePopApiResponseBodyOpenApiMetaList(TeaModel):
    def __init__(self, description=None, example_value=None, name=None, required=None, type=None):
        self.description = description  # type: str
        self.example_value = example_value  # type: str
        self.name = name  # type: str
        self.required = required  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiResponseBodyOpenApiMetaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePopApiResponseBody(TeaModel):
    def __init__(self, api_name=None, open_api_meta_list=None, pop_code=None, request_id=None, version=None):
        self.api_name = api_name  # type: str
        self.open_api_meta_list = open_api_meta_list  # type: list[DescribePopApiResponseBodyOpenApiMetaList]
        self.pop_code = pop_code  # type: str
        self.request_id = request_id  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.open_api_meta_list:
            for k in self.open_api_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePopApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        result['OpenApiMetaList'] = []
        if self.open_api_meta_list is not None:
            for k in self.open_api_meta_list:
                result['OpenApiMetaList'].append(k.to_map() if k else None)
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        self.open_api_meta_list = []
        if m.get('OpenApiMetaList') is not None:
            for k in m.get('OpenApiMetaList'):
                temp_model = DescribePopApiResponseBodyOpenApiMetaList()
                self.open_api_meta_list.append(temp_model.from_map(k))
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePopApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePopApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePopApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePopApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePopApiItemListRequest(TeaModel):
    def __init__(self, api_name=None, api_version=None, env=None, lang=None, pop_code=None):
        self.api_name = api_name  # type: str
        self.api_version = api_version  # type: str
        self.env = env  # type: str
        self.lang = lang  # type: str
        self.pop_code = pop_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiItemListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.env is not None:
            result['Env'] = self.env
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        return self


class DescribePopApiItemListResponseBody(TeaModel):
    def __init__(self, names=None, pop_code=None, request_id=None, total=None, version=None):
        self.names = names  # type: list[str]
        self.pop_code = pop_code  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiItemListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePopApiItemListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePopApiItemListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePopApiItemListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePopApiItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePopApiVersionListRequest(TeaModel):
    def __init__(self, env=None, lang=None, pop_code=None):
        self.env = env  # type: str
        self.lang = lang  # type: str
        self.pop_code = pop_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiVersionListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        return self


class DescribePopApiVersionListResponseBodyVersionList(TeaModel):
    def __init__(self, api_name=None, pop_code=None, version=None):
        self.api_name = api_name  # type: str
        self.pop_code = pop_code  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePopApiVersionListResponseBodyVersionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePopApiVersionListResponseBody(TeaModel):
    def __init__(self, pop_code=None, request_id=None, total=None, version_list=None):
        self.pop_code = pop_code  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: int
        self.version_list = version_list  # type: list[DescribePopApiVersionListResponseBodyVersionList]

    def validate(self):
        if self.version_list:
            for k in self.version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePopApiVersionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['VersionList'] = []
        if self.version_list is not None:
            for k in self.version_list:
                result['VersionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.version_list = []
        if m.get('VersionList') is not None:
            for k in m.get('VersionList'):
                temp_model = DescribePopApiVersionListResponseBodyVersionList()
                self.version_list.append(temp_model.from_map(k))
        return self


class DescribePopApiVersionListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePopApiVersionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePopApiVersionListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePopApiVersionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessTasksRequest(TeaModel):
    def __init__(self, direction=None, entity_name=None, entity_type=None, order_field=None, page_number=None,
                 page_size=None, param_content=None, process_action_end=None, process_action_start=None,
                 process_remove_end=None, process_remove_start=None, process_strategy_uuid=None, scene_code=None, scope=None,
                 source=None, task_id=None, task_status=None, yun_code=None):
        self.direction = direction  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.order_field = order_field  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: int
        self.param_content = param_content  # type: str
        self.process_action_end = process_action_end  # type: long
        self.process_action_start = process_action_start  # type: long
        self.process_remove_end = process_remove_end  # type: long
        self.process_remove_start = process_remove_start  # type: long
        self.process_strategy_uuid = process_strategy_uuid  # type: str
        self.scene_code = scene_code  # type: str
        self.scope = scope  # type: str
        self.source = source  # type: str
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str
        self.yun_code = yun_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.param_content is not None:
            result['ParamContent'] = self.param_content
        if self.process_action_end is not None:
            result['ProcessActionEnd'] = self.process_action_end
        if self.process_action_start is not None:
            result['ProcessActionStart'] = self.process_action_start
        if self.process_remove_end is not None:
            result['ProcessRemoveEnd'] = self.process_remove_end
        if self.process_remove_start is not None:
            result['ProcessRemoveStart'] = self.process_remove_start
        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.yun_code is not None:
            result['YunCode'] = self.yun_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParamContent') is not None:
            self.param_content = m.get('ParamContent')
        if m.get('ProcessActionEnd') is not None:
            self.process_action_end = m.get('ProcessActionEnd')
        if m.get('ProcessActionStart') is not None:
            self.process_action_start = m.get('ProcessActionStart')
        if m.get('ProcessRemoveEnd') is not None:
            self.process_remove_end = m.get('ProcessRemoveEnd')
        if m.get('ProcessRemoveStart') is not None:
            self.process_remove_start = m.get('ProcessRemoveStart')
        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')
        return self


class DescribeProcessTasksResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessTasksResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProcessTasksResponseBodyProcessTasks(TeaModel):
    def __init__(self, creator=None, entity_name=None, entity_type=None, gmt_create_millis=None,
                 gmt_modified_millis=None, input_params=None, process_strategy_uuid=None, process_time=None, remove_time=None,
                 scene_code=None, scene_name=None, scope=None, source=None, task_id=None, task_status=None, yun_code=None):
        self.creator = creator  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.gmt_create_millis = gmt_create_millis  # type: long
        self.gmt_modified_millis = gmt_modified_millis  # type: long
        self.input_params = input_params  # type: str
        self.process_strategy_uuid = process_strategy_uuid  # type: str
        self.process_time = process_time  # type: long
        self.remove_time = remove_time  # type: long
        self.scene_code = scene_code  # type: str
        self.scene_name = scene_name  # type: str
        self.scope = scope  # type: str
        self.source = source  # type: str
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: int
        self.yun_code = yun_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessTasksResponseBodyProcessTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create_millis is not None:
            result['GmtCreateMillis'] = self.gmt_create_millis
        if self.gmt_modified_millis is not None:
            result['GmtModifiedMillis'] = self.gmt_modified_millis
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.remove_time is not None:
            result['RemoveTime'] = self.remove_time
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.yun_code is not None:
            result['YunCode'] = self.yun_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreateMillis') is not None:
            self.gmt_create_millis = m.get('GmtCreateMillis')
        if m.get('GmtModifiedMillis') is not None:
            self.gmt_modified_millis = m.get('GmtModifiedMillis')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('RemoveTime') is not None:
            self.remove_time = m.get('RemoveTime')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')
        return self


class DescribeProcessTasksResponseBody(TeaModel):
    def __init__(self, page=None, process_tasks=None, request_id=None):
        self.page = page  # type: DescribeProcessTasksResponseBodyPage
        self.process_tasks = process_tasks  # type: list[DescribeProcessTasksResponseBodyProcessTasks]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page:
            self.page.validate()
        if self.process_tasks:
            for k in self.process_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProcessTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['ProcessTasks'] = []
        if self.process_tasks is not None:
            for k in self.process_tasks:
                result['ProcessTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribeProcessTasksResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.process_tasks = []
        if m.get('ProcessTasks') is not None:
            for k in m.get('ProcessTasks'):
                temp_model = DescribeProcessTasksResponseBodyProcessTasks()
                self.process_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeProcessTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProcessTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProcessTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordActionOutputListRequest(TeaModel):
    def __init__(self, action_uuid=None, lang=None, page_number=None, page_size=None):
        self.action_uuid = action_uuid  # type: str
        self.lang = lang  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordActionOutputListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSoarRecordActionOutputListResponseBody(TeaModel):
    def __init__(self, action_outputs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.action_outputs = action_outputs  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordActionOutputListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_outputs is not None:
            result['ActionOutputs'] = self.action_outputs
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
        if m.get('ActionOutputs') is not None:
            self.action_outputs = m.get('ActionOutputs')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSoarRecordActionOutputListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSoarRecordActionOutputListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSoarRecordActionOutputListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordActionOutputListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordInOutputRequest(TeaModel):
    def __init__(self, action_uuid=None, lang=None):
        self.action_uuid = action_uuid  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordInOutputRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeSoarRecordInOutputResponseBody(TeaModel):
    def __init__(self, in_output_info=None, request_id=None):
        self.in_output_info = in_output_info  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordInOutputResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_output_info is not None:
            result['InOutputInfo'] = self.in_output_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InOutputInfo') is not None:
            self.in_output_info = m.get('InOutputInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSoarRecordInOutputResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSoarRecordInOutputResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSoarRecordInOutputResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordInOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordsRequest(TeaModel):
    def __init__(self, end_millis=None, lang=None, page_number=None, page_size=None, playbook_uuid=None,
                 start_millis=None, task_status=None, taskflow_md_5=None, trigger_user=None):
        self.end_millis = end_millis  # type: long
        self.lang = lang  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.playbook_uuid = playbook_uuid  # type: str
        self.start_millis = start_millis  # type: long
        self.task_status = task_status  # type: str
        self.taskflow_md_5 = taskflow_md_5  # type: str
        self.trigger_user = trigger_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarRecordsResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordsResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSoarRecordsResponseBodySoarExecuteRecords(TeaModel):
    def __init__(self, end_time=None, error_msg=None, raw_event_req=None, request_uuid=None, result_message=None,
                 start_time=None, status=None, task_name=None, task_type=None, taskflow_md_5=None, trigger_type=None,
                 trigger_user=None):
        self.end_time = end_time  # type: long
        self.error_msg = error_msg  # type: str
        self.raw_event_req = raw_event_req  # type: str
        self.request_uuid = request_uuid  # type: str
        self.result_message = result_message  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.task_name = task_name  # type: str
        self.task_type = task_type  # type: str
        self.taskflow_md_5 = taskflow_md_5  # type: str
        self.trigger_type = trigger_type  # type: str
        self.trigger_user = trigger_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarRecordsResponseBodySoarExecuteRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.raw_event_req is not None:
            result['RawEventReq'] = self.raw_event_req
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RawEventReq') is not None:
            self.raw_event_req = m.get('RawEventReq')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarRecordsResponseBody(TeaModel):
    def __init__(self, page=None, request_id=None, soar_execute_records=None):
        self.page = page  # type: DescribeSoarRecordsResponseBodyPage
        self.request_id = request_id  # type: str
        self.soar_execute_records = soar_execute_records  # type: list[DescribeSoarRecordsResponseBodySoarExecuteRecords]

    def validate(self):
        if self.page:
            self.page.validate()
        if self.soar_execute_records:
            for k in self.soar_execute_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSoarRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SoarExecuteRecords'] = []
        if self.soar_execute_records is not None:
            for k in self.soar_execute_records:
                result['SoarExecuteRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribeSoarRecordsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.soar_execute_records = []
        if m.get('SoarExecuteRecords') is not None:
            for k in m.get('SoarExecuteRecords'):
                temp_model = DescribeSoarRecordsResponseBodySoarExecuteRecords()
                self.soar_execute_records.append(temp_model.from_map(k))
        return self


class DescribeSoarRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSoarRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSoarRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarTaskAndActionsRequest(TeaModel):
    def __init__(self, lang=None, request_uuid=None):
        self.lang = lang  # type: str
        self.request_uuid = request_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarTaskAndActionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DescribeSoarTaskAndActionsResponseBodyDetailsActions(TeaModel):
    def __init__(self, action=None, action_uuid=None, asset_name=None, component=None, end_time=None, node_name=None,
                 request_uuid=None, start_time=None, status=None, task_name=None, task_status=None, trigger_user=None):
        self.action = action  # type: str
        self.action_uuid = action_uuid  # type: str
        self.asset_name = asset_name  # type: str
        self.component = component  # type: str
        self.end_time = end_time  # type: long
        self.node_name = node_name  # type: str
        self.request_uuid = request_uuid  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: str
        self.trigger_user = trigger_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSoarTaskAndActionsResponseBodyDetailsActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.component is not None:
            result['Component'] = self.component
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarTaskAndActionsResponseBodyDetails(TeaModel):
    def __init__(self, actions=None, end_time=None, error_msg=None, raw_event_req=None, request_uuid=None,
                 result_level=None, result_message=None, start_time=None, status=None, task_flow_md_5=None, task_name=None,
                 task_tenant_id=None, trigger_type=None, trigger_user=None):
        self.actions = actions  # type: list[DescribeSoarTaskAndActionsResponseBodyDetailsActions]
        self.end_time = end_time  # type: long
        self.error_msg = error_msg  # type: str
        self.raw_event_req = raw_event_req  # type: str
        self.request_uuid = request_uuid  # type: str
        self.result_level = result_level  # type: str
        self.result_message = result_message  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.task_flow_md_5 = task_flow_md_5  # type: str
        self.task_name = task_name  # type: str
        self.task_tenant_id = task_tenant_id  # type: str
        self.trigger_type = trigger_type  # type: str
        self.trigger_user = trigger_user  # type: str

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSoarTaskAndActionsResponseBodyDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.raw_event_req is not None:
            result['RawEventReq'] = self.raw_event_req
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.result_level is not None:
            result['ResultLevel'] = self.result_level
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_flow_md_5 is not None:
            result['TaskFlowMd5'] = self.task_flow_md_5
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_tenant_id is not None:
            result['TaskTenantId'] = self.task_tenant_id
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DescribeSoarTaskAndActionsResponseBodyDetailsActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RawEventReq') is not None:
            self.raw_event_req = m.get('RawEventReq')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('ResultLevel') is not None:
            self.result_level = m.get('ResultLevel')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskFlowMd5') is not None:
            self.task_flow_md_5 = m.get('TaskFlowMd5')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskTenantId') is not None:
            self.task_tenant_id = m.get('TaskTenantId')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarTaskAndActionsResponseBody(TeaModel):
    def __init__(self, details=None, request_id=None):
        self.details = details  # type: DescribeSoarTaskAndActionsResponseBodyDetails
        self.request_id = request_id  # type: str

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super(DescribeSoarTaskAndActionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = DescribeSoarTaskAndActionsResponseBodyDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSoarTaskAndActionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSoarTaskAndActionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSoarTaskAndActionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarTaskAndActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSophonCommandsRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSophonCommandsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSophonCommandsResponseBodyDataParamConfig(TeaModel):
    def __init__(self, check_field=None, field=None, necessary=None, value=None):
        self.check_field = check_field  # type: str
        self.field = field  # type: str
        self.necessary = necessary  # type: bool
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSophonCommandsResponseBodyDataParamConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_field is not None:
            result['CheckField'] = self.check_field
        if self.field is not None:
            result['Field'] = self.field
        if self.necessary is not None:
            result['Necessary'] = self.necessary
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckField') is not None:
            self.check_field = m.get('CheckField')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Necessary') is not None:
            self.necessary = m.get('Necessary')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeSophonCommandsResponseBodyData(TeaModel):
    def __init__(self, description=None, display_name=None, name=None, param_config=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.name = name  # type: str
        self.param_config = param_config  # type: list[DescribeSophonCommandsResponseBodyDataParamConfig]

    def validate(self):
        if self.param_config:
            for k in self.param_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSophonCommandsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        result['ParamConfig'] = []
        if self.param_config is not None:
            for k in self.param_config:
                result['ParamConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.param_config = []
        if m.get('ParamConfig') is not None:
            for k in m.get('ParamConfig'):
                temp_model = DescribeSophonCommandsResponseBodyDataParamConfig()
                self.param_config.append(temp_model.from_map(k))
        return self


class DescribeSophonCommandsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[DescribeSophonCommandsResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSophonCommandsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeSophonCommandsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSophonCommandsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSophonCommandsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSophonCommandsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSophonCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescriberPython3ScriptLogsRequest(TeaModel):
    def __init__(self, lang=None, request_uuid=None):
        self.lang = lang  # type: str
        self.request_uuid = request_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescriberPython3ScriptLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DescriberPython3ScriptLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, run_result=None):
        self.request_id = request_id  # type: str
        self.run_result = run_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescriberPython3ScriptLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        return self


class DescriberPython3ScriptLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescriberPython3ScriptLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescriberPython3ScriptLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescriberPython3ScriptLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyComponentAssetRequest(TeaModel):
    def __init__(self, asset_config=None, lang=None):
        self.asset_config = asset_config  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyComponentAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_config is not None:
            result['AssetConfig'] = self.asset_config
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetConfig') is not None:
            self.asset_config = m.get('AssetConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ModifyComponentAssetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyComponentAssetResponseBody, self).to_map()
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


class ModifyComponentAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyComponentAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyComponentAssetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookRequest(TeaModel):
    def __init__(self, description=None, display_name=None, lang=None, playbook_uuid=None, taskflow=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.taskflow = taskflow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class ModifyPlaybookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookResponseBody, self).to_map()
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


class ModifyPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookInputOutputRequest(TeaModel):
    def __init__(self, input_params=None, lang=None, output_params=None, param_type=None, playbook_uuid=None):
        self.input_params = input_params  # type: str
        self.lang = lang  # type: str
        self.output_params = output_params  # type: str
        self.param_type = param_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookInputOutputRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ModifyPlaybookInputOutputResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookInputOutputResponseBody, self).to_map()
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


class ModifyPlaybookInputOutputResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPlaybookInputOutputResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPlaybookInputOutputResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookInputOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookInstanceStatusRequest(TeaModel):
    def __init__(self, active=None, lang=None, playbook_uuid=None):
        self.active = active  # type: int
        self.lang = lang  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ModifyPlaybookInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlaybookInstanceStatusResponseBody, self).to_map()
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


class ModifyPlaybookInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPlaybookInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPlaybookInstanceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishPlaybookRequest(TeaModel):
    def __init__(self, description=None, playbook_uuid=None):
        self.description = description  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class PublishPlaybookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishPlaybookResponseBody, self).to_map()
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


class PublishPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTreeDataRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTreeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class QueryTreeDataResponseBody(TeaModel):
    def __init__(self, playbooks=None, request_id=None):
        self.playbooks = playbooks  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTreeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbooks is not None:
            result['Playbooks'] = self.playbooks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Playbooks') is not None:
            self.playbooks = m.get('Playbooks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTreeDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTreeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTreeDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTreeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenamePlaybookNodeRequest(TeaModel):
    def __init__(self, lang=None, new_node_name=None, old_node_name=None, playbook_uuid=None):
        self.lang = lang  # type: str
        self.new_node_name = new_node_name  # type: str
        self.old_node_name = old_node_name  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenamePlaybookNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_node_name is not None:
            result['NewNodeName'] = self.new_node_name
        if self.old_node_name is not None:
            result['OldNodeName'] = self.old_node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewNodeName') is not None:
            self.new_node_name = m.get('NewNodeName')
        if m.get('OldNodeName') is not None:
            self.old_node_name = m.get('OldNodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class RenamePlaybookNodeResponseBody(TeaModel):
    def __init__(self, rename_result=None, request_id=None):
        self.rename_result = rename_result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenamePlaybookNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rename_result is not None:
            result['RenameResult'] = self.rename_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenameResult') is not None:
            self.rename_result = m.get('RenameResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenamePlaybookNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenamePlaybookNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenamePlaybookNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenamePlaybookNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertPlaybookReleaseRequest(TeaModel):
    def __init__(self, is_publish=None, play_release_id=None, playbook_uuid=None):
        self.is_publish = is_publish  # type: bool
        self.play_release_id = play_release_id  # type: int
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevertPlaybookReleaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_publish is not None:
            result['IsPublish'] = self.is_publish
        if self.play_release_id is not None:
            result['PlayReleaseId'] = self.play_release_id
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsPublish') is not None:
            self.is_publish = m.get('IsPublish')
        if m.get('PlayReleaseId') is not None:
            self.play_release_id = m.get('PlayReleaseId')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class RevertPlaybookReleaseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevertPlaybookReleaseResponseBody, self).to_map()
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


class RevertPlaybookReleaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevertPlaybookReleaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevertPlaybookReleaseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertPlaybookReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPython3ScriptRequest(TeaModel):
    def __init__(self, node_name=None, params=None, playbook_uuid=None, python_script=None):
        self.node_name = node_name  # type: str
        self.params = params  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.python_script = python_script  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPython3ScriptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.params is not None:
            result['Params'] = self.params
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.python_script is not None:
            result['PythonScript'] = self.python_script
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('PythonScript') is not None:
            self.python_script = m.get('PythonScript')
        return self


class RunPython3ScriptResponseBody(TeaModel):
    def __init__(self, request_id=None, run_result=None):
        self.request_id = request_id  # type: str
        self.run_result = run_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPython3ScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        return self


class RunPython3ScriptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RunPython3ScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunPython3ScriptResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunPython3ScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerPlaybookRequest(TeaModel):
    def __init__(self, input_param=None, playbook_uuid=None):
        self.input_param = input_param  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_param is not None:
            result['InputParam'] = self.input_param
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputParam') is not None:
            self.input_param = m.get('InputParam')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class TriggerPlaybookResponseBody(TeaModel):
    def __init__(self, request_id=None, trigger_uuid=None):
        self.request_id = request_id  # type: str
        self.trigger_uuid = trigger_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger_uuid is not None:
            result['TriggerUuid'] = self.trigger_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TriggerUuid') is not None:
            self.trigger_uuid = m.get('TriggerUuid')
        return self


class TriggerPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerProcessTaskRequest(TeaModel):
    def __init__(self, action_type=None, task_id=None):
        self.action_type = action_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerProcessTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TriggerProcessTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerProcessTaskResponseBody, self).to_map()
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


class TriggerProcessTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerProcessTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerProcessTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerProcessTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerSophonPlaybookRequest(TeaModel):
    def __init__(self, command_name=None, input_params=None, sophon_task_id=None, trigger_type=None, uuid=None):
        self.command_name = command_name  # type: str
        self.input_params = input_params  # type: str
        self.sophon_task_id = sophon_task_id  # type: str
        self.trigger_type = trigger_type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerSophonPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class TriggerSophonPlaybookResponseBodyData(TeaModel):
    def __init__(self, sophon_task_id=None):
        self.sophon_task_id = sophon_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerSophonPlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class TriggerSophonPlaybookResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: TriggerSophonPlaybookResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TriggerSophonPlaybookResponseBody, self).to_map()
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
            temp_model = TriggerSophonPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerSophonPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerSophonPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerSophonPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerSophonPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPlaybookRequest(TeaModel):
    def __init__(self, playbook_uuid=None, task_flow=None):
        self.playbook_uuid = playbook_uuid  # type: str
        self.task_flow = task_flow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.task_flow is not None:
            result['TaskFlow'] = self.task_flow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskFlow') is not None:
            self.task_flow = m.get('TaskFlow')
        return self


class VerifyPlaybookResponseBodyCheckTaskInfos(TeaModel):
    def __init__(self, detail=None, node_name=None, risk_level=None):
        self.detail = detail  # type: str
        self.node_name = node_name  # type: str
        self.risk_level = risk_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPlaybookResponseBodyCheckTaskInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class VerifyPlaybookResponseBody(TeaModel):
    def __init__(self, check_task_infos=None, request_id=None):
        self.check_task_infos = check_task_infos  # type: list[VerifyPlaybookResponseBodyCheckTaskInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.check_task_infos:
            for k in self.check_task_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifyPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckTaskInfos'] = []
        if self.check_task_infos is not None:
            for k in self.check_task_infos:
                result['CheckTaskInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.check_task_infos = []
        if m.get('CheckTaskInfos') is not None:
            for k in m.get('CheckTaskInfos'):
                temp_model = VerifyPlaybookResponseBodyCheckTaskInfos()
                self.check_task_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPythonFileRequest(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPythonFileRequest, self).to_map()
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


class VerifyPythonFileResponseBodySyntax(TeaModel):
    def __init__(self, end_column=None, end_line_number=None, message=None, severity=None, start_column=None,
                 start_line_number=None):
        self.end_column = end_column  # type: int
        self.end_line_number = end_line_number  # type: int
        self.message = message  # type: str
        self.severity = severity  # type: int
        self.start_column = start_column  # type: int
        self.start_line_number = start_line_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPythonFileResponseBodySyntax, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_column is not None:
            result['EndColumn'] = self.end_column
        if self.end_line_number is not None:
            result['EndLineNumber'] = self.end_line_number
        if self.message is not None:
            result['Message'] = self.message
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_column is not None:
            result['StartColumn'] = self.start_column
        if self.start_line_number is not None:
            result['StartLineNumber'] = self.start_line_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')
        if m.get('EndLineNumber') is not None:
            self.end_line_number = m.get('EndLineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')
        if m.get('StartLineNumber') is not None:
            self.start_line_number = m.get('StartLineNumber')
        return self


class VerifyPythonFileResponseBody(TeaModel):
    def __init__(self, request_id=None, syntax=None):
        self.request_id = request_id  # type: str
        self.syntax = syntax  # type: list[VerifyPythonFileResponseBodySyntax]

    def validate(self):
        if self.syntax:
            for k in self.syntax:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifyPythonFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Syntax'] = []
        if self.syntax is not None:
            for k in self.syntax:
                result['Syntax'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.syntax = []
        if m.get('Syntax') is not None:
            for k in m.get('Syntax'):
                temp_model = VerifyPythonFileResponseBodySyntax()
                self.syntax.append(temp_model.from_map(k))
        return self


class VerifyPythonFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyPythonFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyPythonFileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyPythonFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


