# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAudioAsyncRequest(TeaModel):
    def __init__(self, watermark_id=None, url_list=None):
        self.watermark_id = watermark_id  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAudioAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddAudioAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAudioAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddAudioAsyncResponseBody(TeaModel):
    def __init__(self, msg=None, request_id=None, data=None):
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AddAudioAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddAudioAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddAudioAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddAudioAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddAudioAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAudioAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAudioAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDocAsyncRequest(TeaModel):
    def __init__(self, watermark_id=None, url_list=None):
        self.watermark_id = watermark_id  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDocAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddDocAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDocAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddDocAsyncResponseBody(TeaModel):
    def __init__(self, msg=None, request_id=None, data=None):
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AddDocAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddDocAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddDocAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddDocAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDocAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDocAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDocAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageAsyncRequest(TeaModel):
    def __init__(self, watermark_id=None, url_list=None):
        self.watermark_id = watermark_id  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddImageAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddImageAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AddImageAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddImageAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddImageAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddImageAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddImageAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageSyncRequest(TeaModel):
    def __init__(self, watermark_id=None, url_list=None):
        self.watermark_id = watermark_id  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddImageSyncResponseBodyData(TeaModel):
    def __init__(self, result_url=None, data_id=None):
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageSyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['dataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        return self


class AddImageSyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AddImageSyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddImageSyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddImageSyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddImageSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageSyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddImageSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVideoAsyncRequest(TeaModel):
    def __init__(self, watermark_id=None, vm_type=None, url_list=None):
        self.watermark_id = watermark_id  # type: str
        self.vm_type = vm_type  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVideoAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.vm_type is not None:
            result['VmType'] = self.vm_type
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('VmType') is not None:
            self.vm_type = m.get('VmType')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddVideoAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVideoAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddVideoAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AddVideoAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddVideoAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddVideoAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddVideoAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddVideoAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVideoAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddVideoAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioAddRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioAddRequest, self).to_map()
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


class GetAudioAddResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, result_url=None, data_id=None, gmt_modified=None,
                 media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None, finished_time=None,
                 id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioAddResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAudioAddResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetAudioAddResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAudioAddResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioAddResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioAddResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAudioAddResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAudioAddResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAudioAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioAsyncRequest(TeaModel):
    def __init__(self, app_name=None, url_list=None, water_mark_type=None):
        self.app_name = app_name  # type: str
        self.url_list = url_list  # type: str
        self.water_mark_type = water_mark_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        if self.water_mark_type is not None:
            result['WaterMarkType'] = self.water_mark_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        if m.get('WaterMarkType') is not None:
            self.water_mark_type = m.get('WaterMarkType')
        return self


class GetAudioAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetAudioAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetAudioAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAudioAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAudioAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAudioAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAudioAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioExtractRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioExtractRequest, self).to_map()
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


class GetAudioExtractResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, water_mark_id=None, result_url=None, data_id=None,
                 gmt_modified=None, media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None,
                 finished_time=None, id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.water_mark_id = water_mark_id  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.water_mark_id is not None:
            result['WaterMarkId'] = self.water_mark_id
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('WaterMarkId') is not None:
            self.water_mark_id = m.get('WaterMarkId')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAudioExtractResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetAudioExtractResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAudioExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioExtractResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioExtractResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAudioExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAudioExtractResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAudioExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioTraceRequest(TeaModel):
    def __init__(self, app_name=None, file_uid=None, user_info_list=None):
        self.app_name = app_name  # type: str
        self.file_uid = file_uid  # type: str
        self.user_info_list = user_info_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.file_uid is not None:
            result['FileUid'] = self.file_uid
        if self.user_info_list is not None:
            result['userInfoList'] = self.user_info_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('FileUid') is not None:
            self.file_uid = m.get('FileUid')
        if m.get('userInfoList') is not None:
            self.user_info_list = m.get('userInfoList')
        return self


class GetAudioTraceResponseBodyData(TeaModel):
    def __init__(self, result_url=None, user_info=None):
        self.result_url = result_url  # type: str
        self.user_info = user_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAudioTraceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        return self


class GetAudioTraceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetAudioTraceResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAudioTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioTraceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAudioTraceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAudioTraceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAudioTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocAddRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocAddRequest, self).to_map()
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


class GetDocAddResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, result_url=None, data_id=None, gmt_modified=None,
                 media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None, finished_time=None,
                 id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocAddResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDocAddResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetDocAddResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDocAddResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDocAddResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDocAddResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDocAddResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocAddResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDocAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocAsyncRequest(TeaModel):
    def __init__(self, app_name=None, url_list=None):
        self.app_name = app_name  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class GetDocAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetDocAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetDocAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDocAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDocAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDocAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDocAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDocAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocExtractRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocExtractRequest, self).to_map()
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


class GetDocExtractResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, water_mark_id=None, result_url=None, data_id=None,
                 gmt_modified=None, media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None,
                 finished_time=None, id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.water_mark_id = water_mark_id  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.water_mark_id is not None:
            result['WaterMarkId'] = self.water_mark_id
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('WaterMarkId') is not None:
            self.water_mark_id = m.get('WaterMarkId')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDocExtractResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetDocExtractResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDocExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDocExtractResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDocExtractResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDocExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocExtractResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDocExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageAsyncRequest(TeaModel):
    def __init__(self, app_name=None, url_list=None):
        self.app_name = app_name  # type: long
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class GetImageAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetImageAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetImageAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetImageAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetImageAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageSyncRequest(TeaModel):
    def __init__(self, app_name=None, url_list=None):
        self.app_name = app_name  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class GetImageSyncResponseBodyData(TeaModel):
    def __init__(self, data_id=None, watermark_id=None, meta_file_url=None):
        self.data_id = data_id  # type: str
        self.watermark_id = watermark_id  # type: str
        self.meta_file_url = meta_file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageSyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['dataId'] = self.data_id
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.meta_file_url is not None:
            result['MetaFileUrl'] = self.meta_file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('MetaFileUrl') is not None:
            self.meta_file_url = m.get('MetaFileUrl')
        return self


class GetImageSyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetImageSyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetImageSyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetImageSyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageSyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryTraceFileRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryTraceFileRequest, self).to_map()
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


class GetQueryTraceFileResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, result_url=None, data_id=None, gmt_modified=None,
                 media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None, finished_time=None,
                 id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryTraceFileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetQueryTraceFileResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetQueryTraceFileResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryTraceFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQueryTraceFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetQueryTraceFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryTraceFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryTraceFileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetQueryTraceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAddRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoAddRequest, self).to_map()
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


class GetVideoAddResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, result_url=None, data_id=None, gmt_modified=None,
                 media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None, finished_time=None,
                 id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoAddResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetVideoAddResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetVideoAddResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoAddResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoAddResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoAddResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoAddResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoAddResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAsyncRequest(TeaModel):
    def __init__(self, app_name=None, url_list=None, water_mark_type=None, vm_type=None):
        self.app_name = app_name  # type: str
        self.url_list = url_list  # type: str
        self.water_mark_type = water_mark_type  # type: str
        self.vm_type = vm_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        if self.water_mark_type is not None:
            result['WaterMarkType'] = self.water_mark_type
        if self.vm_type is not None:
            result['VmType'] = self.vm_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        if m.get('WaterMarkType') is not None:
            self.water_mark_type = m.get('WaterMarkType')
        if m.get('VmType') is not None:
            self.vm_type = m.get('VmType')
        return self


class GetVideoAsyncResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, data_id=None):
        self.task_uid = task_uid  # type: str
        self.data_id = data_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetVideoAsyncResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetVideoAsyncResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoAsyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoExtractRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoExtractRequest, self).to_map()
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


class GetVideoExtractResponseBodyData(TeaModel):
    def __init__(self, status=None, source_url=None, water_mark_id=None, result_url=None, data_id=None,
                 gmt_modified=None, media_type=None, msg=None, task_uid=None, app_id=None, gmt_create=None, opt_type=None,
                 finished_time=None, id=None):
        self.status = status  # type: str
        self.source_url = source_url  # type: str
        self.water_mark_id = water_mark_id  # type: str
        self.result_url = result_url  # type: str
        self.data_id = data_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.media_type = media_type  # type: str
        self.msg = msg  # type: str
        self.task_uid = task_uid  # type: str
        self.app_id = app_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.opt_type = opt_type  # type: str
        self.finished_time = finished_time  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.water_mark_id is not None:
            result['WaterMarkId'] = self.water_mark_id
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('WaterMarkId') is not None:
            self.water_mark_id = m.get('WaterMarkId')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetVideoExtractResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetVideoExtractResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoExtractResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoExtractResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoExtractResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTraceRequest(TeaModel):
    def __init__(self, app_name=None, file_uid=None, user_info_list=None, file_type=None):
        self.app_name = app_name  # type: str
        self.file_uid = file_uid  # type: str
        self.user_info_list = user_info_list  # type: str
        self.file_type = file_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.file_uid is not None:
            result['FileUid'] = self.file_uid
        if self.user_info_list is not None:
            result['userInfoList'] = self.user_info_list
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('FileUid') is not None:
            self.file_uid = m.get('FileUid')
        if m.get('userInfoList') is not None:
            self.user_info_list = m.get('userInfoList')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GetVideoTraceResponseBodyData(TeaModel):
    def __init__(self, task_uid=None, result_url=None, user_info=None, file_uid=None):
        self.task_uid = task_uid  # type: str
        self.result_url = result_url  # type: str
        self.user_info = user_info  # type: str
        self.file_uid = file_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTraceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        if self.file_uid is not None:
            result['FileUid'] = self.file_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        if m.get('FileUid') is not None:
            self.file_uid = m.get('FileUid')
        return self


class GetVideoTraceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetVideoTraceResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoTraceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoTraceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoTraceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


