# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateLiveRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, live_id=None, title=None, introduction=None,
                 anchor_id=None, code_level=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id  # type: str
        # 创建直播用户。
        self.user_id = user_id  # type: str
        # 直播资源的唯一标识ID，缺省时系统自动生成36位随机uuid字符串。
        self.live_id = live_id  # type: str
        # 直播标题，支持中英文，最大长度256位。
        self.title = title  # type: str
        # 直播简介，支持中英文，最大长度2048位。
        self.introduction = introduction  # type: str
        # 主播ID，支持中英文，最大长度128位，缺省时主播为当前创建直播用户。
        self.anchor_id = anchor_id  # type: str
        # 直播推流码率，缺省时默认为3。取值：  -1：流畅lld。 1：标清lsd。 2：高清lhd。 3：超清lud。
        self.code_level = code_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        return self


class CreateLiveResponseBodyResult(TeaModel):
    def __init__(self, live_id=None):
        # 直播的唯一标识ID。
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class CreateLiveResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateLiveResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateLiveResponseBody, self).to_map()
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
            temp_model = CreateLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用唯一标识
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
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
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


class UpdateRoomRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, title=None, notice=None, room_owner_id=None, extension=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class UpdateRoomResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoomResponseBody, self).to_map()
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


class UpdateRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRoomResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppTemplateRequest(TeaModel):
    def __init__(self, app_template_id=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class GetAppTemplateResponseBodyResultConfigList(TeaModel):
    def __init__(self, key=None, value=None):
        # 配置项
        self.key = key  # type: str
        # 配置项内容
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppTemplateResponseBodyResultConfigList, self).to_map()
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


class GetAppTemplateResponseBodyResult(TeaModel):
    def __init__(self, app_template_name=None, app_template_creator=None, status=None, component_list=None,
                 create_time=None, sdk_info=None, config_list=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用模板创建者
        self.app_template_creator = app_template_creator  # type: str
        # 应用模板使用状态
        self.status = status  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]
        # 创建时间
        self.create_time = create_time  # type: str
        self.sdk_info = sdk_info  # type: str
        # 配置列表
        self.config_list = config_list  # type: list[GetAppTemplateResponseBodyResultConfigList]

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.status is not None:
            result['Status'] = self.status
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = GetAppTemplateResponseBodyResultConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class GetAppTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetAppTemplateResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAppTemplateResponseBody, self).to_map()
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
            temp_model = GetAppTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAppTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList(TeaModel):
    def __init__(self, plugin_type=None, plugin_id=None, create_time=None, extension=None):
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class GetRoomResponseBodyResultRoomInfo(TeaModel):
    def __init__(self, room_id=None, title=None, create_time=None, notice=None, room_owner_id=None, uv=None,
                 online_count=None, plugin_instance_info_list=None, app_id=None, template_id=None, extension=None):
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房间标题。
        self.title = title  # type: str
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 房间公告。
        self.notice = notice  # type: str
        # 房主用户id。
        self.room_owner_id = room_owner_id  # type: str
        # 访问用户数。
        self.uv = uv  # type: long
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList]
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 创建房间使用的模板id。
        self.template_id = template_id  # type: str
        # 房间拓展字段。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRoomResponseBodyResultRoomInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class GetRoomResponseBodyResult(TeaModel):
    def __init__(self, room_info=None):
        # 房间信息。
        self.room_info = room_info  # type: GetRoomResponseBodyResultRoomInfo

    def validate(self):
        if self.room_info:
            self.room_info.validate()

    def to_map(self):
        _map = super(GetRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_info is not None:
            result['RoomInfo'] = self.room_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomInfo') is not None:
            temp_model = GetRoomResponseBodyResultRoomInfo()
            self.room_info = temp_model.from_map(m['RoomInfo'])
        return self


class GetRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 查询房间信息返回结果。
        self.result = result  # type: GetRoomResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRoomResponseBody, self).to_map()
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
            temp_model = GetRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRoomResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppTemplateRequest(TeaModel):
    def __init__(self, app_template_name=None, component_list=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class CreateAppTemplateShrinkRequest(TeaModel):
    def __init__(self, app_template_name=None, component_list_shrink=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list_shrink = component_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list_shrink is not None:
            result['ComponentList'] = self.component_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list_shrink = m.get('ComponentList')
        return self


class CreateAppTemplateResponseBodyResult(TeaModel):
    def __init__(self, app_template_id=None):
        # 应用模板唯一标示
        self.app_template_id = app_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class CreateAppTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: CreateAppTemplateResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateAppTemplateResponseBody, self).to_map()
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
            temp_model = CreateAppTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsRequest, self).to_map()
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


class ListAppsResponseBodyResultAppInfoList(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_template_id=None, app_template_name=None, app_key=None,
                 app_status=None, create_time=None, component_list=None):
        # 应用唯一标识符
        self.app_id = app_id  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用Key
        self.app_key = app_key  # type: str
        # 应用状态
        self.app_status = app_status  # type: str
        # 应用创建时间
        self.create_time = create_time  # type: str
        # 应用组件列表
        self.component_list = component_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsResponseBodyResultAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class ListAppsResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, page_total=None, app_info_list=None):
        # 总条目数
        self.total_count = total_count  # type: int
        # 总页数
        self.page_total = page_total  # type: int
        # App信息列表
        self.app_info_list = app_info_list  # type: list[ListAppsResponseBodyResultAppInfoList]

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListAppsResponseBodyResultAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果体
        self.result = result  # type: ListAppsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAppsResponseBody, self).to_map()
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
            temp_model = ListAppsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAppsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomsRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList(TeaModel):
    def __init__(self, plugin_type=None, plugin_id=None, create_time=None, extension=None):
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class ListRoomsResponseBodyResultRoomInfoList(TeaModel):
    def __init__(self, room_id=None, title=None, room_owner_id=None, notice=None, uv=None, online_count=None,
                 plugin_instance_info_list=None, create_time=None, app_id=None, template_id=None, extension=None):
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房间标题。
        self.title = title  # type: str
        # 房主用户id。
        self.room_owner_id = room_owner_id  # type: str
        # 房间公告。
        self.notice = notice  # type: str
        # 用户访问数。
        self.uv = uv  # type: long
        # 用户在线数。
        self.online_count = online_count  # type: long
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList]
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: str
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 创建房间使用的模板id。
        self.template_id = template_id  # type: str
        # 房间拓展字段。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomsResponseBodyResultRoomInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class ListRoomsResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, page_total=None, has_more=None, room_info_list=None):
        # 该应用的房间总数。
        self.total_count = total_count  # type: int
        # 该应用的房间总页数。
        self.page_total = page_total  # type: int
        # 是否还有下一页房间列表。
        self.has_more = has_more  # type: bool
        # 房间列表信息。
        self.room_info_list = room_info_list  # type: list[ListRoomsResponseBodyResultRoomInfoList]

    def validate(self):
        if self.room_info_list:
            for k in self.room_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['RoomInfoList'] = []
        if self.room_info_list is not None:
            for k in self.room_info_list:
                result['RoomInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.room_info_list = []
        if m.get('RoomInfoList') is not None:
            for k in m.get('RoomInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k))
        return self


class ListRoomsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: ListRoomsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListRoomsResponseBody, self).to_map()
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
            temp_model = ListRoomsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRoomsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRoomsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppTemplateRequest(TeaModel):
    def __init__(self, app_template_id=None):
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class DeleteAppTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppTemplateResponseBody, self).to_map()
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


class DeleteAppTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number  # type: str
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppTemplatesRequest, self).to_map()
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


class ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList(TeaModel):
    def __init__(self, key=None, value=None):
        # 配置项
        self.key = key  # type: str
        # 配置项内容
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList, self).to_map()
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


class ListAppTemplatesResponseBodyResultAppTemplateInfoList(TeaModel):
    def __init__(self, app_template_id=None, app_template_name=None, app_template_creator=None, status=None,
                 component_list=None, create_time=None, sdk_info=None, config_list=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用模板创建者
        self.app_template_creator = app_template_creator  # type: str
        # 应用模板使用状态
        self.status = status  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]
        # 创建时间
        self.create_time = create_time  # type: str
        # SDK信息
        self.sdk_info = sdk_info  # type: str
        # 配置列表
        self.config_list = config_list  # type: list[ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList]

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponseBodyResultAppTemplateInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.status is not None:
            result['Status'] = self.status
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBodyResult(TeaModel):
    def __init__(self, total_count=None, page_total=None, app_template_info_list=None):
        # 总条目数
        self.total_count = total_count  # type: int
        # 总页数
        self.page_total = page_total  # type: int
        # 应用模板信息列表
        self.app_template_info_list = app_template_info_list  # type: list[ListAppTemplatesResponseBodyResultAppTemplateInfoList]

    def validate(self):
        if self.app_template_info_list:
            for k in self.app_template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['AppTemplateInfoList'] = []
        if self.app_template_info_list is not None:
            for k in self.app_template_info_list:
                result['AppTemplateInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.app_template_info_list = []
        if m.get('AppTemplateInfoList') is not None:
            for k in m.get('AppTemplateInfoList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoList()
                self.app_template_info_list.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: ListAppTemplatesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponseBody, self).to_map()
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
            temp_model = ListAppTemplatesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAppTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(self, app_id=None, app_template_id=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class ListComponentsResponseBodyResultComponentCategoryList(TeaModel):
    def __init__(self, component_type=None, component_name=None, in_use=None):
        # 组件类型
        self.component_type = component_type  # type: str
        # 组件名称
        self.component_name = component_name  # type: str
        # 是否使用
        self.in_use = in_use  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultComponentCategoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.in_use is not None:
            result['InUse'] = self.in_use
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        return self


class ListComponentsResponseBodyResultComponentCategory(TeaModel):
    def __init__(self, type=None, list=None):
        # 组件类别
        self.type = type  # type: str
        # 类别下的组件列表
        self.list = list  # type: list[ListComponentsResponseBodyResultComponentCategoryList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultComponentCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListComponentsResponseBodyResultComponentCategoryList()
                self.list.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBodyResultConfigGroup(TeaModel):
    def __init__(self, key=None, value=None, category=None):
        self.key = key  # type: str
        self.value = value  # type: str
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultConfigGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListComponentsResponseBodyResult(TeaModel):
    def __init__(self, component_category=None, config_group=None):
        # 组件信息
        self.component_category = component_category  # type: list[ListComponentsResponseBodyResultComponentCategory]
        # 配置信息
        self.config_group = config_group  # type: list[ListComponentsResponseBodyResultConfigGroup]

    def validate(self):
        if self.component_category:
            for k in self.component_category:
                if k:
                    k.validate()
        if self.config_group:
            for k in self.config_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentCategory'] = []
        if self.component_category is not None:
            for k in self.component_category:
                result['ComponentCategory'].append(k.to_map() if k else None)
        result['ConfigGroup'] = []
        if self.config_group is not None:
            for k in self.config_group:
                result['ConfigGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component_category = []
        if m.get('ComponentCategory') is not None:
            for k in m.get('ComponentCategory'):
                temp_model = ListComponentsResponseBodyResultComponentCategory()
                self.component_category.append(temp_model.from_map(k))
        self.config_group = []
        if m.get('ConfigGroup') is not None:
            for k in m.get('ConfigGroup'):
                temp_model = ListComponentsResponseBodyResultConfigGroup()
                self.config_group.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果体
        self.result = result  # type: ListComponentsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBody, self).to_map()
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
            temp_model = ListComponentsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListComponentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRequest(TeaModel):
    def __init__(self, live_id=None, title=None, introduction=None):
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 直播标题，支持中英文，最大长度256位
        self.title = title  # type: str
        # 直播简介，支持中英文，最大长度2048位
        self.introduction = introduction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        return self


class UpdateLiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveResponseBody, self).to_map()
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


class UpdateLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppTemplateConfigRequestConfigList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateConfigRequestConfigList, self).to_map()
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


class UpdateAppTemplateConfigRequest(TeaModel):
    def __init__(self, app_template_id=None, config_list=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 更新配置
        self.config_list = config_list  # type: list[UpdateAppTemplateConfigRequestConfigList]

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAppTemplateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = UpdateAppTemplateConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class UpdateAppTemplateConfigShrinkRequest(TeaModel):
    def __init__(self, app_template_id=None, config_list_shrink=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 更新配置
        self.config_list_shrink = config_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')
        return self


class UpdateAppTemplateConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateConfigResponseBody, self).to_map()
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


class UpdateAppTemplateConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppTemplateConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppTemplateConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppTemplateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, live_id=None):
        # 租户名
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36位
        self.room_id = room_id  # type: str
        # 创建直播用户ID
        self.user_id = user_id  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class StopLiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveResponseBody, self).to_map()
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


class StopLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppRequest, self).to_map()
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


class GetAppResponseBodyResult(TeaModel):
    def __init__(self, app_name=None, app_template_id=None, app_template_name=None, app_status=None, app_key=None,
                 create_time=None, component_list=None):
        # 应用名称
        self.app_name = app_name  # type: str
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str
        # 应用Key
        self.app_key = app_key  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 组件列表。
        self.component_list = component_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetAppResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAppResponseBody, self).to_map()
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
            temp_model = GetAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRequest(TeaModel):
    def __init__(self, live_id=None):
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DeleteLiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLiveResponseBody, self).to_map()
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


class DeleteLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveDomainStatusRequest(TeaModel):
    def __init__(self, app_id=None, live_domain_list=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 直播域名列表
        self.live_domain_list = live_domain_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveDomainStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_domain_list is not None:
            result['LiveDomainList'] = self.live_domain_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list = m.get('LiveDomainList')
        return self


class GetLiveDomainStatusShrinkRequest(TeaModel):
    def __init__(self, app_id=None, live_domain_list_shrink=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 直播域名列表
        self.live_domain_list_shrink = live_domain_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveDomainStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_domain_list_shrink is not None:
            result['LiveDomainList'] = self.live_domain_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list_shrink = m.get('LiveDomainList')
        return self


class GetLiveDomainStatusResponseBodyResultLiveDomainInfoList(TeaModel):
    def __init__(self, domain=None, cname=None, status=None):
        # 直播域名
        self.domain = domain  # type: str
        # 直播域名CNAME
        self.cname = cname  # type: str
        # 直播域名状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveDomainStatusResponseBodyResultLiveDomainInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLiveDomainStatusResponseBodyResult(TeaModel):
    def __init__(self, live_domain_info_list=None):
        # 直播域名信息列表
        self.live_domain_info_list = live_domain_info_list  # type: list[GetLiveDomainStatusResponseBodyResultLiveDomainInfoList]

    def validate(self):
        if self.live_domain_info_list:
            for k in self.live_domain_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLiveDomainStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveDomainInfoList'] = []
        if self.live_domain_info_list is not None:
            for k in self.live_domain_info_list:
                result['LiveDomainInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_domain_info_list = []
        if m.get('LiveDomainInfoList') is not None:
            for k in m.get('LiveDomainInfoList'):
                temp_model = GetLiveDomainStatusResponseBodyResultLiveDomainInfoList()
                self.live_domain_info_list.append(temp_model.from_map(k))
        return self


class GetLiveDomainStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetLiveDomainStatusResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveDomainStatusResponseBody, self).to_map()
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
            temp_model = GetLiveDomainStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveDomainStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLiveDomainStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveDomainStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLiveDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, app_key=None, device_id=None):
        # 用户的应用ID，在控制台创建应用时生成
        self.app_id = app_id  # type: str
        # 用户UserId,在AppId下单独唯一
        self.user_id = user_id  # type: str
        # 终端设备类型,通过控制台创建和查询
        self.app_key = app_key  # type: str
        # 终端设备ID
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetAuthTokenResponseBodyResult(TeaModel):
    def __init__(self, access_token=None, refresh_token=None, access_token_expired_time=None):
        # 用于长链接建连的token
        self.access_token = access_token  # type: str
        # 更新Token，若AccessToken过期，则可以使用RefreshToken再次获取新Token
        self.refresh_token = refresh_token  # type: str
        # 登录token过期时间(毫秒)
        self.access_token_expired_time = access_token_expired_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenResponseBodyResult, self).to_map()
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


class GetAuthTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: GetAuthTokenResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAuthTokenResponseBody, self).to_map()
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
            temp_model = GetAuthTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAuthTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuthTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppTemplateRequest(TeaModel):
    def __init__(self, app_template_id=None, app_template_name=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        return self


class UpdateAppTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateResponseBody, self).to_map()
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


class UpdateAppTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImpProductStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 开通状态
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImpProductStatusResponseBody, self).to_map()
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


class GetImpProductStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImpProductStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImpProductStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImpProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishLiveRequest(TeaModel):
    def __init__(self, live_id=None, user_id=None):
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 当前用户Id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PublishLiveResponseBodyResult(TeaModel):
    def __init__(self, live_id=None, anchor_id=None, status=None, push_url=None, live_url=None):
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 主播ID
        self.anchor_id = anchor_id  # type: str
        # 直播状态：Created-已创建未开播，Living-直播中，End-直播结束
        self.status = status  # type: str
        # 直播推流地址
        self.push_url = push_url  # type: str
        # 直播拉流地址
        self.live_url = live_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishLiveResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.status is not None:
            result['Status'] = self.status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        return self


class PublishLiveResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: PublishLiveResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(PublishLiveResponseBody, self).to_map()
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
            temp_model = PublishLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRequest(TeaModel):
    def __init__(self, live_id=None):
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveResponseBodyResultPlayUrlInfoList(TeaModel):
    def __init__(self, code_level=None, flv_url=None, hls_url=None, rtmp_url=None):
        # 直播拉取分辨率 -1:lld 1:lsd 2:lhd 3:lud
        self.code_level = code_level  # type: int
        # flv拉流地址
        self.flv_url = flv_url  # type: str
        # hls拉流地址
        self.hls_url = hls_url  # type: str
        # rtmp拉流地址
        self.rtmp_url = rtmp_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveResponseBodyResultPlayUrlInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.flv_url is not None:
            result['FlvUrl'] = self.flv_url
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('FlvUrl') is not None:
            self.flv_url = m.get('FlvUrl')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')
        return self


class GetLiveResponseBodyResult(TeaModel):
    def __init__(self, anchor_id=None, live_id=None, title=None, playback_url=None, create_time=None, end_time=None,
                 duration=None, push_url=None, live_url=None, status=None, introduction=None, room_id=None, app_id=None,
                 user_id=None, code_level=None, play_url_info_list=None):
        # 主播ID
        self.anchor_id = anchor_id  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 直播标题
        self.title = title  # type: str
        # 直播回放地址
        self.playback_url = playback_url  # type: str
        # 直播创建时间（毫秒ms）
        self.create_time = create_time  # type: long
        # 直播结束时间（毫秒ms）
        self.end_time = end_time  # type: long
        # 直播持续时间（毫秒ms）
        self.duration = duration  # type: long
        # 直播推流地址
        self.push_url = push_url  # type: str
        # 直播拉流地址
        self.live_url = live_url  # type: str
        # 直播状态：Created-已创建，未开播，Living-直播中，End-直播结束
        self.status = status  # type: str
        # 直播简介
        self.introduction = introduction  # type: str
        # 房间id
        self.room_id = room_id  # type: str
        # 租户名
        self.app_id = app_id  # type: str
        # 创建直播用户
        self.user_id = user_id  # type: str
        # 直播推送分辨率 -1:lld 1:lsd 2:lhd 3:lud
        self.code_level = code_level  # type: int
        # 多分辨率多协议播放信息
        self.play_url_info_list = play_url_info_list  # type: list[GetLiveResponseBodyResultPlayUrlInfoList]

    def validate(self):
        if self.play_url_info_list:
            for k in self.play_url_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLiveResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.status is not None:
            result['Status'] = self.status
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        result['PlayUrlInfoList'] = []
        if self.play_url_info_list is not None:
            for k in self.play_url_info_list:
                result['PlayUrlInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        self.play_url_info_list = []
        if m.get('PlayUrlInfoList') is not None:
            for k in m.get('PlayUrlInfoList'):
                temp_model = GetLiveResponseBodyResultPlayUrlInfoList()
                self.play_url_info_list.append(temp_model.from_map(k))
        return self


class GetLiveResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: GetLiveResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveResponseBody, self).to_map()
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
            temp_model = GetLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoomRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class DeleteRoomResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoomResponseBody, self).to_map()
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


class DeleteRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRoomResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None, app_template_id=None):
        # 应用名称
        self.app_name = app_name  # type: str
        # 模板ID
        self.app_template_id = app_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(self, app_id=None):
        # 应用唯一标示
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBodyResult, self).to_map()
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


class CreateAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateRoomRequest(TeaModel):
    def __init__(self, app_id=None, template_id=None, room_id=None, title=None, notice=None, room_owner_id=None,
                 extension=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间模板唯一标识，当前支持的取值：default，传空默认为default。
        self.template_id = template_id  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
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
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: CreateRoomResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRoomResponseBody, self).to_map()
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
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class UpdateAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_status=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str

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
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppResponseBody, self).to_map()
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


class UpdateAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


