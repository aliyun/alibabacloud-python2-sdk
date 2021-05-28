# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeAppsRequest(TeaModel):
    def __init__(self, app_id=None, app_status=None, page_num=None, page_size=None):
        # 白板应用唯一标识符，默认查询所有应用ID
        self.app_id = app_id  # type: str
        # 白板应用状态，默认查询所有状态。（取值：1:启用，2:停用）
        self.app_status = app_status  # type: long
        # 第几页，默认查询第1页。
        self.page_num = page_num  # type: long
        # 每页显示个数，默认为10。
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAppsResponseBodyResultAppList(TeaModel):
    def __init__(self, app_id=None, app_name=None, status=None, callback_url=None, domain_names=None,
                 create_time=None, callback_type=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板应用名
        self.app_name = app_name  # type: str
        # 白板应用状态（取值：1:启用，2:停用）
        self.status = status  # type: long
        # 白板应用回调地址URL
        self.callback_url = callback_url  # type: str
        # 合法域名列表，使用英文逗号(,)分隔
        self.domain_names = domain_names  # type: str
        # 白板应用创建时间
        self.create_time = create_time  # type: str
        # 白板应用回调类型
        self.callback_type = callback_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsResponseBodyResultAppList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.status is not None:
            result['Status'] = self.status
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        return self


class DescribeAppsResponseBodyResult(TeaModel):
    def __init__(self, total_num=None, total_page=None, app_list=None):
        self.total_num = total_num  # type: long
        self.total_page = total_page  # type: long
        # App信息列表
        self.app_list = app_list  # type: list[DescribeAppsResponseBodyResultAppList]

    def validate(self):
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = DescribeAppsResponseBodyResultAppList()
                self.app_list.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: DescribeAppsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = DescribeAppsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseWhiteBoardRecordingRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, doc_key=None, record_id=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 结束白板录制的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 白板录制Session的唯一标识
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseWhiteBoardRecordingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class PauseWhiteBoardRecordingResponseBodyResult(TeaModel):
    def __init__(self, pause_time=None):
        # 录制结束的UNIX时间戳
        self.pause_time = pause_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseWhiteBoardRecordingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')
        return self


class PauseWhiteBoardRecordingResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: PauseWhiteBoardRecordingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(PauseWhiteBoardRecordingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = PauseWhiteBoardRecordingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PauseWhiteBoardRecordingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PauseWhiteBoardRecordingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PauseWhiteBoardRecordingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PauseWhiteBoardRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppCallbackUrlRequest(TeaModel):
    def __init__(self, app_id=None, app_callback_url=None, app_callback_auth_key=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板应用回调地址URL
        self.app_callback_url = app_callback_url  # type: str
        # 白板应用回调鉴权码，由8~20位大小写字母、数字或下划线组成
        self.app_callback_auth_key = app_callback_auth_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppCallbackUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_callback_url is not None:
            result['AppCallbackUrl'] = self.app_callback_url
        if self.app_callback_auth_key is not None:
            result['AppCallbackAuthKey'] = self.app_callback_auth_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppCallbackUrl') is not None:
            self.app_callback_url = m.get('AppCallbackUrl')
        if m.get('AppCallbackAuthKey') is not None:
            self.app_callback_auth_key = m.get('AppCallbackAuthKey')
        return self


class SetAppCallbackUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppCallbackUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppCallbackUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAppCallbackUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAppCallbackUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppCallbackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartWhiteBoardRecordingRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, doc_key=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 启动白板录制的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartWhiteBoardRecordingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        return self


class StartWhiteBoardRecordingResponseBodyResult(TeaModel):
    def __init__(self, record_id=None, start_time=None):
        # 白板录制Session的唯一标识
        self.record_id = record_id  # type: str
        # 录制开始的UNIX时间戳
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartWhiteBoardRecordingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StartWhiteBoardRecordingResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: StartWhiteBoardRecordingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(StartWhiteBoardRecordingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = StartWhiteBoardRecordingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class StartWhiteBoardRecordingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartWhiteBoardRecordingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartWhiteBoardRecordingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartWhiteBoardRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppNameRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板应用名，由不超过32位的中文、英文、数字或下划线组成
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class SetAppNameResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAppNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAppNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhiteBoardsRequest(TeaModel):
    def __init__(self, app_id=None, doc_status=None, page_num=None, page_size=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板文档状态，默认查询所有状态。（取值：1:启用，2:停用）
        self.doc_status = doc_status  # type: long
        # 第几页，默认查询第1页
        self.page_num = page_num  # type: long
        # 每页显示个数，默认为10
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteBoardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.doc_status is not None:
            result['DocStatus'] = self.doc_status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('DocStatus') is not None:
            self.doc_status = m.get('DocStatus')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWhiteBoardsResponseBodyResultDocList(TeaModel):
    def __init__(self, app_id=None, doc_key=None, status=None, create_user_id=None, create_time=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 文档状态（取值：1:启用，2:停用）
        self.status = status  # type: long
        # 创建白板的用户ID
        self.create_user_id = create_user_id  # type: str
        # 白板应用创建时间
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteBoardsResponseBodyResultDocList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.status is not None:
            result['Status'] = self.status
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class DescribeWhiteBoardsResponseBodyResult(TeaModel):
    def __init__(self, total_num=None, total_page=None, doc_list=None):
        self.total_num = total_num  # type: long
        self.total_page = total_page  # type: long
        # App信息列表
        self.doc_list = doc_list  # type: list[DescribeWhiteBoardsResponseBodyResultDocList]

    def validate(self):
        if self.doc_list:
            for k in self.doc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhiteBoardsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['DocList'] = []
        if self.doc_list is not None:
            for k in self.doc_list:
                result['DocList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.doc_list = []
        if m.get('DocList') is not None:
            for k in m.get('DocList'):
                temp_model = DescribeWhiteBoardsResponseBodyResultDocList()
                self.doc_list.append(temp_model.from_map(k))
        return self


class DescribeWhiteBoardsResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: DescribeWhiteBoardsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeWhiteBoardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = DescribeWhiteBoardsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeWhiteBoardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeWhiteBoardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWhiteBoardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWhiteBoardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeWhiteBoardRecordingRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, doc_key=None, record_id=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 结束白板录制的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 白板录制Session的唯一标识
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeWhiteBoardRecordingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResumeWhiteBoardRecordingResponseBodyResult(TeaModel):
    def __init__(self, resume_time=None):
        # 录制结束的UNIX时间戳
        self.resume_time = resume_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeWhiteBoardRecordingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        return self


class ResumeWhiteBoardRecordingResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: ResumeWhiteBoardRecordingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ResumeWhiteBoardRecordingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = ResumeWhiteBoardRecordingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ResumeWhiteBoardRecordingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeWhiteBoardRecordingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeWhiteBoardRecordingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeWhiteBoardRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppDomainNamesRequest(TeaModel):
    def __init__(self, app_id=None, app_domain_names=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 所有会使用到白板应用的客户网站域名，多个使用英文逗号(,)分隔，最多传10个
        self.app_domain_names = app_domain_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppDomainNamesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_domain_names is not None:
            result['AppDomainNames'] = self.app_domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppDomainNames') is not None:
            self.app_domain_names = m.get('AppDomainNames')
        return self


class SetAppDomainNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppDomainNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppDomainNamesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAppDomainNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAppDomainNamesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenWhiteBoardRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, doc_key=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 打开白板的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenWhiteBoardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        return self


class OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo(TeaModel):
    def __init__(self, avatar_url=None, nick=None, nick_pinyin=None, user_id=None):
        # 用户头像的URL
        self.avatar_url = avatar_url  # type: str
        # 用户昵称
        self.nick = nick  # type: str
        # 用户的拼音昵称
        self.nick_pinyin = nick_pinyin  # type: str
        # 打开白板的用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.nick_pinyin is not None:
            result['NickPinyin'] = self.nick_pinyin
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('NickPinyin') is not None:
            self.nick_pinyin = m.get('NickPinyin')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class OpenWhiteBoardResponseBodyResultDocumentAccessInfo(TeaModel):
    def __init__(self, access_token=None, collab_host=None, permission=None, user_info=None, ws_domain=None):
        # 连接签名
        self.access_token = access_token  # type: str
        # 白板长连接地址
        self.collab_host = collab_host  # type: str
        # 权限码，取值：0:无权限，1:只读，2:读写
        self.permission = permission  # type: long
        # 用户信息
        self.user_info = user_info  # type: OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo
        # 新协议长连接服务域名
        self.ws_domain = ws_domain  # type: str

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(OpenWhiteBoardResponseBodyResultDocumentAccessInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.collab_host is not None:
            result['CollabHost'] = self.collab_host
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.ws_domain is not None:
            result['WsDomain'] = self.ws_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CollabHost') is not None:
            self.collab_host = m.get('CollabHost')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('UserInfo') is not None:
            temp_model = OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('WsDomain') is not None:
            self.ws_domain = m.get('WsDomain')
        return self


class OpenWhiteBoardResponseBodyResult(TeaModel):
    def __init__(self, document_access_info=None):
        # 白板连接信息
        self.document_access_info = document_access_info  # type: OpenWhiteBoardResponseBodyResultDocumentAccessInfo

    def validate(self):
        if self.document_access_info:
            self.document_access_info.validate()

    def to_map(self):
        _map = super(OpenWhiteBoardResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_access_info is not None:
            result['DocumentAccessInfo'] = self.document_access_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocumentAccessInfo') is not None:
            temp_model = OpenWhiteBoardResponseBodyResultDocumentAccessInfo()
            self.document_access_info = temp_model.from_map(m['DocumentAccessInfo'])
        return self


class OpenWhiteBoardResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: OpenWhiteBoardResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(OpenWhiteBoardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = OpenWhiteBoardResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class OpenWhiteBoardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenWhiteBoardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenWhiteBoardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenWhiteBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshUsersPermissionsRequest(TeaModel):
    def __init__(self, user_ids=None, doc_key=None, app_id=None):
        # 需要刷新权限的用户ID，多个用英文逗号（,）分隔，最多30个，每个ID由纯数字组成
        self.user_ids = user_ids  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshUsersPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class RefreshUsersPermissionsResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshUsersPermissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RefreshUsersPermissionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshUsersPermissionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshUsersPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshUsersPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppCallbackTypeRequest(TeaModel):
    def __init__(self, app_id=None, app_callback_type=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板应用回调类型
        self.app_callback_type = app_callback_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppCallbackTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_callback_type is not None:
            result['AppCallbackType'] = self.app_callback_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppCallbackType') is not None:
            self.app_callback_type = m.get('AppCallbackType')
        return self


class SetAppCallbackTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppCallbackTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppCallbackTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAppCallbackTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAppCallbackTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppCallbackTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None):
        # 白板应用名，由不超过32位的中文、英文、数字或下划线组成
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(self, app_id=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: CreateAppResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUsersPermissionsRequest(TeaModel):
    def __init__(self, user_ids=None, doc_key=None, app_id=None, permission_type=None):
        # 需要设置权限的用户ID，多个用英文逗号（,）分隔，最多30个，每个ID由纯数字组成
        self.user_ids = user_ids  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 用户白板权限类型，可选值：ban/read/edit
        self.permission_type = permission_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUsersPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        return self


class SetUsersPermissionsResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUsersPermissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetUsersPermissionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetUsersPermissionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUsersPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetUsersPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWhiteBoardRequest(TeaModel):
    def __init__(self, user_id=None, app_id=None):
        # 创建白板的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhiteBoardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class CreateWhiteBoardResponseBodyResult(TeaModel):
    def __init__(self, doc_key=None):
        # 文档唯一标识符，由大小写字母和数字组成
        self.doc_key = doc_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhiteBoardResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        return self


class CreateWhiteBoardResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: CreateWhiteBoardResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateWhiteBoardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = CreateWhiteBoardResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateWhiteBoardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWhiteBoardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWhiteBoardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWhiteBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppStatusRequest(TeaModel):
    def __init__(self, app_id=None, app_status=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 白板应用状态（取值：1:启用，2:停用）
        self.app_status = app_status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        return self


class SetAppStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAppStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAppStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAppStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopWhiteBoardRecordingRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, doc_key=None, record_id=None):
        # 白板应用唯一标识符
        self.app_id = app_id  # type: str
        # 结束白板录制的用户ID（客户业务用户），由1~32位大小写字母、数字、下划线、短划线（-）组成
        self.user_id = user_id  # type: str
        # 白板文档唯一标识符
        self.doc_key = doc_key  # type: str
        # 白板录制Session的唯一标识
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopWhiteBoardRecordingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class StopWhiteBoardRecordingResponseBodyResult(TeaModel):
    def __init__(self, stop_time=None):
        # 录制结束的UNIX时间戳
        self.stop_time = stop_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopWhiteBoardRecordingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class StopWhiteBoardRecordingResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求结果
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 返回结果体
        self.result = result  # type: StopWhiteBoardRecordingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(StopWhiteBoardRecordingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = StopWhiteBoardRecordingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class StopWhiteBoardRecordingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopWhiteBoardRecordingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopWhiteBoardRecordingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopWhiteBoardRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


