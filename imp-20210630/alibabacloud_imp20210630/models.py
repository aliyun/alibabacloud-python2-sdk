# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateIceProjectRequest(TeaModel):
    def __init__(self, app_id=None, url_region_id=None, project_title=None, cover_url=None, live_id=None):
        # appId
        self.app_id = app_id  # type: str
        # 回放地址的地址
        self.url_region_id = url_region_id  # type: str
        # 工程标题
        self.project_title = project_title  # type: str
        # 封面
        self.cover_url = cover_url  # type: str
        # 唯一ID，比如直播uuid
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIceProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.url_region_id is not None:
            result['UrlRegionId'] = self.url_region_id
        if self.project_title is not None:
            result['ProjectTitle'] = self.project_title
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UrlRegionId') is not None:
            self.url_region_id = m.get('UrlRegionId')
        if m.get('ProjectTitle') is not None:
            self.project_title = m.get('ProjectTitle')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class CreateIceProjectResponseBodyResult(TeaModel):
    def __init__(self, project_id=None):
        # 工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIceProjectResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateIceProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateIceProjectResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateIceProjectResponseBody, self).to_map()
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
            temp_model = CreateIceProjectResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateIceProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIceProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIceProjectResponse, self).to_map()
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
            temp_model = CreateIceProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMemberRequest(TeaModel):
    def __init__(self, conference_id=None, to_user_id=None, from_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 被邀请用户ID
        self.to_user_id = to_user_id  # type: str
        # 邀请者用户ID
        self.from_user_id = from_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class RemoveMemberResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMemberResponseBody, self).to_map()
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


class RemoveMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveMemberResponse, self).to_map()
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
            temp_model = RemoveMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplyLinkMicUsersRequest(TeaModel):
    def __init__(self, conference_id=None, page_number=None, page_size=None):
        # 会议唯一标识符
        self.conference_id = conference_id  # type: str
        # 查询页码，从第1页开始。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大显示个数为100。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplyLinkMicUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApplyLinkMicUsersResponseBodyResult(TeaModel):
    def __init__(self, apply_link_mic_user_list=None, has_more=None, total_count=None, page_total=None):
        # 会议申请连麦用户列表。
        self.apply_link_mic_user_list = apply_link_mic_user_list  # type: list[str]
        # 是否还有下一页成员列表。
        self.has_more = has_more  # type: bool
        # 该会议的申请连麦成员总数。
        self.total_count = total_count  # type: int
        # 改会议的申请连麦成员总页数。
        self.page_total = page_total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplyLinkMicUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_link_mic_user_list is not None:
            result['ApplyLinkMicUserList'] = self.apply_link_mic_user_list
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyLinkMicUserList') is not None:
            self.apply_link_mic_user_list = m.get('ApplyLinkMicUserList')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        return self


class ListApplyLinkMicUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: ListApplyLinkMicUsersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListApplyLinkMicUsersResponseBody, self).to_map()
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
            temp_model = ListApplyLinkMicUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListApplyLinkMicUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListApplyLinkMicUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplyLinkMicUsersResponse, self).to_map()
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
            temp_model = ListApplyLinkMicUsersResponseBody()
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


class BanCommentRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, ban_comment_user=None, ban_comment_time=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str
        # 被禁言的用户在房间内的唯一标识
        self.ban_comment_user = ban_comment_user  # type: str
        # 禁言时长（秒）
        self.ban_comment_time = ban_comment_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BanCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        if self.ban_comment_time is not None:
            result['BanCommentTime'] = self.ban_comment_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        if m.get('BanCommentTime') is not None:
            self.ban_comment_time = m.get('BanCommentTime')
        return self


class BanCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 操作是否成功
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BanCommentResponseBody, self).to_map()
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


class BanCommentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BanCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BanCommentResponse, self).to_map()
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
            temp_model = BanCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMemberRequest(TeaModel):
    def __init__(self, conference_id=None, to_user_id=None, from_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 被邀请用户ID
        self.to_user_id = to_user_id  # type: str
        # 邀请者用户ID
        self.from_user_id = from_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class AddMemberResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMemberResponseBody, self).to_map()
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


class AddMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMemberResponse, self).to_map()
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
            temp_model = AddMemberResponseBody()
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


class RegisterIceOssMediaRequest(TeaModel):
    def __init__(self, project_id=None, app_id=None, playback_url_domain=None, oss_bucket=None, oss_endpoint=None,
                 url_region_id=None, media_url=None, from_type=None, media_title=None, live_id=None):
        # 工程ID
        self.project_id = project_id  # type: str
        # appId
        self.app_id = app_id  # type: str
        # 回放cdn域名
        self.playback_url_domain = playback_url_domain  # type: str
        # oss bucket
        self.oss_bucket = oss_bucket  # type: str
        # oss域名
        self.oss_endpoint = oss_endpoint  # type: str
        # 回放地址的区域ID
        self.url_region_id = url_region_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.media_url = media_url  # type: str
        # 来源的服务
        self.from_type = from_type  # type: str
        # 媒资标题
        self.media_title = media_title  # type: str
        # 唯一ID，比如直播uuid
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterIceOssMediaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.playback_url_domain is not None:
            result['PlaybackUrlDomain'] = self.playback_url_domain
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.url_region_id is not None:
            result['UrlRegionId'] = self.url_region_id
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.media_title is not None:
            result['MediaTitle'] = self.media_title
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PlaybackUrlDomain') is not None:
            self.playback_url_domain = m.get('PlaybackUrlDomain')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('UrlRegionId') is not None:
            self.url_region_id = m.get('UrlRegionId')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('MediaTitle') is not None:
            self.media_title = m.get('MediaTitle')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class RegisterIceOssMediaResponseBodyResult(TeaModel):
    def __init__(self, media_id=None):
        # 媒体Id
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterIceOssMediaResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class RegisterIceOssMediaResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        self.result = result  # type: RegisterIceOssMediaResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RegisterIceOssMediaResponseBody, self).to_map()
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
            temp_model = RegisterIceOssMediaResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class RegisterIceOssMediaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterIceOssMediaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterIceOssMediaResponse, self).to_map()
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
            temp_model = RegisterIceOssMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConferenceRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, title=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id  # type: str
        # 创建会议用户。
        self.user_id = user_id  # type: str
        # 会议标题，支持中英文，最大长度256位。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateConferenceResponseBodyResult(TeaModel):
    def __init__(self, conference_id=None):
        # 会议的唯一标识ID。
        self.conference_id = conference_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConferenceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class CreateConferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateConferenceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateConferenceResponseBody, self).to_map()
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
            temp_model = CreateConferenceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateConferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConferenceResponse, self).to_map()
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
            temp_model = CreateConferenceResponseBody()
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
    def __init__(self, app_id=None, live_domain_list=None, live_domain_type=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 直播域名列表
        self.live_domain_list = live_domain_list  # type: list[str]
        # 直播域名类型，推流域名: push, 拉流域名: pull, 回放域名: palyback
        self.live_domain_type = live_domain_type  # type: str

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
        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list = m.get('LiveDomainList')
        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')
        return self


class GetLiveDomainStatusShrinkRequest(TeaModel):
    def __init__(self, app_id=None, live_domain_list_shrink=None, live_domain_type=None):
        # 应用唯一标识
        self.app_id = app_id  # type: str
        # 直播域名列表
        self.live_domain_list_shrink = live_domain_list_shrink  # type: str
        # 直播域名类型，推流域名: push, 拉流域名: pull, 回放域名: palyback
        self.live_domain_type = live_domain_type  # type: str

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
        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list_shrink = m.get('LiveDomainList')
        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')
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


class SendCustomMessageToAllRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, body=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 消息体内容。
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class SendCustomMessageToAllResponseBodyResult(TeaModel):
    def __init__(self, message_id=None):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
        self.message_id = message_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToAllResponseBodyResult, self).to_map()
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


class SendCustomMessageToAllResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: SendCustomMessageToAllResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendCustomMessageToAllResponseBody, self).to_map()
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
            temp_model = SendCustomMessageToAllResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToAllResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCustomMessageToAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCustomMessageToAllResponse, self).to_map()
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
            temp_model = SendCustomMessageToAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgreeLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, to_user_id=None, from_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 被同意用户ID
        self.to_user_id = to_user_id  # type: str
        # 同意者用户ID
        self.from_user_id = from_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgreeLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class AgreeLinkMicResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgreeLinkMicResponseBody, self).to_map()
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


class AgreeLinkMicResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AgreeLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AgreeLinkMicResponse, self).to_map()
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
            temp_model = AgreeLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainOwnerVerifyContentRequest(TeaModel):
    def __init__(self, live_domain_name=None):
        # 直播域名
        self.live_domain_name = live_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainOwnerVerifyContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_domain_name is not None:
            result['LiveDomainName'] = self.live_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveDomainName') is not None:
            self.live_domain_name = m.get('LiveDomainName')
        return self


class GetDomainOwnerVerifyContentResponseBodyResult(TeaModel):
    def __init__(self, content=None):
        # 域名归属校验内容
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainOwnerVerifyContentResponseBodyResult, self).to_map()
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


class GetDomainOwnerVerifyContentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetDomainOwnerVerifyContentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDomainOwnerVerifyContentResponseBody, self).to_map()
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
            temp_model = GetDomainOwnerVerifyContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDomainOwnerVerifyContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDomainOwnerVerifyContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainOwnerVerifyContentResponse, self).to_map()
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
            temp_model = GetDomainOwnerVerifyContentResponseBody()
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


class DeleteConferenceRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, conference_id=None):
        # 租户名
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36位
        self.room_id = room_id  # type: str
        # 创建会议用户ID
        self.user_id = user_id  # type: str
        # 会议资源的唯一标识ID
        self.conference_id = conference_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class DeleteConferenceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConferenceResponseBody, self).to_map()
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


class DeleteConferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConferenceResponse, self).to_map()
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
            temp_model = DeleteConferenceResponseBody()
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


class VerifyDomainOwnerRequest(TeaModel):
    def __init__(self, live_domain_name=None):
        # 直播域名
        self.live_domain_name = live_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDomainOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_domain_name is not None:
            result['LiveDomainName'] = self.live_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveDomainName') is not None:
            self.live_domain_name = m.get('LiveDomainName')
        return self


class VerifyDomainOwnerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDomainOwnerResponseBody, self).to_map()
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


class VerifyDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyDomainOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyDomainOwnerResponse, self).to_map()
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
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class GetStandardRoomJumpUrlRequest(TeaModel):
    def __init__(self, app_id=None, user_id=None, app_key=None, platform=None, biz_type=None, biz_id=None,
                 user_nick=None):
        # 用户的应用ID，在控制台创建应用时生成
        self.app_id = app_id  # type: str
        # 用户UserId,在AppId下单独唯一
        self.user_id = user_id  # type: str
        # 终端设备类型,通过控制台创建和查询
        self.app_key = app_key  # type: str
        # 平台：win, mac, android, ios, web
        self.platform = platform  # type: str
        # 业务类型：互动直播live，互动课堂class
        self.biz_type = biz_type  # type: str
        # 资源ID：根据业务类型来定，比如直播ID，课堂ID等
        self.biz_id = biz_id  # type: str
        # 用户昵称
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStandardRoomJumpUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class GetStandardRoomJumpUrlResponseBodyResult(TeaModel):
    def __init__(self, standard_room_jump_url=None):
        # 样板间跳转协议地址
        self.standard_room_jump_url = standard_room_jump_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStandardRoomJumpUrlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_room_jump_url is not None:
            result['StandardRoomJumpUrl'] = self.standard_room_jump_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StandardRoomJumpUrl') is not None:
            self.standard_room_jump_url = m.get('StandardRoomJumpUrl')
        return self


class GetStandardRoomJumpUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: GetStandardRoomJumpUrlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetStandardRoomJumpUrlResponseBody, self).to_map()
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
            temp_model = GetStandardRoomJumpUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetStandardRoomJumpUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStandardRoomJumpUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStandardRoomJumpUrlResponse, self).to_map()
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
            temp_model = GetStandardRoomJumpUrlResponseBody()
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


class ListRoomLivesRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, status=None, query_timestamp=None, size=None, room_id_list=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36个字符。
        self.room_id = room_id  # type: str
        # 直播状态筛选条件，0-直播 1-下播，不传则返回全部状态
        self.status = status  # type: int
        # 拉取在这个时间戳之前创建的直播，单位毫秒，不传则默认拉取最新创建的。
        self.query_timestamp = query_timestamp  # type: long
        # 拉取直播数量。
        self.size = size  # type: int
        # 房间ID列表，可指定多个房间id，过滤优先级高于RoomId。
        self.room_id_list = room_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomLivesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.query_timestamp is not None:
            result['QueryTimestamp'] = self.query_timestamp
        if self.size is not None:
            result['Size'] = self.size
        if self.room_id_list is not None:
            result['RoomIdList'] = self.room_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QueryTimestamp') is not None:
            self.query_timestamp = m.get('QueryTimestamp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('RoomIdList') is not None:
            self.room_id_list = m.get('RoomIdList')
        return self


class ListRoomLivesShrinkRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, status=None, query_timestamp=None, size=None,
                 room_id_list_shrink=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36个字符。
        self.room_id = room_id  # type: str
        # 直播状态筛选条件，0-直播 1-下播，不传则返回全部状态
        self.status = status  # type: int
        # 拉取在这个时间戳之前创建的直播，单位毫秒，不传则默认拉取最新创建的。
        self.query_timestamp = query_timestamp  # type: long
        # 拉取直播数量。
        self.size = size  # type: int
        # 房间ID列表，可指定多个房间id，过滤优先级高于RoomId。
        self.room_id_list_shrink = room_id_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomLivesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.query_timestamp is not None:
            result['QueryTimestamp'] = self.query_timestamp
        if self.size is not None:
            result['Size'] = self.size
        if self.room_id_list_shrink is not None:
            result['RoomIdList'] = self.room_id_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QueryTimestamp') is not None:
            self.query_timestamp = m.get('QueryTimestamp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('RoomIdList') is not None:
            self.room_id_list_shrink = m.get('RoomIdList')
        return self


class ListRoomLivesResponseBodyResultLiveList(TeaModel):
    def __init__(self, room_id=None, title=None, room_owner_id=None, notice=None, uv=None, app_id=None,
                 extension=None, live_id=None, status=None):
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
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 直播id。
        self.live_id = live_id  # type: str
        # 直播状态，0-在播 1-不在播。
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomLivesResponseBodyResultLiveList, self).to_map()
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRoomLivesResponseBodyResult(TeaModel):
    def __init__(self, has_more=None, live_list=None, next_query_timestamp=None):
        # 是否还有下一页直播列表。
        self.has_more = has_more  # type: bool
        # 直播列表信息。
        self.live_list = live_list  # type: list[ListRoomLivesResponseBodyResultLiveList]
        # 下一个拉取的时间戳，单位毫秒。
        self.next_query_timestamp = next_query_timestamp  # type: long

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomLivesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        if self.next_query_timestamp is not None:
            result['NextQueryTimestamp'] = self.next_query_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListRoomLivesResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        if m.get('NextQueryTimestamp') is not None:
            self.next_query_timestamp = m.get('NextQueryTimestamp')
        return self


class ListRoomLivesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: ListRoomLivesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListRoomLivesResponseBody, self).to_map()
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
            temp_model = ListRoomLivesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomLivesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRoomLivesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRoomLivesResponse, self).to_map()
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
            temp_model = ListRoomLivesResponseBody()
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


class UpdateRoomShrinkRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, title=None, notice=None, room_owner_id=None, extension_shrink=None):
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
        self.extension_shrink = extension_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoomShrinkRequest, self).to_map()
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
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
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
            self.extension_shrink = m.get('Extension')
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
                 create_time=None, sdk_info=None, config_list=None, scene=None, integration_mode=None, standard_room_info=None):
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
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str

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
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
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
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
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


class SendCommentRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, sender_id=None, content=None, extension=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 直播间唯一标识，在调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.sender_id = sender_id  # type: str
        # 发送的文本内容。最大的长度不超过256个字节。
        self.content = content  # type: str
        # 扩展字段，服务端仅做透传。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class SendCommentShrinkRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, sender_id=None, content=None, extension_shrink=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 直播间唯一标识，在调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.sender_id = sender_id  # type: str
        # 发送的文本内容。最大的长度不超过256个字节。
        self.content = content  # type: str
        # 扩展字段，服务端仅做透传。
        self.extension_shrink = extension_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        return self


class SendCommentResponseBodyResultCommentVO(TeaModel):
    def __init__(self, comment_id=None, sender_id=None, sender_nick=None, create_at=None, content=None,
                 extension=None):
        # 弹幕的唯一ID。
        self.comment_id = comment_id  # type: str
        # 弹幕的发送者ID标识。
        self.sender_id = sender_id  # type: str
        # 弹幕发送者的昵称。
        self.sender_nick = sender_nick  # type: str
        # 弹幕的创建时间，Unix时间戳，单位：毫秒。
        self.create_at = create_at  # type: long
        # 弹幕的内容。
        self.content = content  # type: str
        # 扩展字段。
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentResponseBodyResultCommentVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_id is not None:
            result['CommentId'] = self.comment_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.create_at is not None:
            result['CreateAt'] = self.create_at
        if self.content is not None:
            result['Content'] = self.content
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommentId') is not None:
            self.comment_id = m.get('CommentId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class SendCommentResponseBodyResult(TeaModel):
    def __init__(self, comment_vo=None):
        # 返回的弹幕数据模型。
        self.comment_vo = comment_vo  # type: SendCommentResponseBodyResultCommentVO

    def validate(self):
        if self.comment_vo:
            self.comment_vo.validate()

    def to_map(self):
        _map = super(SendCommentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_vo is not None:
            result['CommentVO'] = self.comment_vo.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommentVO') is not None:
            temp_model = SendCommentResponseBodyResultCommentVO()
            self.comment_vo = temp_model.from_map(m['CommentVO'])
        return self


class SendCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用发送直播间弹幕的返回结果。
        self.result = result  # type: SendCommentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendCommentResponseBody, self).to_map()
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
            temp_model = SendCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCommentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCommentResponse, self).to_map()
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
            temp_model = SendCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppTemplateRequest(TeaModel):
    def __init__(self, app_template_name=None, scene=None, integration_mode=None, component_list=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        # 集成方式（一体化SDK：paasSDK，样板间：standardRoom）
        self.integration_mode = integration_mode  # type: str
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
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class CreateAppTemplateShrinkRequest(TeaModel):
    def __init__(self, app_template_name=None, scene=None, integration_mode=None, component_list_shrink=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        # 集成方式（一体化SDK：paasSDK，样板间：standardRoom）
        self.integration_mode = integration_mode  # type: str
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
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.component_list_shrink is not None:
            result['ComponentList'] = self.component_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
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


class GetConferenceRequest(TeaModel):
    def __init__(self, conference_id=None):
        # 会议资源唯一标识。
        self.conference_id = conference_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class GetConferenceResponseBodyResult(TeaModel):
    def __init__(self, conference_id=None, title=None, status=None, room_id=None, user_id=None, app_id=None,
                 create_time=None):
        # 会议资源唯一标识。
        self.conference_id = conference_id  # type: str
        # 会议标题。
        self.title = title  # type: str
        # 会议状态。
        self.status = status  # type: str
        # 房间ID。
        self.room_id = room_id  # type: str
        # 创建会议用户。
        self.user_id = user_id  # type: str
        # 租户名
        self.app_id = app_id  # type: str
        # 会议创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConferenceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.title is not None:
            result['Title'] = self.title
        if self.status is not None:
            result['Status'] = self.status
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class GetConferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetConferenceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetConferenceResponseBody, self).to_map()
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
            temp_model = GetConferenceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetConferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConferenceResponse, self).to_map()
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
            temp_model = GetConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, to_user_id=None, from_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 被同意用户ID
        self.to_user_id = to_user_id  # type: str
        # 同意者用户ID
        self.from_user_id = from_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class RejectLinkMicResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectLinkMicResponseBody, self).to_map()
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


class RejectLinkMicResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RejectLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectLinkMicResponse, self).to_map()
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
            temp_model = RejectLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, status=None, integration_mode=None):
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int
        # 应用状态
        self.status = status  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str

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
        if self.status is not None:
            result['Status'] = self.status
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        return self


class ListAppsResponseBodyResultAppInfoList(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_template_id=None, app_template_name=None, app_key=None,
                 app_status=None, app_config_status=None, create_time=None, integration_mode=None, standard_room_info=None,
                 component_list=None):
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
        # 应用配置状态
        self.app_config_status = app_config_status  # type: str
        # 应用创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str
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
        if self.app_config_status is not None:
            result['AppConfigStatus'] = self.app_config_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
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
        if m.get('AppConfigStatus') is not None:
            self.app_config_status = m.get('AppConfigStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
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


class CancelBanAllCommentRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBanAllCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelBanAllCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 操作成功标识
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBanAllCommentResponseBody, self).to_map()
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


class CancelBanAllCommentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelBanAllCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelBanAllCommentResponse, self).to_map()
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
            temp_model = CancelBanAllCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConferenceUsersRequest(TeaModel):
    def __init__(self, conference_id=None, page_number=None, page_size=None):
        # 会议唯一标识符
        self.conference_id = conference_id  # type: str
        # 查询页码，从第1页开始。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大显示个数为100。
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConferenceUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListConferenceUsersResponseBodyResultConferenceUserList(TeaModel):
    def __init__(self, user_id=None, status=None):
        # 用户ID。
        self.user_id = user_id  # type: str
        # 用户状态。
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConferenceUsersResponseBodyResultConferenceUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConferenceUsersResponseBodyResult(TeaModel):
    def __init__(self, conference_user_list=None, has_more=None, total_count=None, page_total=None):
        # 会议用户列表。
        self.conference_user_list = conference_user_list  # type: list[ListConferenceUsersResponseBodyResultConferenceUserList]
        # 是否还有数据
        self.has_more = has_more  # type: bool
        # 总条目数
        self.total_count = total_count  # type: int
        # 总页数
        self.page_total = page_total  # type: int

    def validate(self):
        if self.conference_user_list:
            for k in self.conference_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConferenceUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConferenceUserList'] = []
        if self.conference_user_list is not None:
            for k in self.conference_user_list:
                result['ConferenceUserList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conference_user_list = []
        if m.get('ConferenceUserList') is not None:
            for k in m.get('ConferenceUserList'):
                temp_model = ListConferenceUsersResponseBodyResultConferenceUserList()
                self.conference_user_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        return self


class ListConferenceUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: ListConferenceUsersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListConferenceUsersResponseBody, self).to_map()
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
            temp_model = ListConferenceUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListConferenceUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConferenceUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConferenceUsersResponse, self).to_map()
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
            temp_model = ListConferenceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBanCommentRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None, ban_comment_user=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str
        # 取消禁言的用户唯一标识
        self.ban_comment_user = ban_comment_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBanCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        return self


class CancelBanCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 操作成功标识
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBanCommentResponseBody, self).to_map()
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


class CancelBanCommentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelBanCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelBanCommentResponse, self).to_map()
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
            temp_model = CancelBanCommentResponseBody()
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
                 component_list=None, create_time=None, sdk_info=None, config_list=None, scene=None, integration_mode=None,
                 standard_room_info=None):
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
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str

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
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
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
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
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


class ListComponentsResponseBodyResultSceneListComponentCategoryList(TeaModel):
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
        _map = super(ListComponentsResponseBodyResultSceneListComponentCategoryList, self).to_map()
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


class ListComponentsResponseBodyResultSceneListComponentCategory(TeaModel):
    def __init__(self, type=None, list=None):
        # 组件类别
        self.type = type  # type: str
        # 类别下的组件列表
        self.list = list  # type: list[ListComponentsResponseBodyResultSceneListComponentCategoryList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultSceneListComponentCategory, self).to_map()
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
                temp_model = ListComponentsResponseBodyResultSceneListComponentCategoryList()
                self.list.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBodyResultSceneList(TeaModel):
    def __init__(self, scene=None, component_category=None):
        # 场景类别
        self.scene = scene  # type: str
        # 组件信息
        self.component_category = component_category  # type: list[ListComponentsResponseBodyResultSceneListComponentCategory]

    def validate(self):
        if self.component_category:
            for k in self.component_category:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultSceneList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene
        result['ComponentCategory'] = []
        if self.component_category is not None:
            for k in self.component_category:
                result['ComponentCategory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        self.component_category = []
        if m.get('ComponentCategory') is not None:
            for k in m.get('ComponentCategory'):
                temp_model = ListComponentsResponseBodyResultSceneListComponentCategory()
                self.component_category.append(temp_model.from_map(k))
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


class ListComponentsResponseBodyResult(TeaModel):
    def __init__(self, config_group=None, scene_list=None, component_category=None):
        # 配置信息
        self.config_group = config_group  # type: list[ListComponentsResponseBodyResultConfigGroup]
        # 场景列表
        self.scene_list = scene_list  # type: list[ListComponentsResponseBodyResultSceneList]
        # 组件信息
        self.component_category = component_category  # type: list[ListComponentsResponseBodyResultComponentCategory]

    def validate(self):
        if self.config_group:
            for k in self.config_group:
                if k:
                    k.validate()
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()
        if self.component_category:
            for k in self.component_category:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigGroup'] = []
        if self.config_group is not None:
            for k in self.config_group:
                result['ConfigGroup'].append(k.to_map() if k else None)
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
        result['ComponentCategory'] = []
        if self.component_category is not None:
            for k in self.component_category:
                result['ComponentCategory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_group = []
        if m.get('ConfigGroup') is not None:
            for k in m.get('ConfigGroup'):
                temp_model = ListComponentsResponseBodyResultConfigGroup()
                self.config_group.append(temp_model.from_map(k))
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = ListComponentsResponseBodyResultSceneList()
                self.scene_list.append(temp_model.from_map(k))
        self.component_category = []
        if m.get('ComponentCategory') is not None:
            for k in m.get('ComponentCategory'):
                temp_model = ListComponentsResponseBodyResultComponentCategory()
                self.component_category.append(temp_model.from_map(k))
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


class ApplyLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 申请连麦用户
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ApplyLinkMicResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyLinkMicResponseBody, self).to_map()
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


class ApplyLinkMicResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyLinkMicResponse, self).to_map()
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
            temp_model = ApplyLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelApplyLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 申请连麦用户
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelApplyLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelApplyLinkMicResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelApplyLinkMicResponseBody, self).to_map()
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


class CancelApplyLinkMicResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelApplyLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelApplyLinkMicResponse, self).to_map()
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
            temp_model = CancelApplyLinkMicResponseBody()
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
    def __init__(self, app_name=None, app_template_id=None, app_template_name=None, app_status=None,
                 app_config_status=None, app_key=None, create_time=None, integration_mode=None, standard_room_info=None,
                 component_list=None):
        # 应用名称
        self.app_name = app_name  # type: str
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str
        # 应用配置状态
        self.app_config_status = app_config_status  # type: str
        # 应用Key
        self.app_key = app_key  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str
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
        if self.app_config_status is not None:
            result['AppConfigStatus'] = self.app_config_status
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
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
        if m.get('AppConfigStatus') is not None:
            self.app_config_status = m.get('AppConfigStatus')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
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


class SendCustomMessageToUsersRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, body=None, receiver_list=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 消息体内容。
        self.body = body  # type: str
        # 消息指定的接收人ID列表。
        self.receiver_list = receiver_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.body is not None:
            result['Body'] = self.body
        if self.receiver_list is not None:
            result['ReceiverList'] = self.receiver_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ReceiverList') is not None:
            self.receiver_list = m.get('ReceiverList')
        return self


class SendCustomMessageToUsersResponseBodyResult(TeaModel):
    def __init__(self, message_id=None):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
        self.message_id = message_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToUsersResponseBodyResult, self).to_map()
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


class SendCustomMessageToUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: SendCustomMessageToUsersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SendCustomMessageToUsersResponseBody, self).to_map()
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
            temp_model = SendCustomMessageToUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCustomMessageToUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCustomMessageToUsersResponse, self).to_map()
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
            temp_model = SendCustomMessageToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BanAllCommentRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BanAllCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BanAllCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 操作成功标识
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BanAllCommentResponseBody, self).to_map()
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


class BanAllCommentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BanAllCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BanAllCommentResponse, self).to_map()
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
            temp_model = BanAllCommentResponseBody()
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
                 user_id=None, code_level=None, play_url_info_list=None, cover_url=None, user_define_field=None):
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
        # 封面图片
        self.cover_url = cover_url  # type: str
        # 用户自定义数据存储
        self.user_define_field = user_define_field  # type: str

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
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.user_define_field is not None:
            result['UserDefineField'] = self.user_define_field
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
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('UserDefineField') is not None:
            self.user_define_field = m.get('UserDefineField')
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


class CreateRoomShrinkRequest(TeaModel):
    def __init__(self, app_id=None, template_id=None, room_id=None, title=None, notice=None, room_owner_id=None,
                 extension_shrink=None):
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
        self.extension_shrink = extension_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomShrinkRequest, self).to_map()
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
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
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
            self.extension_shrink = m.get('Extension')
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


class UpdateConferenceRequest(TeaModel):
    def __init__(self, conference_id=None, title=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 会议标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateConferenceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConferenceResponseBody, self).to_map()
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


class UpdateConferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConferenceResponse, self).to_map()
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
            temp_model = UpdateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


