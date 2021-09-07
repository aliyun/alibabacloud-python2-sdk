# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ListAppInfosRequestRequestParams(TeaModel):
    def __init__(self, type=None, keyword=None, page_size=None, page_number=None):
        # 关键字类型，包含appName、appId两类
        self.type = type  # type: str
        # 关键字
        self.keyword = keyword  # type: str
        # 分页大小，大于0的任意数
        self.page_size = page_size  # type: int
        # 页码，从1开始
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInfosRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListAppInfosRequest(TeaModel):
    def __init__(self, request_params=None):
        self.request_params = request_params  # type: ListAppInfosRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ListAppInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            temp_model = ListAppInfosRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListAppInfosShrinkRequest(TeaModel):
    def __init__(self, request_params_shrink=None):
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInfosShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListAppInfosResponseBodyResultAppInfos(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, app_status=None, prod_version=None,
                 instance_id=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 应用名
        self.app_name = app_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 应用状态
        self.app_status = app_status  # type: int
        # 产品版本
        self.prod_version = prod_version  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInfosResponseBodyResultAppInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.prod_version is not None:
            result['ProdVersion'] = self.prod_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('ProdVersion') is not None:
            self.prod_version = m.get('ProdVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAppInfosResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, app_infos=None):
        # 总数，用于分页
        self.total_count = total_count  # type: int
        # 应用信息列表
        self.app_infos = app_infos  # type: list[ListAppInfosResponseBodyResultAppInfos]

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInfosResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = ListAppInfosResponseBodyResultAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        return self


class ListAppInfosResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, code=None, success=None, result=None):
        # desc
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool
        # result
        self.result = result  # type: ListAppInfosResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAppInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = ListAppInfosResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAppInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInfosResponse, self).to_map()
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
            temp_model = ListAppInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_cid=None, keys=None):
        # 用户id
        self.app_uid = app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSingleChatExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveSingleChatExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        self.app_id = app_id  # type: str
        # 单聊移除拓展字段请求实体
        self.request_params = request_params  # type: RemoveSingleChatExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveSingleChatExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveSingleChatExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveSingleChatExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        self.app_id = app_id  # type: str
        # 单聊移除拓展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSingleChatExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveSingleChatExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSingleChatExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveSingleChatExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSingleChatExtensionByKeysResponse, self).to_map()
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
            temp_model = RemoveSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportMessageRequestRequestParamsMessages(TeaModel):
    def __init__(self, uuid=None, app_cid=None, conversation_type=None, sender_id=None, receiver_ids=None,
                 content_type=None, content=None, create_time=None, extensions=None):
        # 唯一标识，用于重入
        self.uuid = uuid  # type: str
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 会话类型1 单聊 2 群聊
        self.conversation_type = conversation_type  # type: long
        # 发送者ID
        self.sender_id = sender_id  # type: str
        # 接受者列表, 群聊如果列表为空者全员接收
        self.receiver_ids = receiver_ids  # type: list[str]
        # 消息类型
        self.content_type = content_type  # type: long
        # 消息内容
        self.content = content  # type: str
        # 消息发送时间戳
        self.create_time = create_time  # type: long
        # 自定义信息
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportMessageRequestRequestParamsMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ImportMessageRequestRequestParams(TeaModel):
    def __init__(self, messages=None):
        self.messages = messages  # type: list[ImportMessageRequestRequestParamsMessages]

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportMessageRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ImportMessageRequestRequestParamsMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class ImportMessageRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: ImportMessageRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ImportMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportMessageShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportMessageResponseBodyResult(TeaModel):
    def __init__(self, import_message_result=None):
        self.import_message_result = import_message_result  # type: dict[str, ResultImportMessageResultValue]

    def validate(self):
        if self.import_message_result:
            for v in self.import_message_result.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ImportMessageResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportMessageResult'] = {}
        if self.import_message_result is not None:
            for k, v in self.import_message_result.items():
                result['ImportMessageResult'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.import_message_result = {}
        if m.get('ImportMessageResult') is not None:
            for k, v in m.get('ImportMessageResult').items():
                temp_model = ResultImportMessageResultValue()
                self.import_message_result[k] = temp_model.from_map(v)
        return self


class ImportMessageResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: ImportMessageResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ImportMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ImportMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportMessageResponse, self).to_map()
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
            temp_model = ImportMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, operator_app_uid=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 操作者uid
        self.operator_app_uid = operator_app_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SilenceAllGroupMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class SilenceAllGroupMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: SilenceAllGroupMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SilenceAllGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SilenceAllGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SilenceAllGroupMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SilenceAllGroupMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SilenceAllGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SilenceAllGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SilenceAllGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SilenceAllGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SilenceAllGroupMembersResponse, self).to_map()
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
            temp_model = SilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomMessagesRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, sub_type=None, page_number=None, page_size=None):
        # 应用的appKey。
        self.domain = domain  # type: str
        # 房间ID，由调用CreateRoom时返回。
        self.room_id = room_id  # type: str
        # 要查询的消息的类型,请传递100000以上的整数，如果不传，则默认拉取全部类型的消息。
        self.sub_type = sub_type  # type: int
        # 分页查询时的页数，从1开始，每次分页查询时加1。
        self.page_number = page_number  # type: int
        # 分页查询时的请求大小，要求大于0，且最大不得超过100。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomMessagesRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRoomMessagesRequest(TeaModel):
    def __init__(self, request=None):
        # 请求参数的结构体。
        self.request = request  # type: ListRoomMessagesRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(ListRoomMessagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = ListRoomMessagesRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class ListRoomMessagesResponseBodyResultRoomMessageList(TeaModel):
    def __init__(self, room_id=None, message_id=None, sub_type=None, sender_id=None, send_time_millis=None,
                 body=None):
        # 房间ID。
        self.room_id = room_id  # type: str
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
        self.message_id = message_id  # type: str
        # 消息的类型。
        self.sub_type = sub_type  # type: int
        # 消息的发送者ID。
        self.sender_id = sender_id  # type: str
        # 消息的发送时间,毫秒unix时间戳。
        self.send_time_millis = send_time_millis  # type: long
        # 消息体。
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomMessagesResponseBodyResultRoomMessageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.send_time_millis is not None:
            result['SendTimeMillis'] = self.send_time_millis
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SendTimeMillis') is not None:
            self.send_time_millis = m.get('SendTimeMillis')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class ListRoomMessagesResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, room_message_list=None, has_more=None):
        # 互动消息的总数。
        self.total_count = total_count  # type: int
        # 房间的互动消息列表，按照发送时间戳由大到小排序。
        self.room_message_list = room_message_list  # type: list[ListRoomMessagesResponseBodyResultRoomMessageList]
        # 是否还有下一页查询的数据。
        self.has_more = has_more  # type: bool

    def validate(self):
        if self.room_message_list:
            for k in self.room_message_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomMessagesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['RoomMessageList'] = []
        if self.room_message_list is not None:
            for k in self.room_message_list:
                result['RoomMessageList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.room_message_list = []
        if m.get('RoomMessageList') is not None:
            for k in m.get('RoomMessageList'):
                temp_model = ListRoomMessagesResponseBodyResultRoomMessageList()
                self.room_message_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        return self


class ListRoomMessagesResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_message=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 请求是否成功。
        self.response_success = response_success  # type: bool
        # 错误码，请求异常时返回。
        self.error_code = error_code  # type: str
        # 错误信息，请求异常时返回。
        self.error_message = error_message  # type: str
        # 请求的返回结果。
        self.result = result  # type: ListRoomMessagesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListRoomMessagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            temp_model = ListRoomMessagesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomMessagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRoomMessagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRoomMessagesResponse, self).to_map()
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
            temp_model = ListRoomMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, extensions=None):
        self.app_cid = app_cid  # type: str
        # 扩展字段
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetGroupExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群聊设置扩展字段请求实体
        self.request_params = request_params  # type: SetGroupExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetGroupExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetGroupExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群聊设置扩展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetGroupExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetGroupExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGroupExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGroupExtensionByKeysResponse, self).to_map()
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
            temp_model = SetGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupMemberExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, app_uid=None, keys=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 用户ID
        self.app_uid = app_uid  # type: str
        # 扩展信息中需要删除的key列表
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMemberExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveGroupMemberExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 删除群成员扩展信息的请求体
        self.request_params = request_params  # type: RemoveGroupMemberExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveGroupMemberExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupMemberExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupMemberExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 删除群成员扩展信息的请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMemberExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupMemberExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMemberExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupMemberExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveGroupMemberExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveGroupMemberExtensionByKeysResponse, self).to_map()
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
            temp_model = RemoveGroupMemberExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, members=None, silence_duration=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 群会话id
        self.app_cid = app_cid  # type: str
        # 禁言用户列表
        self.members = members  # type: list[str]
        # 禁言时长
        self.silence_duration = silence_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceBlacklistRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class AddGroupSilenceBlacklistRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params = request_params  # type: AddGroupSilenceBlacklistRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(AddGroupSilenceBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupSilenceBlacklistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupSilenceBlacklistShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceBlacklistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupSilenceBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceBlacklistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupSilenceBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGroupSilenceBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGroupSilenceBlacklistResponse, self).to_map()
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
            temp_model = AddGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, members=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 群会话id
        self.app_cid = app_cid  # type: str
        # 禁言用户列表
        self.members = members  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceWhitelistRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class RemoveGroupSilenceWhitelistRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params = request_params  # type: RemoveGroupSilenceWhitelistRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveGroupSilenceWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupSilenceWhitelistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupSilenceWhitelistShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceWhitelistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupSilenceWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupSilenceWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveGroupSilenceWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveGroupSilenceWhitelistResponse, self).to_map()
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
            temp_model = RemoveGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetailReportStatisticsRequestRequestParams(TeaModel):
    def __init__(self, start_time=None, end_time=None, report_statistics_type=None):
        # 开始时间，utc
        self.start_time = start_time  # type: str
        # 结束时间，utc
        self.end_time = end_time  # type: str
        # 报表类型  user、groupChat、message
        self.report_statistics_type = report_statistics_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDetailReportStatisticsRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_statistics_type is not None:
            result['ReportStatisticsType'] = self.report_statistics_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportStatisticsType') is not None:
            self.report_statistics_type = m.get('ReportStatisticsType')
        return self


class ListDetailReportStatisticsRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params = request_params  # type: ListDetailReportStatisticsRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ListDetailReportStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ListDetailReportStatisticsRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListDetailReportStatisticsShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDetailReportStatisticsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListDetailReportStatisticsResponseBodyResult(TeaModel):
    def __init__(self, data=None):
        # 数据
        self.data = data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDetailReportStatisticsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListDetailReportStatisticsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, code=None, success=None, result=None):
        # desc
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool
        # result
        self.result = result  # type: ListDetailReportStatisticsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListDetailReportStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = ListDetailReportStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDetailReportStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDetailReportStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDetailReportStatisticsResponse, self).to_map()
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
            temp_model = ListDetailReportStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_cid=None, extensions=None):
        # 用户id
        self.app_uid = app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str
        # 拓展字段
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserConversationExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetUserConversationExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        self.app_id = app_id  # type: str
        # 设置用户拓展字段请求实体
        self.request_params = request_params  # type: SetUserConversationExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetUserConversationExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetUserConversationExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetUserConversationExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        self.app_id = app_id  # type: str
        # 设置用户拓展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserConversationExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetUserConversationExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserConversationExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetUserConversationExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserConversationExtensionByKeysResponse, self).to_map()
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
            temp_model = SetUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupByIdRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None):
        # 群会话ID
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupByIdRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class GetGroupByIdRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # APP ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 群会话信息获取的请求体
        self.request_params = request_params  # type: GetGroupByIdRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetGroupByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetGroupByIdRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetGroupByIdShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # APP ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 群会话信息获取的请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupByIdShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetGroupByIdResponseBodyResult(TeaModel):
    def __init__(self, app_cid=None, owner_app_uid=None, icon_media_id=None, title=None, member_count=None,
                 member_limit=None, extensions=None, ceate_time=None):
        # 群会话ID
        self.app_cid = app_cid  # type: str
        # 群主ID
        self.owner_app_uid = owner_app_uid  # type: str
        # 群图像
        self.icon_media_id = icon_media_id  # type: str
        # 群名称
        self.title = title  # type: str
        # 当前群人数
        self.member_count = member_count  # type: int
        # 群人数上限
        self.member_limit = member_limit  # type: int
        # 群扩展信息
        self.extensions = extensions  # type: dict[str, str]
        # 群创建时间
        self.ceate_time = ceate_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupByIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.owner_app_uid is not None:
            result['OwnerAppUid'] = self.owner_app_uid
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.title is not None:
            result['Title'] = self.title
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.member_limit is not None:
            result['MemberLimit'] = self.member_limit
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.ceate_time is not None:
            result['CeateTime'] = self.ceate_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OwnerAppUid') is not None:
            self.owner_app_uid = m.get('OwnerAppUid')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('MemberLimit') is not None:
            self.member_limit = m.get('MemberLimit')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('CeateTime') is not None:
            self.ceate_time = m.get('CeateTime')
        return self


class GetGroupByIdResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 群信息获取的返回结果
        self.result = result  # type: GetGroupByIdResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetGroupByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetGroupByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGroupByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupByIdResponse, self).to_map()
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
            temp_model = GetGroupByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTenantStatusRequestRequest(TeaModel):
    def __init__(self, domain=None, status=None):
        # 应用appKey
        self.domain = domain  # type: str
        # 应用状态
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTenantStatusRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateTenantStatusRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: UpdateTenantStatusRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(UpdateTenantStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = UpdateTenantStatusRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class UpdateTenantStatusResponseBody(TeaModel):
    def __init__(self, response_success=None, error_code=None, error_msg=None, result=None, request_id=None):
        # Id of the request
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 是否更新成功
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTenantStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTenantStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTenantStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTenantStatusResponse, self).to_map()
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
            temp_model = UpdateTenantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommonConfigRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用id
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommonConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetCommonConfigResponseBodyResultCommonConfigLoginConfig(TeaModel):
    def __init__(self, login_type=None):
        # 登录类型
        self.login_type = login_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommonConfigResponseBodyResultCommonConfigLoginConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        return self


class GetCommonConfigResponseBodyResultCommonConfigAppConfigs(TeaModel):
    def __init__(self, app_key=None, platform=None):
        # appKey
        self.app_key = app_key  # type: str
        # 平台
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommonConfigResponseBodyResultCommonConfigAppConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetCommonConfigResponseBodyResultCommonConfig(TeaModel):
    def __init__(self, login_config=None, app_configs=None):
        # 登录配置
        self.login_config = login_config  # type: GetCommonConfigResponseBodyResultCommonConfigLoginConfig
        # app配置
        self.app_configs = app_configs  # type: list[GetCommonConfigResponseBodyResultCommonConfigAppConfigs]

    def validate(self):
        if self.login_config:
            self.login_config.validate()
        if self.app_configs:
            for k in self.app_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCommonConfigResponseBodyResultCommonConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_config is not None:
            result['LoginConfig'] = self.login_config.to_map()
        result['AppConfigs'] = []
        if self.app_configs is not None:
            for k in self.app_configs:
                result['AppConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginConfig') is not None:
            temp_model = GetCommonConfigResponseBodyResultCommonConfigLoginConfig()
            self.login_config = temp_model.from_map(m['LoginConfig'])
        self.app_configs = []
        if m.get('AppConfigs') is not None:
            for k in m.get('AppConfigs'):
                temp_model = GetCommonConfigResponseBodyResultCommonConfigAppConfigs()
                self.app_configs.append(temp_model.from_map(k))
        return self


class GetCommonConfigResponseBodyResult(TeaModel):
    def __init__(self, common_config=None):
        # 通用配置
        self.common_config = common_config  # type: GetCommonConfigResponseBodyResultCommonConfig

    def validate(self):
        if self.common_config:
            self.common_config.validate()

    def to_map(self):
        _map = super(GetCommonConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_config is not None:
            result['CommonConfig'] = self.common_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonConfig') is not None:
            temp_model = GetCommonConfigResponseBodyResultCommonConfig()
            self.common_config = temp_model.from_map(m['CommonConfig'])
        return self


class GetCommonConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 返回值
        self.result = result  # type: GetCommonConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCommonConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetCommonConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetCommonConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCommonConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCommonConfigResponse, self).to_map()
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
            temp_model = GetCommonConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestRequestParamsOptionsReceiveScopeOption(TeaModel):
    def __init__(self, receiver_ids=None, exclude_receiver_ids=None, receive_scope=None):
        # 接受者列表
        self.receiver_ids = receiver_ids  # type: list[str]
        # 不接收者列表
        self.exclude_receiver_ids = exclude_receiver_ids  # type: list[str]
        # 消息获取控制。0: 会话内除指定ExcludeReceivers均可获取；1: 会话内仅指定ReceiverIds可获取
        self.receive_scope = receive_scope  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequestRequestParamsOptionsReceiveScopeOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        if self.exclude_receiver_ids is not None:
            result['ExcludeReceiverIds'] = self.exclude_receiver_ids
        if self.receive_scope is not None:
            result['ReceiveScope'] = self.receive_scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        if m.get('ExcludeReceiverIds') is not None:
            self.exclude_receiver_ids = m.get('ExcludeReceiverIds')
        if m.get('ReceiveScope') is not None:
            self.receive_scope = m.get('ReceiveScope')
        return self


class SendMessageRequestRequestParamsOptionsSingleChatCreateRequest(TeaModel):
    def __init__(self, app_cid=None, app_uids=None, extensions=None, user_conversation=None):
        # 单聊会话ID
        self.app_cid = app_cid  # type: str
        # 用户ID列表
        self.app_uids = app_uids  # type: list[str]
        # 扩展信息
        self.extensions = extensions  # type: dict[str, str]
        # 用户会话视图信息
        self.user_conversation = user_conversation  # type: dict[str, RequestParamsOptionsSingleChatCreateRequestUserConversationValue]

    def validate(self):
        if self.user_conversation:
            for v in self.user_conversation.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SendMessageRequestRequestParamsOptionsSingleChatCreateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        result['UserConversation'] = {}
        if self.user_conversation is not None:
            for k, v in self.user_conversation.items():
                result['UserConversation'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        self.user_conversation = {}
        if m.get('UserConversation') is not None:
            for k, v in m.get('UserConversation').items():
                temp_model = RequestParamsOptionsSingleChatCreateRequestUserConversationValue()
                self.user_conversation[k] = temp_model.from_map(v)
        return self


class SendMessageRequestRequestParamsOptions(TeaModel):
    def __init__(self, red_point_policy=None, receive_scope_option=None, single_chat_create_request=None):
        # 未读消息小红点控制。0:增加小红点; 1:不增加小红点
        self.red_point_policy = red_point_policy  # type: int
        # 接受相关设置
        self.receive_scope_option = receive_scope_option  # type: SendMessageRequestRequestParamsOptionsReceiveScopeOption
        # 单聊会话不存在时新建自定义单聊请求体
        self.single_chat_create_request = single_chat_create_request  # type: SendMessageRequestRequestParamsOptionsSingleChatCreateRequest

    def validate(self):
        if self.receive_scope_option:
            self.receive_scope_option.validate()
        if self.single_chat_create_request:
            self.single_chat_create_request.validate()

    def to_map(self):
        _map = super(SendMessageRequestRequestParamsOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.red_point_policy is not None:
            result['RedPointPolicy'] = self.red_point_policy
        if self.receive_scope_option is not None:
            result['ReceiveScopeOption'] = self.receive_scope_option.to_map()
        if self.single_chat_create_request is not None:
            result['SingleChatCreateRequest'] = self.single_chat_create_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RedPointPolicy') is not None:
            self.red_point_policy = m.get('RedPointPolicy')
        if m.get('ReceiveScopeOption') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsReceiveScopeOption()
            self.receive_scope_option = temp_model.from_map(m['ReceiveScopeOption'])
        if m.get('SingleChatCreateRequest') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsSingleChatCreateRequest()
            self.single_chat_create_request = temp_model.from_map(m['SingleChatCreateRequest'])
        return self


class SendMessageRequestRequestParams(TeaModel):
    def __init__(self, uuid=None, app_cid=None, conversation_type=None, sender_id=None, content_type=None,
                 content=None, extensions=None, options=None):
        # 消息UUID
        self.uuid = uuid  # type: str
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 会话类型
        self.conversation_type = conversation_type  # type: int
        # 发送者UID
        self.sender_id = sender_id  # type: str
        # 消息内容类型
        self.content_type = content_type  # type: int
        # 消息内容Json
        self.content = content  # type: str
        # 消息扩展字段
        self.extensions = extensions  # type: dict[str, str]
        # 消息设置
        self.options = options  # type: SendMessageRequestRequestParamsOptions

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super(SendMessageRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.options is not None:
            result['Options'] = self.options.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Options') is not None:
            temp_model = SendMessageRequestRequestParamsOptions()
            self.options = temp_model.from_map(m['Options'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 消息发送请求体
        self.request_params = request_params  # type: SendMessageRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SendMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 消息发送请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SendMessageResponseBodyResult(TeaModel):
    def __init__(self, msg_id=None, create_time=None):
        # 消息ID
        self.msg_id = msg_id  # type: str
        # 消息创建时间戳(毫秒)
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: SendMessageResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = SendMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupMembersRoleRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, operator_app_uid=None, role=None, app_uids=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 操作用户ID。
        self.operator_app_uid = operator_app_uid  # type: str
        # 更新后的成员角色。取值： 2：管理员。 3：普通。 100~127：自定义。 不能为1。
        self.role = role  # type: int
        # 需要更改的uids
        self.app_uids = app_uids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupMembersRoleRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class UpdateGroupMembersRoleRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # App ID。IMPaaS租户的ID。
        self.app_id = app_id  # type: str
        # 更新群成员角色请求体。
        self.request_params = request_params  # type: UpdateGroupMembersRoleRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateGroupMembersRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupMembersRoleRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupMembersRoleShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # App ID。IMPaaS租户的ID。
        self.app_id = app_id  # type: str
        # 更新群成员角色请求体。
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupMembersRoleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupMembersRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 错误码。
        self.code = code  # type: str
        # 错误信息。
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupMembersRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupMembersRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupMembersRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupMembersRoleResponse, self).to_map()
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
            temp_model = UpdateGroupMembersRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelSilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, operator_app_uid=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 操作者uid
        self.operator_app_uid = operator_app_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelSilenceAllGroupMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class CancelSilenceAllGroupMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: CancelSilenceAllGroupMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(CancelSilenceAllGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = CancelSilenceAllGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class CancelSilenceAllGroupMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelSilenceAllGroupMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class CancelSilenceAllGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelSilenceAllGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CancelSilenceAllGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelSilenceAllGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelSilenceAllGroupMembersResponse, self).to_map()
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
            temp_model = CancelSilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupIconRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, operator_app_uid=None, icon_media_id=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 操作者用户ID
        self.operator_app_uid = operator_app_uid  # type: str
        # 群聊头像文件MediaID
        self.icon_media_id = icon_media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupIconRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        return self


class UpdateGroupIconRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: UpdateGroupIconRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateGroupIconRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupIconRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupIconShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupIconShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupIconResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupIconResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupIconResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupIconResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupIconResponse, self).to_map()
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
            temp_model = UpdateGroupIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupMembersRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, app_uids_removed=None):
        self.operator_app_uid = operator_app_uid  # type: str
        self.app_cid = app_cid  # type: str
        self.app_uids_removed = app_uids_removed  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids_removed is not None:
            result['AppUidsRemoved'] = self.app_uids_removed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUidsRemoved') is not None:
            self.app_uids_removed = m.get('AppUidsRemoved')
        return self


class RemoveGroupMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群踢人请求实体
        self.request_params = request_params  # type: RemoveGroupMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群踢人请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveGroupMembersResponse, self).to_map()
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
            temp_model = RemoveGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupAllMembersRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None):
        # 会话ID
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupAllMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ListGroupAllMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 拉取群成员列表的请求体
        self.request_params = request_params  # type: ListGroupAllMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ListGroupAllMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ListGroupAllMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListGroupAllMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 拉取群成员列表的请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupAllMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListGroupAllMembersResponseBodyResultMembers(TeaModel):
    def __init__(self, app_uid=None, role=None, nick=None, join_time=None, extensions=None):
        # 群成员ID
        self.app_uid = app_uid  # type: str
        # 群成员角色
        self.role = role  # type: int
        # 群成员昵称
        self.nick = nick  # type: str
        # 群成员入群时间
        self.join_time = join_time  # type: long
        # 群成员扩展信息
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupAllMembersResponseBodyResultMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ListGroupAllMembersResponseBodyResult(TeaModel):
    def __init__(self, members=None):
        # 群成员列表
        self.members = members  # type: list[ListGroupAllMembersResponseBodyResultMembers]

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupAllMembersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = ListGroupAllMembersResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        return self


class ListGroupAllMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 拉取群成员列表的结果
        self.result = result  # type: ListGroupAllMembersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListGroupAllMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ListGroupAllMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListGroupAllMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupAllMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupAllMembersResponse, self).to_map()
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
            temp_model = ListGroupAllMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMuteSettingRequestRequestParams(TeaModel):
    def __init__(self, app_uids=None):
        # 用户列表
        self.app_uids = app_uids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserMuteSettingRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class GetUserMuteSettingRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: GetUserMuteSettingRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetUserMuteSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetUserMuteSettingRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetUserMuteSettingShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserMuteSettingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetUserMuteSettingResponseBodyResult(TeaModel):
    def __init__(self, user_mute_settings=None):
        self.user_mute_settings = user_mute_settings  # type: dict[str, ResultUserMuteSettingsValue]

    def validate(self):
        if self.user_mute_settings:
            for v in self.user_mute_settings.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(GetUserMuteSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserMuteSettings'] = {}
        if self.user_mute_settings is not None:
            for k, v in self.user_mute_settings.items():
                result['UserMuteSettings'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_mute_settings = {}
        if m.get('UserMuteSettings') is not None:
            for k, v in m.get('UserMuteSettings').items():
                temp_model = ResultUserMuteSettingsValue()
                self.user_mute_settings[k] = temp_model.from_map(v)
        return self


class GetUserMuteSettingResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        # 返回值
        self.result = result  # type: GetUserMuteSettingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetUserMuteSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetUserMuteSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserMuteSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserMuteSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserMuteSettingResponse, self).to_map()
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
            temp_model = GetUserMuteSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomStatisticsRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None):
        # 应用的appKey。
        self.domain = domain  # type: str
        # 房间ID，由调用CreateRoom时返回。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoomStatisticsRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomStatisticsRequest(TeaModel):
    def __init__(self, request=None):
        # 请求参数的结构体。
        self.request = request  # type: GetRoomStatisticsRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(GetRoomStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = GetRoomStatisticsRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class GetRoomStatisticsResponseBodyResult(TeaModel):
    def __init__(self, online_count=None, uv=None, pv=None):
        # 当前房间的在线观众数。
        self.online_count = online_count  # type: int
        # 当前房间的历史用户访问数目（UV）。
        self.uv = uv  # type: int
        # 当前房间的历史访问数目（PV）。
        self.pv = pv  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoomStatisticsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.uv is not None:
            result['UV'] = self.uv
        if self.pv is not None:
            result['PV'] = self.pv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        if m.get('PV') is not None:
            self.pv = m.get('PV')
        return self


class GetRoomStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_message=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 请求是否成功。
        self.response_success = response_success  # type: bool
        # 错误码，请求异常时返回。
        self.error_code = error_code  # type: str
        # 错误信息，请求异常时返回。
        self.error_message = error_message  # type: str
        # 请求的返回结果。
        self.result = result  # type: GetRoomStatisticsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRoomStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            temp_model = GetRoomStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRoomStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRoomStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRoomStatisticsResponse, self).to_map()
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
            temp_model = GetRoomStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupMembersRequestRequestParamsInitMembers(TeaModel):
    def __init__(self, app_uid=None, role=None, nick=None, join_time=None, extensions=None):
        self.app_uid = app_uid  # type: str
        # 1群主，2管理员，3普通
        self.role = role  # type: int
        self.nick = nick  # type: str
        # unix毫秒数
        self.join_time = join_time  # type: long
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupMembersRequestRequestParamsInitMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class AddGroupMembersRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, init_members=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str
        # 初始化成员
        self.init_members = init_members  # type: list[AddGroupMembersRequestRequestParamsInitMembers]

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddGroupMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = AddGroupMembersRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        return self


class AddGroupMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群加人请求实体
        self.request_params = request_params  # type: AddGroupMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(AddGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群加人请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGroupMembersResponse, self).to_map()
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
            temp_model = AddGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupMemberByIdsRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, app_uids=None):
        # 会话id
        self.app_cid = app_cid  # type: str
        # appUid
        self.app_uids = app_uids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupMemberByIdsRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class GetGroupMemberByIdsRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群聊设置扩展字段请求实体
        self.request_params = request_params  # type: GetGroupMemberByIdsRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetGroupMemberByIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetGroupMemberByIdsRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetGroupMemberByIdsShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群聊设置扩展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupMemberByIdsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetGroupMemberByIdsResponseBodyResultMembers(TeaModel):
    def __init__(self, app_uid=None, role=None, nick=None, join_time=None, extensions=None):
        self.app_uid = app_uid  # type: str
        self.role = role  # type: int
        self.nick = nick  # type: str
        self.join_time = join_time  # type: long
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupMemberByIdsResponseBodyResultMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class GetGroupMemberByIdsResponseBodyResult(TeaModel):
    def __init__(self, members=None):
        # 群成员
        self.members = members  # type: list[GetGroupMemberByIdsResponseBodyResultMembers]

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGroupMemberByIdsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = GetGroupMemberByIdsResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        return self


class GetGroupMemberByIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: GetGroupMemberByIdsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetGroupMemberByIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetGroupMemberByIdsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupMemberByIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGroupMemberByIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupMemberByIdsResponse, self).to_map()
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
            temp_model = GetGroupMemberByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, sender_id=None, sub_type=None, body=None):
        # 应用的appKey。
        self.domain = domain  # type: str
        # 房间ID，由调用CreateRoom时返回。
        self.room_id = room_id  # type: str
        # 消息的发送者ID。
        self.sender_id = sender_id  # type: str
        # 消息的类型，由业务自定义，请传递100000以上。
        self.sub_type = sub_type  # type: int
        # 消息体。
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class SendCustomMessageRequest(TeaModel):
    def __init__(self, request=None):
        # 请求参数的结构体。
        self.request = request  # type: SendCustomMessageRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(SendCustomMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = SendCustomMessageRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class SendCustomMessageResponseBodyResult(TeaModel):
    def __init__(self, message_id=None):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
        self.message_id = message_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_message=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 请求是否成功。
        self.response_success = response_success  # type: bool
        # 错误码，请求异常时返回。
        self.error_code = error_code  # type: str
        # 错误信息，请求异常时返回。
        self.error_message = error_message  # type: str
        # 请求的返回结果。
        self.result = result  # type: SendCustomMessageResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendCustomMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCustomMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCustomMessageResponse, self).to_map()
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
            temp_model = SendCustomMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppNameRequestRequestParams(TeaModel):
    def __init__(self, app_name=None):
        # 应用名
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppNameRequestRequestParams, self).to_map()
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


class UpdateAppNameRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params = request_params  # type: UpdateAppNameRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateAppNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateAppNameRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateAppNameShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppNameShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateAppNameResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, code=None, success=None):
        # desc
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAppNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppNameResponse, self).to_map()
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
            temp_model = UpdateAppNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIMConfigRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用名
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIMConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetIMConfigResponseBodyResultImConfigMsgConfig(TeaModel):
    def __init__(self, client_msg_recall_time_interval_minute=None):
        # 消息撤回时间，分钟
        self.client_msg_recall_time_interval_minute = client_msg_recall_time_interval_minute  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIMConfigResponseBodyResultImConfigMsgConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_msg_recall_time_interval_minute is not None:
            result['ClientMsgRecallTimeIntervalMinute'] = self.client_msg_recall_time_interval_minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientMsgRecallTimeIntervalMinute') is not None:
            self.client_msg_recall_time_interval_minute = m.get('ClientMsgRecallTimeIntervalMinute')
        return self


class GetIMConfigResponseBodyResultImConfigCallbackConfig(TeaModel):
    def __init__(self, callback_url=None, signature_key=None, signature_value=None, apis=None, spis=None,
                 events=None):
        # 回调url，支持外部url
        self.callback_url = callback_url  # type: str
        # 加签密钥-key
        self.signature_key = signature_key  # type: str
        # 加签密钥-value
        self.signature_value = signature_value  # type: str
        # 已开通的回调方法Id列表
        self.apis = apis  # type: dict[str, bool]
        # 已开通的回调方法Id列表
        self.spis = spis  # type: dict[str, bool]
        # 已开通的事件输出列表
        self.events = events  # type: dict[str, bool]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIMConfigResponseBodyResultImConfigCallbackConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.apis is not None:
            result['Apis'] = self.apis
        if self.spis is not None:
            result['Spis'] = self.spis
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('Apis') is not None:
            self.apis = m.get('Apis')
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class GetIMConfigResponseBodyResultImConfig(TeaModel):
    def __init__(self, msg_config=None, callback_config=None):
        # 消息配置
        self.msg_config = msg_config  # type: GetIMConfigResponseBodyResultImConfigMsgConfig
        # 回调配置
        self.callback_config = callback_config  # type: GetIMConfigResponseBodyResultImConfigCallbackConfig

    def validate(self):
        if self.msg_config:
            self.msg_config.validate()
        if self.callback_config:
            self.callback_config.validate()

    def to_map(self):
        _map = super(GetIMConfigResponseBodyResultImConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_config is not None:
            result['MsgConfig'] = self.msg_config.to_map()
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfigMsgConfig()
            self.msg_config = temp_model.from_map(m['MsgConfig'])
        if m.get('CallbackConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfigCallbackConfig()
            self.callback_config = temp_model.from_map(m['CallbackConfig'])
        return self


class GetIMConfigResponseBodyResult(TeaModel):
    def __init__(self, im_config=None):
        # im相关配置
        self.im_config = im_config  # type: GetIMConfigResponseBodyResultImConfig

    def validate(self):
        if self.im_config:
            self.im_config.validate()

    def to_map(self):
        _map = super(GetIMConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_config is not None:
            result['ImConfig'] = self.im_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfig()
            self.im_config = temp_model.from_map(m['ImConfig'])
        return self


class GetIMConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, http_status_code=None, messaage=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 网络错误码
        self.http_status_code = http_status_code  # type: int
        # 错误信息
        self.messaage = messaage  # type: str
        # 返回结果
        self.result = result  # type: GetIMConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetIMConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.messaage is not None:
            result['Messaage'] = self.messaage
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Messaage') is not None:
            self.messaage = m.get('Messaage')
        if m.get('Result') is not None:
            temp_model = GetIMConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetIMConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIMConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIMConfigResponse, self).to_map()
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
            temp_model = GetIMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_cid=None, extensions=None):
        # 用户id
        self.app_uid = app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str
        # 拓展字段
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSingleChatExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetSingleChatExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 创建群聊请求实体
        self.request_params = request_params  # type: SetSingleChatExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetSingleChatExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetSingleChatExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetSingleChatExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 创建群聊请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSingleChatExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetSingleChatExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSingleChatExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetSingleChatExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetSingleChatExtensionByKeysResponse, self).to_map()
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
            temp_model = SetSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppStatusRequestRequestParams(TeaModel):
    def __init__(self, enable=None):
        # 是否开启
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppStatusRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateAppStatusRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params = request_params  # type: UpdateAppStatusRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateAppStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateAppStatusRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateAppStatusShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 请求
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateAppStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool
        # 错误信息
        self.message = message  # type: str
        # 错误码
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateAppStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppStatusResponse, self).to_map()
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
            temp_model = UpdateAppStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MuteUsersRequestRequestParams(TeaModel):
    def __init__(self, app_uids=None, mute_duration=None, mute=None):
        # 需要禁言的用户
        self.app_uids = app_uids  # type: list[str]
        # 单位秒
        self.mute_duration = mute_duration  # type: long
        # true: 禁言, false: 解除禁言
        self.mute = mute  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MuteUsersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration
        if self.mute is not None:
            result['Mute'] = self.mute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        return self


class MuteUsersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: MuteUsersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(MuteUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = MuteUsersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class MuteUsersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MuteUsersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class MuteUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MuteUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class MuteUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MuteUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MuteUsersResponse, self).to_map()
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
            temp_model = MuteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallMessageRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_cid=None, msg_id=None, type=None, operator_type=None, extensions=None):
        # 操作者ID
        self.app_uid = app_uid  # type: str
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 消息ID
        self.msg_id = msg_id  # type: str
        # 撤回显示类型（默认为0)。0：静默撤回，不显示撤回信息，1：普通撤回，显示撤回信息；
        self.type = type  # type: int
        # 操作者类型(默认为0)。0: 发送者; 1: 群主; 2: 系统; 3: 安全合规; 101: 业务自定义类型
        self.operator_type = operator_type  # type: int
        # 业务自定义扩展字段
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecallMessageRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class RecallMessageRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: RecallMessageRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RecallMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RecallMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RecallMessageShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecallMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RecallMessageResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecallMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecallMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecallMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecallMessageResponse, self).to_map()
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
            temp_model = RecallMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, members=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 群会话id
        self.app_cid = app_cid  # type: str
        # 禁言用户列表
        self.members = members  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceWhitelistRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class AddGroupSilenceWhitelistRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params = request_params  # type: AddGroupSilenceWhitelistRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(AddGroupSilenceWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupSilenceWhitelistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupSilenceWhitelistShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceWhitelistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupSilenceWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupSilenceWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupSilenceWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGroupSilenceWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGroupSilenceWhitelistResponse, self).to_map()
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
            temp_model = AddGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupOwnerRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, new_owner_app_uid=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 新群主
        self.new_owner_app_uid = new_owner_app_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupOwnerRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.new_owner_app_uid is not None:
            result['NewOwnerAppUid'] = self.new_owner_app_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('NewOwnerAppUid') is not None:
            self.new_owner_app_uid = m.get('NewOwnerAppUid')
        return self


class SetGroupOwnerRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # App ID，IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 群主转让的请求体
        self.request_params = request_params  # type: SetGroupOwnerRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetGroupOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetGroupOwnerRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupOwnerShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # App ID，IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 群主转让的请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupOwnerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetGroupOwnerResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 错误码。
        self.code = code  # type: str
        # 错误信息。
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetGroupOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGroupOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGroupOwnerResponse, self).to_map()
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
            temp_model = SetGroupOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomUsersRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, page_number=None, page_size=None):
        # 应用的appKey。
        self.domain = domain  # type: str
        # 房间ID，由调用CreateRoom时返回。
        self.room_id = room_id  # type: str
        # 分页查询时的页数，从1开始，每次分页查询时加1。
        self.page_number = page_number  # type: int
        # 分页查询时的请求大小，要求大于0，最大不得超过100。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomUsersRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRoomUsersRequest(TeaModel):
    def __init__(self, request=None):
        # 请求参数的结构体。
        self.request = request  # type: ListRoomUsersRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(ListRoomUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = ListRoomUsersRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class ListRoomUsersResponseBodyResultRoomUserVOList(TeaModel):
    def __init__(self, room_id=None, user_id=None, nick=None):
        # 房间ID。
        self.room_id = room_id  # type: str
        # 用户ID。
        self.user_id = user_id  # type: str
        # 用户的昵称。
        self.nick = nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomUsersResponseBodyResultRoomUserVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.nick is not None:
            result['Nick'] = self.nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        return self


class ListRoomUsersResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, room_user_volist=None, has_more=None):
        # 房间的历史观看成员总数。
        self.total_count = total_count  # type: int
        # 返回的观众列表。
        self.room_user_volist = room_user_volist  # type: list[ListRoomUsersResponseBodyResultRoomUserVOList]
        # 是否还有下一页查询的数据。
        self.has_more = has_more  # type: bool

    def validate(self):
        if self.room_user_volist:
            for k in self.room_user_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['RoomUserVOList'] = []
        if self.room_user_volist is not None:
            for k in self.room_user_volist:
                result['RoomUserVOList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.room_user_volist = []
        if m.get('RoomUserVOList') is not None:
            for k in m.get('RoomUserVOList'):
                temp_model = ListRoomUsersResponseBodyResultRoomUserVOList()
                self.room_user_volist.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        return self


class ListRoomUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_message=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 请求是否成功。
        self.response_success = response_success  # type: bool
        # 错误码，请求异常时返回。
        self.error_code = error_code  # type: str
        # 错误信息，请求异常时返回。
        self.error_message = error_message  # type: str
        # 请求的返回结果。
        self.result = result  # type: ListRoomUsersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListRoomUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            temp_model = ListRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRoomUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRoomUsersResponse, self).to_map()
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
            temp_model = ListRoomUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用id
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool
        # 错误信息
        self.message = message  # type: str
        # 错误码
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResponse, self).to_map()
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None, members=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 群会话id
        self.app_cid = app_cid  # type: str
        # 禁言用户列表
        self.members = members  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceBlacklistRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class RemoveGroupSilenceBlacklistRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言删除黑名单请求体
        self.request_params = request_params  # type: RemoveGroupSilenceBlacklistRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveGroupSilenceBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupSilenceBlacklistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupSilenceBlacklistShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言删除黑名单请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceBlacklistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupSilenceBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupSilenceBlacklistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupSilenceBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveGroupSilenceBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveGroupSilenceBlacklistResponse, self).to_map()
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
            temp_model = RemoveGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, msg_id=None, keys=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 消息ID
        self.msg_id = msg_id  # type: str
        # 需删除的Key
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMessageExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveMessageExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: RemoveMessageExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveMessageExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveMessageExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveMessageExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMessageExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveMessageExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码，成功时为0
        self.code = code  # type: str
        # 错误信息，成功时为0	空
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMessageExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveMessageExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveMessageExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveMessageExtensionByKeysResponse, self).to_map()
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
            temp_model = RemoveMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUploadUrlRequestRequestParams(TeaModel):
    def __init__(self, mime_type=None):
        # 多媒体资源类型(文件后缀名)
        self.mime_type = mime_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUploadUrlRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mime_type is not None:
            result['MimeType'] = self.mime_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')
        return self


class GetMediaUploadUrlRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: GetMediaUploadUrlRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetMediaUploadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMediaUploadUrlRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMediaUploadUrlShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUploadUrlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMediaUploadUrlResponseBodyResult(TeaModel):
    def __init__(self, upload_url=None, media_id=None):
        # 上传Url
        self.upload_url = upload_url  # type: str
        # 多媒体文件ID
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUploadUrlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaUploadUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        # 调用返回值
        self.result = result  # type: GetMediaUploadUrlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMediaUploadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMediaUploadUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaUploadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaUploadUrlResponse, self).to_map()
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
            temp_model = GetMediaUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUrlRequestRequestParams(TeaModel):
    def __init__(self, media_id=None, url_expire_time=None):
        # 多媒体资源ID
        self.media_id = media_id  # type: str
        # URL过期时间(秒，最大86400)
        self.url_expire_time = url_expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUrlRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class GetMediaUrlRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: GetMediaUrlRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetMediaUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMediaUrlRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMediaUrlShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUrlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMediaUrlResponseBodyResult(TeaModel):
    def __init__(self, url=None):
        # 文件Url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaUrlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: GetMediaUrlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMediaUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMediaUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaUrlResponse, self).to_map()
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
            temp_model = GetMediaUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSingleConversationRequestRequestParamsConversation(TeaModel):
    def __init__(self, app_cid=None, app_uids=None, extensions=None, create_time=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 用户ID列表
        self.app_uids = app_uids  # type: list[str]
        # 扩展字段
        self.extensions = extensions  # type: dict[str, str]
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSingleConversationRequestRequestParamsConversation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ImportSingleConversationRequestRequestParams(TeaModel):
    def __init__(self, conversation=None, user_conversations=None):
        # 会话基础信息
        self.conversation = conversation  # type: ImportSingleConversationRequestRequestParamsConversation
        # 用户会话视图
        self.user_conversations = user_conversations  # type: dict[str, RequestParamsUserConversationsValue]

    def validate(self):
        if self.conversation:
            self.conversation.validate()
        if self.user_conversations:
            for v in self.user_conversations.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ImportSingleConversationRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation is not None:
            result['Conversation'] = self.conversation.to_map()
        result['UserConversations'] = {}
        if self.user_conversations is not None:
            for k, v in self.user_conversations.items():
                result['UserConversations'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conversation') is not None:
            temp_model = ImportSingleConversationRequestRequestParamsConversation()
            self.conversation = temp_model.from_map(m['Conversation'])
        self.user_conversations = {}
        if m.get('UserConversations') is not None:
            for k, v in m.get('UserConversations').items():
                temp_model = RequestParamsUserConversationsValue()
                self.user_conversations[k] = temp_model.from_map(v)
        return self


class ImportSingleConversationRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: ImportSingleConversationRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ImportSingleConversationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportSingleConversationRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportSingleConversationShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSingleConversationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportSingleConversationResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSingleConversationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ImportSingleConversationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportSingleConversationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportSingleConversationResponse, self).to_map()
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
            temp_model = ImportSingleConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCallbackConfigRequestRequestParams(TeaModel):
    def __init__(self, callback_url=None, signature_key=None, signature_value=None, apis=None, spis=None,
                 events=None):
        # 回调url
        self.callback_url = callback_url  # type: str
        # 加签密钥-key
        self.signature_key = signature_key  # type: str
        # 加签密钥-value
        self.signature_value = signature_value  # type: str
        # 回调api列表
        self.apis = apis  # type: dict[str, bool]
        # 回调列表
        self.spis = spis  # type: dict[str, bool]
        # 事件输出列表
        self.events = events  # type: dict[str, bool]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCallbackConfigRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.apis is not None:
            result['Apis'] = self.apis
        if self.spis is not None:
            result['Spis'] = self.spis
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('Apis') is not None:
            self.apis = m.get('Apis')
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class UpdateCallbackConfigRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # 应用Id
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: UpdateCallbackConfigRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateCallbackConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateCallbackConfigRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateCallbackConfigShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # 应用Id
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCallbackConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateCallbackConfigResponseBodyResultImConfigMsgConfig(TeaModel):
    def __init__(self, msg_recall_time_interval=None):
        # 消息撤回时间间隔，毫秒
        self.msg_recall_time_interval = msg_recall_time_interval  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCallbackConfigResponseBodyResultImConfigMsgConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_recall_time_interval is not None:
            result['MsgRecallTimeInterval'] = self.msg_recall_time_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgRecallTimeInterval') is not None:
            self.msg_recall_time_interval = m.get('MsgRecallTimeInterval')
        return self


class UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig(TeaModel):
    def __init__(self, backend_url=None, signature_key=None, signature_value=None, api_ids=None):
        # 回调url
        self.backend_url = backend_url  # type: str
        # 加签密钥-key
        self.signature_key = signature_key  # type: str
        # 加签密钥-value
        self.signature_value = signature_value  # type: str
        # 回调方法列表
        self.api_ids = api_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_url is not None:
            result['BackendUrl'] = self.backend_url
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendUrl') is not None:
            self.backend_url = m.get('BackendUrl')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        return self


class UpdateCallbackConfigResponseBodyResultImConfig(TeaModel):
    def __init__(self, msg_config=None, callback_config=None):
        # 消息配置
        self.msg_config = msg_config  # type: UpdateCallbackConfigResponseBodyResultImConfigMsgConfig
        # 回调配置
        self.callback_config = callback_config  # type: UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig

    def validate(self):
        if self.msg_config:
            self.msg_config.validate()
        if self.callback_config:
            self.callback_config.validate()

    def to_map(self):
        _map = super(UpdateCallbackConfigResponseBodyResultImConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_config is not None:
            result['MsgConfig'] = self.msg_config.to_map()
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfigMsgConfig()
            self.msg_config = temp_model.from_map(m['MsgConfig'])
        if m.get('CallbackConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig()
            self.callback_config = temp_model.from_map(m['CallbackConfig'])
        return self


class UpdateCallbackConfigResponseBodyResult(TeaModel):
    def __init__(self, im_config=None):
        # im相关配置
        self.im_config = im_config  # type: UpdateCallbackConfigResponseBodyResultImConfig

    def validate(self):
        if self.im_config:
            self.im_config.validate()

    def to_map(self):
        _map = super(UpdateCallbackConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_config is not None:
            result['ImConfig'] = self.im_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfig()
            self.im_config = temp_model.from_map(m['ImConfig'])
        return self


class UpdateCallbackConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, code=None, success=None, result=None):
        # desc
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool
        # result
        self.result = result  # type: UpdateCallbackConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateCallbackConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateCallbackConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCallbackConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCallbackConfigResponse, self).to_map()
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
            temp_model = UpdateCallbackConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitTenantRequestRequest(TeaModel):
    def __init__(self, domain=None):
        # 应用appKey
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitTenantRequestRequest, self).to_map()
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


class InitTenantRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: InitTenantRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(InitTenantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = InitTenantRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class InitTenantResponseBody(TeaModel):
    def __init__(self, response_success=None, error_code=None, error_msg=None, result=None, request_id=None):
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 是否初始化成功
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitTenantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitTenantResponse, self).to_map()
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
            temp_model = InitTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatMemberRequestRequestParamsGroupChatMembers(TeaModel):
    def __init__(self, app_uid=None, role=None, nick=None, top=None, red_point=None, mute=None, visible=None,
                 join_time=None, modify_time=None, extensions=None):
        # 用户ID
        self.app_uid = app_uid  # type: str
        # 成员权限
        self.role = role  # type: long
        # 昵称
        self.nick = nick  # type: str
        # 是否置顶
        self.top = top  # type: bool
        # 未读数
        self.red_point = red_point  # type: long
        # 是否免打扰
        self.mute = mute  # type: bool
        # 是否可见
        self.visible = visible  # type: bool
        # 入群时间戳
        self.join_time = join_time  # type: long
        # 最后修改时间
        self.modify_time = modify_time  # type: long
        # 自定义信息
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatMemberRequestRequestParamsGroupChatMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.top is not None:
            result['Top'] = self.top
        if self.red_point is not None:
            result['RedPoint'] = self.red_point
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('RedPoint') is not None:
            self.red_point = m.get('RedPoint')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ImportGroupChatMemberRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, group_chat_members=None):
        # 群ID
        self.app_cid = app_cid  # type: str
        self.group_chat_members = group_chat_members  # type: list[ImportGroupChatMemberRequestRequestParamsGroupChatMembers]

    def validate(self):
        if self.group_chat_members:
            for k in self.group_chat_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportGroupChatMemberRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        result['GroupChatMembers'] = []
        if self.group_chat_members is not None:
            for k in self.group_chat_members:
                result['GroupChatMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        self.group_chat_members = []
        if m.get('GroupChatMembers') is not None:
            for k in m.get('GroupChatMembers'):
                temp_model = ImportGroupChatMemberRequestRequestParamsGroupChatMembers()
                self.group_chat_members.append(temp_model.from_map(k))
        return self


class ImportGroupChatMemberRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: ImportGroupChatMemberRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ImportGroupChatMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportGroupChatMemberRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportGroupChatMemberShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatMemberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportGroupChatMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ImportGroupChatMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportGroupChatMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportGroupChatMemberResponse, self).to_map()
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
            temp_model = ImportGroupChatMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupSilenceMembersRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None):
        # 操作者
        self.operator_app_uid = operator_app_uid  # type: str
        # 群会话id
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupSilenceMembersRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ListGroupSilenceMembersRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params = request_params  # type: ListGroupSilenceMembersRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ListGroupSilenceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ListGroupSilenceMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListGroupSilenceMembersShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupSilenceMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListGroupSilenceMembersResponseBodyResult(TeaModel):
    def __init__(self, app_cid=None, whitelist=None, blacklist=None):
        # 群会话id
        self.app_cid = app_cid  # type: str
        # 禁言白名单
        self.whitelist = whitelist  # type: list[str]
        # 禁言黑名单用户及对应禁言时长
        self.blacklist = blacklist  # type: dict[str, long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupSilenceMembersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        return self


class ListGroupSilenceMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: ListGroupSilenceMembersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListGroupSilenceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ListGroupSilenceMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListGroupSilenceMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupSilenceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupSilenceMembersResponse, self).to_map()
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
            temp_model = ListGroupSilenceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, keys=None):
        # 会话id
        self.app_cid = app_cid  # type: str
        # 拓展字段的key
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveGroupExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 移除群聊拓展字段请求实体
        self.request_params = request_params  # type: RemoveGroupExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveGroupExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 移除群聊拓展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveGroupExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveGroupExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveGroupExtensionByKeysResponse, self).to_map()
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
            temp_model = RemoveGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupMemberExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, app_uid=None, extensions=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 用户ID
        self.app_uid = app_uid  # type: str
        # 扩展信息
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupMemberExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetGroupMemberExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 设置群成员扩展信息的请求体
        self.request_params = request_params  # type: SetGroupMemberExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetGroupMemberExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetGroupMemberExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupMemberExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # App ID, IMPaaS租户的ID
        self.app_id = app_id  # type: str
        # 设置群成员扩展信息的请求体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupMemberExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetGroupMemberExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGroupMemberExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetGroupMemberExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGroupMemberExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGroupMemberExtensionByKeysResponse, self).to_map()
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
            temp_model = SetGroupMemberExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequestRequestParamsInitMembers(TeaModel):
    def __init__(self, app_uid=None, role=None, nick=None, join_time=None, extensions=None):
        self.app_uid = app_uid  # type: str
        # 1群主，2管理员，3普通
        self.role = role  # type: int
        self.nick = nick  # type: str
        # unix时间毫秒数
        self.join_time = join_time  # type: long
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequestRequestParamsInitMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class CreateGroupRequestRequestParams(TeaModel):
    def __init__(self, uuid=None, creator_app_uid=None, title=None, icon_media_id=None, extensions=None,
                 init_members=None):
        # UUID(不可重复)
        self.uuid = uuid  # type: str
        # 创建者
        self.creator_app_uid = creator_app_uid  # type: str
        # 群标题
        self.title = title  # type: str
        # 图标的id
        self.icon_media_id = icon_media_id  # type: str
        # 拓展字段
        self.extensions = extensions  # type: dict[str, str]
        # 初始化成员
        self.init_members = init_members  # type: list[CreateGroupRequestRequestParamsInitMembers]

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateGroupRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.creator_app_uid is not None:
            result['CreatorAppUid'] = self.creator_app_uid
        if self.title is not None:
            result['Title'] = self.title
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CreatorAppUid') is not None:
            self.creator_app_uid = m.get('CreatorAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = CreateGroupRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 创建群聊请求实体
        self.request_params = request_params  # type: CreateGroupRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = CreateGroupRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class CreateGroupShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 创建群聊请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class CreateGroupResponseBodyResult(TeaModel):
    def __init__(self, app_cid=None):
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: CreateGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = CreateGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageByIdRequestRequestParams(TeaModel):
    def __init__(self, msg_id=None):
        # 消息Id
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageByIdRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class GetMessageByIdRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        # 请求实体
        self.request_params = request_params  # type: GetMessageByIdRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetMessageByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMessageByIdRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMessageByIdShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        # 请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageByIdShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMessageByIdResponseBodyResult(TeaModel):
    def __init__(self, msg_id=None, app_cid=None, conversation_type=None, create_time=None, sender_id=None,
                 content_type=None, content=None, extensions=None):
        # 消息Id
        self.msg_id = msg_id  # type: str
        # 会话Id
        self.app_cid = app_cid  # type: str
        # 会话类型
        self.conversation_type = conversation_type  # type: int
        # 创建时间
        self.create_time = create_time  # type: long
        # 发送者的用户Id
        self.sender_id = sender_id  # type: str
        # 消息类型
        self.content_type = content_type  # type: int
        # 消息体
        self.content = content  # type: str
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageByIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class GetMessageByIdResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: GetMessageByIdResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMessageByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMessageByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMessageByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMessageByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMessageByIdResponse, self).to_map()
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
            temp_model = GetMessageByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyRoomRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, open_id=None):
        # 应用appKey
        self.domain = domain  # type: str
        # 房间id
        self.room_id = room_id  # type: str
        # 操作人id
        self.open_id = open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyRoomRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.room_id is not None:
            result['roomId'] = self.room_id
        if self.open_id is not None:
            result['openId'] = self.open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        if m.get('openId') is not None:
            self.open_id = m.get('openId')
        return self


class DestroyRoomRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: DestroyRoomRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(DestroyRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = DestroyRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class DestroyRoomResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, result=None, response_success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        # 是否销毁成功
        self.result = result  # type: bool
        self.response_success = response_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        return self


class DestroyRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DestroyRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DestroyRoomResponse, self).to_map()
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
            temp_model = DestroyRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickOffRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_keys=None, information=None):
        # 用户ID
        self.app_uid = app_uid  # type: str
        # 被踢下线的App的AppKey列表，为空时全部踢下线
        self.app_keys = app_keys  # type: list[str]
        # 下线文案
        self.information = information  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickOffRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_keys is not None:
            result['AppKeys'] = self.app_keys
        if self.information is not None:
            result['Information'] = self.information
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKeys') is not None:
            self.app_keys = m.get('AppKeys')
        if m.get('Information') is not None:
            self.information = m.get('Information')
        return self


class KickOffRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: KickOffRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(KickOffRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = KickOffRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class KickOffShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickOffShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class KickOffResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickOffResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class KickOffResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: KickOffResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KickOffResponse, self).to_map()
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
            temp_model = KickOffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallbackApiIdsResponseBodyResult(TeaModel):
    def __init__(self, spis=None, events=None):
        # 回调列表
        self.spis = spis  # type: dict[str, bool]
        # 事件输出列表
        self.events = events  # type: dict[str, bool]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCallbackApiIdsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spis is not None:
            result['Spis'] = self.spis
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class ListCallbackApiIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, http_status_code=None, message=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 业务是否成功
        self.success = success  # type: bool
        # 业务错误码
        self.code = code  # type: str
        # 网络错误码
        self.http_status_code = http_status_code  # type: int
        # 错误信息
        self.message = message  # type: str
        # 返回结果
        self.result = result  # type: ListCallbackApiIdsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListCallbackApiIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ListCallbackApiIdsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListCallbackApiIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCallbackApiIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCallbackApiIdsResponse, self).to_map()
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
            temp_model = ListCallbackApiIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageReadRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, msg_id=None):
        # 操作者ID
        self.app_uid = app_uid  # type: str
        # 消息ID
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageReadRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SetMessageReadRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: SetMessageReadRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetMessageReadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetMessageReadRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetMessageReadShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageReadShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetMessageReadResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageReadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetMessageReadResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetMessageReadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetMessageReadResponse, self).to_map()
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
            temp_model = SetMessageReadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMsgRecallIntervalRequestRequestParams(TeaModel):
    def __init__(self, client_msg_recall_interval_minute=None):
        # 消息撤回时间间隔
        self.client_msg_recall_interval_minute = client_msg_recall_interval_minute  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMsgRecallIntervalRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_msg_recall_interval_minute is not None:
            result['ClientMsgRecallIntervalMinute'] = self.client_msg_recall_interval_minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientMsgRecallIntervalMinute') is not None:
            self.client_msg_recall_interval_minute = m.get('ClientMsgRecallIntervalMinute')
        return self


class UpdateMsgRecallIntervalRequest(TeaModel):
    def __init__(self, request_params=None, app_id=None):
        # 请求
        self.request_params = request_params  # type: UpdateMsgRecallIntervalRequestRequestParams
        # 应用Id
        self.app_id = app_id  # type: str

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateMsgRecallIntervalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            temp_model = UpdateMsgRecallIntervalRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class UpdateMsgRecallIntervalShrinkRequest(TeaModel):
    def __init__(self, request_params_shrink=None, app_id=None):
        # 请求
        self.request_params_shrink = request_params_shrink  # type: str
        # 应用Id
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMsgRecallIntervalShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class UpdateMsgRecallIntervalResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, code=None, success=None, result=None):
        # desc
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool
        # result
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMsgRecallIntervalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateMsgRecallIntervalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateMsgRecallIntervalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMsgRecallIntervalResponse, self).to_map()
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
            temp_model = UpdateMsgRecallIntervalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToRoomUsersRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, sender_id=None, sub_type=None, body=None):
        # 应用的appKey。
        self.domain = domain  # type: str
        # 房间ID，由调用CreateRoom时返回。
        self.room_id = room_id  # type: str
        # 消息的发送者ID。
        self.sender_id = sender_id  # type: str
        # 消息的类型，由业务自定义，请传递100000以上。
        self.sub_type = sub_type  # type: int
        # 消息体。
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToRoomUsersRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class SendCustomMessageToRoomUsersRequest(TeaModel):
    def __init__(self, request=None, receivers=None):
        # 请求参数的结构体。
        self.request = request  # type: SendCustomMessageToRoomUsersRequestRequest
        # 指定的消息接受者的用户ID列表，大小不得超过100。
        self.receivers = receivers  # type: list[str]

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(SendCustomMessageToRoomUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = SendCustomMessageToRoomUsersRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        return self


class SendCustomMessageToRoomUsersResponseBodyResult(TeaModel):
    def __init__(self, message_id=None):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
        self.message_id = message_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToRoomUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageToRoomUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_message=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 请求是否成功。
        self.response_success = response_success  # type: bool
        # 错误码，请求异常时返回。
        self.error_code = error_code  # type: str
        # 错误信息，请求异常时返回。
        self.error_message = error_message  # type: str
        # 请求的返回结果。
        self.result = result  # type: SendCustomMessageToRoomUsersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendCustomMessageToRoomUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToRoomUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCustomMessageToRoomUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCustomMessageToRoomUsersResponse, self).to_map()
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
            temp_model = SendCustomMessageToRoomUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupTitleRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, operator_app_uid=None, title=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 操作者用户ID
        self.operator_app_uid = operator_app_uid  # type: str
        # 群聊标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupTitleRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGroupTitleRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: UpdateGroupTitleRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(UpdateGroupTitleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupTitleRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupTitleShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupTitleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupTitleResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupTitleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupTitleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupTitleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupTitleResponse, self).to_map()
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
            temp_model = UpdateGroupTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_key=None, device_id=None):
        # 用户ID
        self.app_uid = app_uid  # type: str
        # AppKey
        self.app_key = app_key  # type: str
        # 设备ID
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: GetLoginTokenRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetLoginTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetLoginTokenRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetLoginTokenShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetLoginTokenResponseBodyResult(TeaModel):
    def __init__(self, access_token=None, refresh_token=None, access_token_expired_time=None):
        # 登录Tokon
        self.access_token = access_token  # type: str
        # 更新Token
        self.refresh_token = refresh_token  # type: str
        # 登录Token过期时间
        self.access_token_expired_time = access_token_expired_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: GetLoginTokenResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetLoginTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLoginTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponse, self).to_map()
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DismissGroupRequestRequestParams(TeaModel):
    def __init__(self, operator_app_uid=None, app_cid=None):
        # 操作用户
        self.operator_app_uid = operator_app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DismissGroupRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class DismissGroupRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        self.app_id = app_id  # type: str
        # 解散群聊请求实体
        self.request_params = request_params  # type: DismissGroupRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(DismissGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = DismissGroupRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class DismissGroupShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        self.app_id = app_id  # type: str
        # 解散群聊请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DismissGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class DismissGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DismissGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DismissGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DismissGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DismissGroupResponse, self).to_map()
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
            temp_model = DismissGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatConversationRequestRequestParams(TeaModel):
    def __init__(self, uuid=None, owner_app_uid=None, title=None, icon_media_id=None, member_limit=None,
                 extensions=None, create_time=None, silence_all=None):
        # 唯一标识，用于重入
        self.uuid = uuid  # type: str
        # 群主uid
        self.owner_app_uid = owner_app_uid  # type: str
        # 群标题
        self.title = title  # type: str
        # 群头像
        self.icon_media_id = icon_media_id  # type: str
        # 群上限
        self.member_limit = member_limit  # type: long
        # 扩展字段
        self.extensions = extensions  # type: dict[str, str]
        # 创建时间
        self.create_time = create_time  # type: long
        # 是否全员禁言
        self.silence_all = silence_all  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatConversationRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.owner_app_uid is not None:
            result['OwnerAppUid'] = self.owner_app_uid
        if self.title is not None:
            result['Title'] = self.title
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.member_limit is not None:
            result['MemberLimit'] = self.member_limit
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.silence_all is not None:
            result['SilenceAll'] = self.silence_all
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('OwnerAppUid') is not None:
            self.owner_app_uid = m.get('OwnerAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('MemberLimit') is not None:
            self.member_limit = m.get('MemberLimit')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SilenceAll') is not None:
            self.silence_all = m.get('SilenceAll')
        return self


class ImportGroupChatConversationRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: ImportGroupChatConversationRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(ImportGroupChatConversationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportGroupChatConversationRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportGroupChatConversationShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatConversationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportGroupChatConversationResponseBodyResult(TeaModel):
    def __init__(self, app_cid=None):
        # 群ID
        self.app_cid = app_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportGroupChatConversationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ImportGroupChatConversationResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: ImportGroupChatConversationResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ImportGroupChatConversationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ImportGroupChatConversationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportGroupChatConversationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportGroupChatConversationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportGroupChatConversationResponse, self).to_map()
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
            temp_model = ImportGroupChatConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequestRequest(TeaModel):
    def __init__(self, domain=None, owner_id=None, owner_nick=None, title=None):
        # 应用appKey
        self.domain = domain  # type: str
        # 创建者id
        self.owner_id = owner_id  # type: str
        # 创建者昵称
        self.owner_nick = owner_nick  # type: str
        # 创建房间的标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.owner_nick is not None:
            result['ownerNick'] = self.owner_nick
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('ownerNick') is not None:
            self.owner_nick = m.get('ownerNick')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateRoomRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: CreateRoomRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(CreateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(self, room_id=None):
        # 房间id
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['roomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(self, response_success=None, error_code=None, error_msg=None, result=None, request_id=None):
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        self.result = result  # type: CreateRoomResponseBodyResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRoomResponse, self).to_map()
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_cid=None, keys=None):
        # 用户id
        self.app_uid = app_uid  # type: str
        # 会话id
        self.app_cid = app_cid  # type: str
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserConversationExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveUserConversationExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        self.app_id = app_id  # type: str
        # 移除用户拓展字段请求实体
        self.request_params = request_params  # type: RemoveUserConversationExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(RemoveUserConversationExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveUserConversationExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveUserConversationExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        self.app_id = app_id  # type: str
        # 移除用户拓展字段请求实体
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserConversationExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveUserConversationExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserConversationExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveUserConversationExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserConversationExtensionByKeysResponse, self).to_map()
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
            temp_model = RemoveUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(self, app_cid=None, msg_id=None, extensions=None):
        # 会话ID
        self.app_cid = app_cid  # type: str
        # 消息ID
        self.msg_id = msg_id  # type: str
        # 需设置的K-V对
        self.extensions = extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageExtensionByKeysRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetMessageExtensionByKeysRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: SetMessageExtensionByKeysRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(SetMessageExtensionByKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetMessageExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetMessageExtensionByKeysShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageExtensionByKeysShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetMessageExtensionByKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误码，成功时为0
        self.code = code  # type: str
        # 错误信息，成功时为空
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageExtensionByKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetMessageExtensionByKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetMessageExtensionByKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetMessageExtensionByKeysResponse, self).to_map()
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
            temp_model = SetMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResultImportMessageResultValue(TeaModel):
    def __init__(self, result=None, msg_id=None):
        # 0 成功
        self.result = result  # type: long
        # 消息ID
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultImportMessageResultValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.msg_id is not None:
            result['msgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('msgId') is not None:
            self.msg_id = m.get('msgId')
        return self


class RequestParamsOptionsSingleChatCreateRequestUserConversationValue(TeaModel):
    def __init__(self, user_extensions=None):
        # 扩展信息
        self.user_extensions = user_extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestParamsOptionsSingleChatCreateRequestUserConversationValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_extensions is not None:
            result['UserExtensions'] = self.user_extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserExtensions') is not None:
            self.user_extensions = m.get('UserExtensions')
        return self


class ResultUserMuteSettingsValue(TeaModel):
    def __init__(self, mute=None, expire_time=None):
        self.mute = mute  # type: bool
        self.expire_time = expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultUserMuteSettingsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class RequestParamsUserConversationsValue(TeaModel):
    def __init__(self, top=None, red_point=None, mute=None, visible=None, create_time=None, modify_time=None,
                 user_extensions=None):
        # 是否置顶
        self.top = top  # type: bool
        # 未读数
        self.red_point = red_point  # type: long
        # 是否免打扰
        self.mute = mute  # type: bool
        # 是否可见
        self.visible = visible  # type: bool
        # 创建时间戳
        self.create_time = create_time  # type: long
        # 修改时间戳
        self.modify_time = modify_time  # type: long
        # 自定义信息
        self.user_extensions = user_extensions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestParamsUserConversationsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.red_point is not None:
            result['RedPoint'] = self.red_point
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.user_extensions is not None:
            result['UserExtensions'] = self.user_extensions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('RedPoint') is not None:
            self.red_point = m.get('RedPoint')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('UserExtensions') is not None:
            self.user_extensions = m.get('UserExtensions')
        return self


