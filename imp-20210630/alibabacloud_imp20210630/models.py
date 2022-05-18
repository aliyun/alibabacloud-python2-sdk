# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddMemberRequest(TeaModel):
    def __init__(self, conference_id=None, from_user_id=None, to_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 邀请者用户ID
        self.from_user_id = from_user_id  # type: str
        # 被邀请用户ID
        self.to_user_id = to_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgreeLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, from_user_id=None, to_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 同意者用户ID
        self.from_user_id = from_user_id  # type: str
        # 被同意用户ID
        self.to_user_id = to_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgreeLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AgreeLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AgreeLinkMicResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ApplyLinkMicResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BanAllCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BanAllCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BanCommentRequest(TeaModel):
    def __init__(self, app_id=None, ban_comment_time=None, ban_comment_user=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 禁言时长（秒）
        self.ban_comment_time = ban_comment_time  # type: long
        # 被禁言的用户在房间内的唯一标识
        self.ban_comment_user = ban_comment_user  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BanCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ban_comment_time is not None:
            result['BanCommentTime'] = self.ban_comment_time
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BanCommentTime') is not None:
            self.ban_comment_time = m.get('BanCommentTime')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BanCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BanCommentResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelApplyLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelApplyLinkMicResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelBanAllCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelBanAllCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBanCommentRequest(TeaModel):
    def __init__(self, app_id=None, ban_comment_user=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 取消禁言的用户唯一标识
        self.ban_comment_user = ban_comment_user  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 用户在房间内的唯一标识
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBanCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ban_comment_user is not None:
            result['BanCommentUser'] = self.ban_comment_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BanCommentUser') is not None:
            self.ban_comment_user = m.get('BanCommentUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelBanCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelBanCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelUserAdminRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id  # type: str
        # 用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUserAdminRequest, self).to_map()
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


class CancelUserAdminResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUserAdminResponseBody, self).to_map()
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


class CancelUserAdminResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelUserAdminResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelUserAdminResponse, self).to_map()
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
            temp_model = CancelUserAdminResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class CreateAppTemplateRequest(TeaModel):
    def __init__(self, app_template_name=None, component_list=None, integration_mode=None, scene=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]
        # 集成方式（一体化SDK：paasSDK，样板间：standardRoom）
        self.integration_mode = integration_mode  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str

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
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class CreateAppTemplateShrinkRequest(TeaModel):
    def __init__(self, app_template_name=None, component_list_shrink=None, integration_mode=None, scene=None):
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list_shrink = component_list_shrink  # type: str
        # 集成方式（一体化SDK：paasSDK，样板间：standardRoom）
        self.integration_mode = integration_mode  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str

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
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list_shrink = m.get('ComponentList')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClassRequest(TeaModel):
    def __init__(self, app_id=None, create_nickname=None, create_user_id=None, title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 创建人用户昵称。
        self.create_nickname = create_nickname  # type: str
        # 创建人用户ID。
        self.create_user_id = create_user_id  # type: str
        # 课堂标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateClassResponseBodyResult(TeaModel):
    def __init__(self, class_id=None, conf_id=None, create_nickname=None, create_user_id=None, live_id=None,
                 room_id=None, status=None, title=None, whiteboard_id=None, whiteboard_record_id=None):
        # 课堂唯一标识。
        self.class_id = class_id  # type: str
        # 连麦会议唯一标识。
        self.conf_id = conf_id  # type: str
        # 创建人昵称。
        self.create_nickname = create_nickname  # type: str
        # 创建人ID。
        self.create_user_id = create_user_id  # type: str
        # 直播的唯一标识ID。
        self.live_id = live_id  # type: str
        # 房间ID
        self.room_id = room_id  # type: str
        # 课堂状态，0:未开始 1:上课中 2:已下课。
        self.status = status  # type: int
        # 课堂标题。
        self.title = title  # type: str
        # 白板ID
        self.whiteboard_id = whiteboard_id  # type: str
        # 白板录制ID
        self.whiteboard_record_id = whiteboard_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClassResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class CreateClassResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: CreateClassResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateClassResponseBody, self).to_map()
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
            temp_model = CreateClassResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateClassResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClassResponse, self).to_map()
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
            temp_model = CreateClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConferenceRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, title=None, user_id=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id  # type: str
        # 会议标题，支持中英文，最大长度256位。
        self.title = title  # type: str
        # 创建会议用户。
        self.user_id = user_id  # type: str

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
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRequest(TeaModel):
    def __init__(self, anchor_id=None, app_id=None, code_level=None, introduction=None, live_id=None, room_id=None,
                 title=None, user_id=None):
        # 主播ID，支持中英文，最大长度128位，缺省时主播为当前创建直播用户。
        self.anchor_id = anchor_id  # type: str
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 直播推流码率，缺省时默认为3。取值：  -1：流畅lld。 1：标清lsd。 2：高清lhd。 3：超清lud。
        self.code_level = code_level  # type: int
        # 直播简介，支持中英文，最大长度2048位。
        self.introduction = introduction  # type: str
        # 直播资源的唯一标识ID，缺省时系统自动生成36位随机uuid字符串。
        self.live_id = live_id  # type: str
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id  # type: str
        # 直播标题，支持中英文，最大长度256位。
        self.title = title  # type: str
        # 创建直播用户。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRoomRequest(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, cover_url=None, extension=None, notice=None,
                 title=None, user_id=None):
        # 主播id，仅支持英文和数字，最大长度36位。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 封面，支持图片地址链接格式
        self.cover_url = cover_url  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。最大支持4096个字节。
        self.extension = extension  # type: dict[str, str]
        # 公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateLiveRoomShrinkRequest(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, cover_url=None, extension_shrink=None,
                 notice=None, title=None, user_id=None):
        # 主播id，仅支持英文和数字，最大长度36位。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 封面，支持图片地址链接格式
        self.cover_url = cover_url  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。最大支持4096个字节。
        self.extension_shrink = extension_shrink  # type: str
        # 公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateLiveRoomResponseBodyResultArtcInfo(TeaModel):
    def __init__(self, artc_h5url=None, artc_url=None):
        # RTS转码流地址，推荐web端使用。
        self.artc_h5url = artc_h5url  # type: str
        # RTS原码流地址，推荐移动端使用。
        self.artc_url = artc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRoomResponseBodyResultArtcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
        return self


class CreateLiveRoomResponseBodyResultPluginInstanceInfoList(TeaModel):
    def __init__(self, create_time=None, extension=None, plugin_id=None, plugin_type=None):
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLiveRoomResponseBodyResultPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class CreateLiveRoomResponseBodyResult(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, artc_info=None, chat_id=None, cover_url=None,
                 extension=None, hls_url=None, live_id=None, live_url=None, notice=None, playback_url=None,
                 plugin_instance_info_list=None, push_url=None, room_id=None, title=None):
        # 主播ID。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用ID。
        self.app_id = app_id  # type: str
        # RTS低延迟播流信息。
        self.artc_info = artc_info  # type: CreateLiveRoomResponseBodyResultArtcInfo
        # 聊天ID。
        self.chat_id = chat_id  # type: str
        # 封面。
        self.cover_url = cover_url  # type: str
        # 直播拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 原画HLS播放地址。
        self.hls_url = hls_url  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 直播拉流地址。
        self.live_url = live_url  # type: str
        # 公告。
        self.notice = notice  # type: str
        # 直播回放地址。
        self.playback_url = playback_url  # type: str
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[CreateLiveRoomResponseBodyResultPluginInstanceInfoList]
        # 直播推流地址。
        self.push_url = push_url  # type: str
        # 房间ID。
        self.room_id = room_id  # type: str
        # 标题。
        self.title = title  # type: str

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLiveRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = CreateLiveRoomResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = CreateLiveRoomResponseBodyResultPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: CreateLiveRoomResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateLiveRoomResponseBody, self).to_map()
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
            temp_model = CreateLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLiveRoomResponse, self).to_map()
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
            temp_model = CreateLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequest(TeaModel):
    def __init__(self, app_id=None, extension=None, notice=None, room_id=None, room_owner_id=None, template_id=None,
                 title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension  # type: dict[str, str]
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 房间模板唯一标识，当前支持的取值：default，传空默认为default。
        self.template_id = template_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateRoomShrinkRequest(TeaModel):
    def __init__(self, app_id=None, extension_shrink=None, notice=None, room_id=None, room_owner_id=None,
                 template_id=None, title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension_shrink = extension_shrink  # type: str
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 房间模板唯一标识，当前支持的取值：default，传空默认为default。
        self.template_id = template_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSensitiveWordRequest(TeaModel):
    def __init__(self, app_id=None, word_list=None):
        # 用户的应用ID，在控制台创建应用时生成。包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        self.word_list = word_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSensitiveWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class CreateSensitiveWordShrinkRequest(TeaModel):
    def __init__(self, app_id=None, word_list_shrink=None):
        # 用户的应用ID，在控制台创建应用时生成。包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        self.word_list_shrink = word_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSensitiveWordShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list_shrink is not None:
            result['WordList'] = self.word_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list_shrink = m.get('WordList')
        return self


class CreateSensitiveWordResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSensitiveWordResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSensitiveWordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用发送直播间弹幕的返回结果。
        self.result = result  # type: CreateSensitiveWordResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateSensitiveWordResponseBody, self).to_map()
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
            temp_model = CreateSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateSensitiveWordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSensitiveWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSensitiveWordResponse, self).to_map()
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
            temp_model = CreateSensitiveWordResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClassRequest(TeaModel):
    def __init__(self, app_id=None, class_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 课堂唯一标识。
        self.class_id = class_id  # type: str
        # 操作人用户ID，仅支持中英文数字，下划线，中划线，1~36个字符。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteClassResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClassResponseBody, self).to_map()
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


class DeleteClassResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClassResponse, self).to_map()
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
            temp_model = DeleteClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommentRequest(TeaModel):
    def __init__(self, app_id=None, comment_id_list=None, room_id=None, user_id=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 需要删除的弹幕id列表
        self.comment_id_list = comment_id_list  # type: list[str]
        # 直播间唯一标识，在调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 删除的操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.comment_id_list is not None:
            result['CommentIdList'] = self.comment_id_list
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommentIdList') is not None:
            self.comment_id_list = m.get('CommentIdList')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteCommentResponseBodyResult(TeaModel):
    def __init__(self, delete_result=None):
        # 删除的结果
        self.delete_result = delete_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        return self


class DeleteCommentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用删除直播间弹幕的返回结果。
        self.result = result  # type: DeleteCommentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteCommentResponseBody, self).to_map()
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
            temp_model = DeleteCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteCommentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCommentResponse, self).to_map()
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
            temp_model = DeleteCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConferenceRequest(TeaModel):
    def __init__(self, app_id=None, conference_id=None, room_id=None, user_id=None):
        # 租户名
        self.app_id = app_id  # type: str
        # 会议资源的唯一标识ID
        self.conference_id = conference_id  # type: str
        # 房间ID，最大长度36位
        self.room_id = room_id  # type: str
        # 创建会议用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteConferenceResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRoomRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLiveRoomResponseBody, self).to_map()
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


class DeleteLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLiveRoomResponse, self).to_map()
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
            temp_model = DeleteLiveRoomResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSensitiveWordRequest(TeaModel):
    def __init__(self, app_id=None, word_list=None):
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.app_id = app_id  # type: str
        self.word_list = word_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSensitiveWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class DeleteSensitiveWordShrinkRequest(TeaModel):
    def __init__(self, app_id=None, word_list_shrink=None):
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.app_id = app_id  # type: str
        self.word_list_shrink = word_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSensitiveWordShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.word_list_shrink is not None:
            result['WordList'] = self.word_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WordList') is not None:
            self.word_list_shrink = m.get('WordList')
        return self


class DeleteSensitiveWordResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSensitiveWordResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSensitiveWordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用发送直播间弹幕的返回结果。
        self.result = result  # type: DeleteSensitiveWordResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteSensitiveWordResponseBody, self).to_map()
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
            temp_model = DeleteSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteSensitiveWordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSensitiveWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSensitiveWordResponse, self).to_map()
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
            temp_model = DeleteSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterImpPlayBackTimeByLiveIdRequest(TeaModel):
    def __init__(self, app_id=None, end_ts=None, live_id=None, start_ts=None):
        self.app_id = app_id  # type: str
        self.end_ts = end_ts  # type: long
        self.live_id = live_id  # type: str
        self.start_ts = start_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMeterImpPlayBackTimeByLiveIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData(TeaModel):
    def __init__(self, watch_time=None):
        self.watch_time = watch_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watch_time is not None:
            result['WatchTime'] = self.watch_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatchTime') is not None:
            self.watch_time = m.get('WatchTime')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData]
        # Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMeterImpPlayBackTimeByLiveIdResponseBody, self).to_map()
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
                temp_model = DescribeMeterImpPlayBackTimeByLiveIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterImpPlayBackTimeByLiveIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMeterImpPlayBackTimeByLiveIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMeterImpPlayBackTimeByLiveIdResponse, self).to_map()
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
            temp_model = DescribeMeterImpPlayBackTimeByLiveIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None):
        self.app_id = app_id  # type: str
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMeterImpWatchLiveTimeByLiveIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData(TeaModel):
    def __init__(self, watch_time_in_latency=None, watch_time_in_low_latency=None):
        self.watch_time_in_latency = watch_time_in_latency  # type: long
        self.watch_time_in_low_latency = watch_time_in_low_latency  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watch_time_in_latency is not None:
            result['WatchTimeInLatency'] = self.watch_time_in_latency
        if self.watch_time_in_low_latency is not None:
            result['WatchTimeInLowLatency'] = self.watch_time_in_low_latency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatchTimeInLatency') is not None:
            self.watch_time_in_latency = m.get('WatchTimeInLatency')
        if m.get('WatchTimeInLowLatency') is not None:
            self.watch_time_in_low_latency = m.get('WatchTimeInLowLatency')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData]
        # Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMeterImpWatchLiveTimeByLiveIdResponseBody, self).to_map()
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
                temp_model = DescribeMeterImpWatchLiveTimeByLiveIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeterImpWatchLiveTimeByLiveIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMeterImpWatchLiveTimeByLiveIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMeterImpWatchLiveTimeByLiveIdResponse, self).to_map()
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
            temp_model = DescribeMeterImpWatchLiveTimeByLiveIdResponseBody()
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
    def __init__(self, app_config_status=None, app_key=None, app_name=None, app_status=None, app_template_id=None,
                 app_template_name=None, component_list=None, create_time=None, integration_mode=None, standard_room_info=None):
        # 应用配置状态
        self.app_config_status = app_config_status  # type: str
        # 应用Key
        self.app_key = app_key  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表。
        self.component_list = component_list  # type: list[str]
        # 创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_config_status is not None:
            result['AppConfigStatus'] = self.app_config_status
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppConfigStatus') is not None:
            self.app_config_status = m.get('AppConfigStatus')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class GetAppTemplateResponseBodyResultApps(TeaModel):
    def __init__(self, app_id=None, app_key=None, app_name=None, app_status=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用的Key
        self.app_key = app_key  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppTemplateResponseBodyResultApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
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
    def __init__(self, app_template_creator=None, app_template_name=None, apps=None, component_list=None,
                 config_list=None, create_time=None, integration_mode=None, scene=None, sdk_info=None, standard_room_info=None,
                 status=None):
        # 应用模板创建者
        self.app_template_creator = app_template_creator  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用列表信息
        self.apps = apps  # type: list[GetAppTemplateResponseBodyResultApps]
        # 组件列表
        self.component_list = component_list  # type: list[str]
        # 配置列表
        self.config_list = config_list  # type: list[GetAppTemplateResponseBodyResultConfigList]
        # 创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        self.sdk_info = sdk_info  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str
        # 应用模板使用状态
        self.status = status  # type: str

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = GetAppTemplateResponseBodyResultApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = GetAppTemplateResponseBodyResultConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(self, app_id=None, app_key=None, device_id=None, user_id=None):
        # 用户的应用ID，在控制台创建应用时生成
        self.app_id = app_id  # type: str
        # 终端设备类型,通过控制台创建和查询
        self.app_key = app_key  # type: str
        # 终端设备ID
        self.device_id = device_id  # type: str
        # 用户UserId,在AppId下单独唯一
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAuthTokenResponseBodyResult(TeaModel):
    def __init__(self, access_token=None, access_token_expired_time=None, refresh_token=None):
        # 用于长连接建连的token
        self.access_token = access_token  # type: str
        # 登录token过期时间(毫秒)
        self.access_token_expired_time = access_token_expired_time  # type: long
        # 更新Token，若AccessToken过期，则可以使用RefreshToken再次获取新Token
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuthTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClassDetailRequest(TeaModel):
    def __init__(self, app_id=None, class_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 课堂唯一标识，由调用CreateClass返回。
        self.class_id = class_id  # type: str
        # 操作人用户ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClassDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetClassDetailResponseBodyResult(TeaModel):
    def __init__(self, class_id=None, conf_id=None, create_nickname=None, create_user_id=None, end_time=None,
                 live_id=None, room_id=None, start_time=None, status=None, title=None, whiteboard_id=None,
                 whiteboard_record_id=None):
        # 课堂唯一标识，由调用CreateClass返回。
        self.class_id = class_id  # type: str
        # 连麦会议唯一标识。
        self.conf_id = conf_id  # type: str
        # 创建人昵称。
        self.create_nickname = create_nickname  # type: str
        # 创建人ID。
        self.create_user_id = create_user_id  # type: str
        # 下课时间戳，毫秒。
        self.end_time = end_time  # type: long
        # 直播的唯一标识ID。
        self.live_id = live_id  # type: str
        # 房间ID
        self.room_id = room_id  # type: str
        # 开始上课时间戳，毫秒。
        self.start_time = start_time  # type: long
        # 课堂状态，0:未开始 1:上课中 2:已下课。
        self.status = status  # type: int
        # 课堂标题。
        self.title = title  # type: str
        # 白板ID
        self.whiteboard_id = whiteboard_id  # type: str
        # 白板录制ID
        self.whiteboard_record_id = whiteboard_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClassDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class GetClassDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: GetClassDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetClassDetailResponseBody, self).to_map()
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
            temp_model = GetClassDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClassDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClassDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClassDetailResponse, self).to_map()
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
            temp_model = GetClassDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClassRecordRequest(TeaModel):
    def __init__(self, app_id=None, class_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 课程唯一标识，由调用CreateClass返回。
        self.class_id = class_id  # type: str
        # 操作人用户ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClassRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetClassRecordResponseBodyResult(TeaModel):
    def __init__(self, playback_url_map=None):
        self.playback_url_map = playback_url_map  # type: dict[str, list[str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClassRecordResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playback_url_map is not None:
            result['PlaybackUrlMap'] = self.playback_url_map
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybackUrlMap') is not None:
            self.playback_url_map = m.get('PlaybackUrlMap')
        return self


class GetClassRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: GetClassRecordResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetClassRecordResponseBody, self).to_map()
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
            temp_model = GetClassRecordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClassRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClassRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClassRecordResponse, self).to_map()
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
            temp_model = GetClassRecordResponseBody()
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
    def __init__(self, app_id=None, conference_id=None, create_time=None, playback_url=None, room_id=None,
                 status=None, title=None, user_id=None):
        # 租户名
        self.app_id = app_id  # type: str
        # 会议资源唯一标识。
        self.conference_id = conference_id  # type: str
        # 会议创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 录制回放地址，m3u8格式，会议结束后10秒才会生成。
        self.playback_url = playback_url  # type: str
        # 房间ID。
        self.room_id = room_id  # type: str
        # 会议状态。
        self.status = status  # type: str
        # 会议标题。
        self.title = title  # type: str
        # 创建会议用户。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConferenceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetConferenceResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainOwnerVerifyContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetDomainOwnerVerifyContentResponseBody()
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


class GetLiveResponseBodyResultArtcInfo(TeaModel):
    def __init__(self, artc_h5url=None, artc_url=None):
        # 原画转码地址
        self.artc_h5url = artc_h5url  # type: str
        # 源码地址
        self.artc_url = artc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveResponseBodyResultArtcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
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
    def __init__(self, anchor_id=None, app_id=None, artc_info=None, code_level=None, cover_url=None,
                 create_time=None, duration=None, end_time=None, hls_url=None, introduction=None, live_id=None, live_url=None,
                 play_url_info_list=None, playback_url=None, push_url=None, room_id=None, status=None, title=None,
                 user_define_field=None, user_id=None):
        # 主播ID
        self.anchor_id = anchor_id  # type: str
        # 租户名
        self.app_id = app_id  # type: str
        # rts播流信息
        self.artc_info = artc_info  # type: GetLiveResponseBodyResultArtcInfo
        # 直播推送分辨率 -1:lld 1:lsd 2:lhd 3:lud
        self.code_level = code_level  # type: int
        # 封面图片
        self.cover_url = cover_url  # type: str
        # 直播创建时间（毫秒ms）
        self.create_time = create_time  # type: long
        # 直播持续时间（毫秒ms）
        self.duration = duration  # type: long
        # 直播结束时间（毫秒ms）
        self.end_time = end_time  # type: long
        # hls播放地址
        self.hls_url = hls_url  # type: str
        # 直播简介
        self.introduction = introduction  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 直播拉流地址
        self.live_url = live_url  # type: str
        # 多分辨率多协议播放信息
        self.play_url_info_list = play_url_info_list  # type: list[GetLiveResponseBodyResultPlayUrlInfoList]
        # 直播回放地址
        self.playback_url = playback_url  # type: str
        # 直播推流地址
        self.push_url = push_url  # type: str
        # 房间id
        self.room_id = room_id  # type: str
        # 直播状态：Created-已创建，未开播，Living-直播中，End-直播结束
        self.status = status  # type: str
        # 直播标题
        self.title = title  # type: str
        # 用户自定义数据存储
        self.user_define_field = user_define_field  # type: str
        # 创建直播用户
        self.user_id = user_id  # type: str

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        result['PlayUrlInfoList'] = []
        if self.play_url_info_list is not None:
            for k in self.play_url_info_list:
                result['PlayUrlInfoList'].append(k.to_map() if k else None)
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_define_field is not None:
            result['UserDefineField'] = self.user_define_field
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = GetLiveResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        self.play_url_info_list = []
        if m.get('PlayUrlInfoList') is not None:
            for k in m.get('PlayUrlInfoList'):
                temp_model = GetLiveResponseBodyResultPlayUrlInfoList()
                self.play_url_info_list.append(temp_model.from_map(k))
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserDefineField') is not None:
            self.user_define_field = m.get('UserDefineField')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetLiveResponseBody()
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
    def __init__(self, cname=None, domain=None, status=None):
        # 直播域名CNAME
        self.cname = cname  # type: str
        # 直播域名
        self.domain = domain  # type: str
        # 直播域名状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveDomainStatusResponseBodyResultLiveDomainInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveDomainStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetLiveDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRecordRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播唯一标识，由调用CreateLiveRoom返回。
        self.live_id = live_id  # type: str
        # 操作人用户ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetLiveRecordResponseBodyResult(TeaModel):
    def __init__(self, playback_url_map=None):
        self.playback_url_map = playback_url_map  # type: dict[str, list[str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRecordResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playback_url_map is not None:
            result['PlaybackUrlMap'] = self.playback_url_map
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybackUrlMap') is not None:
            self.playback_url_map = m.get('PlaybackUrlMap')
        return self


class GetLiveRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
        self.result = result  # type: GetLiveRecordResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveRecordResponseBody, self).to_map()
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
            temp_model = GetLiveRecordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveRecordResponse, self).to_map()
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
            temp_model = GetLiveRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveRoomResponseBodyResultArtcInfo(TeaModel):
    def __init__(self, artc_h5url=None, artc_url=None):
        # RTS转码流地址，推荐web端使用。
        self.artc_h5url = artc_h5url  # type: str
        # RTS原码流地址，推荐移动端使用。
        self.artc_url = artc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomResponseBodyResultArtcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artc_h5url is not None:
            result['ArtcH5Url'] = self.artc_h5url
        if self.artc_url is not None:
            result['ArtcUrl'] = self.artc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtcH5Url') is not None:
            self.artc_h5url = m.get('ArtcH5Url')
        if m.get('ArtcUrl') is not None:
            self.artc_url = m.get('ArtcUrl')
        return self


class GetLiveRoomResponseBodyResultPluginInstanceInfoList(TeaModel):
    def __init__(self, create_time=None, extension=None, plugin_id=None, plugin_type=None):
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomResponseBodyResultPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class GetLiveRoomResponseBodyResult(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, artc_info=None, chat_id=None, cover_url=None,
                 create_time=None, end_time=None, extension=None, hls_url=None, hls_url_https=None, live_id=None, live_url=None,
                 live_url_https=None, notice=None, online_count=None, playback_url=None, playback_url_https=None,
                 plugin_instance_info_list=None, push_url=None, pv=None, room_id=None, rtmp_url=None, start_time=None, status=None, title=None,
                 uv=None):
        # 主播ID。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称
        self.anchor_nick = anchor_nick  # type: str
        # 应用ID。
        self.app_id = app_id  # type: str
        # RTS低延迟播流信息。
        self.artc_info = artc_info  # type: GetLiveRoomResponseBodyResultArtcInfo
        # 聊天ID。
        self.chat_id = chat_id  # type: str
        # 封面。
        self.cover_url = cover_url  # type: str
        # 直播创建时间，单位：毫秒。
        self.create_time = create_time  # type: long
        # 直播结束时间，单位：毫秒。
        self.end_time = end_time  # type: long
        # 直播拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 原画HLS播放地址。
        self.hls_url = hls_url  # type: str
        # https协议的原画HLS播放地址。
        self.hls_url_https = hls_url_https  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 直播拉流地址。
        self.live_url = live_url  # type: str
        # https协议的直播拉流地址。
        self.live_url_https = live_url_https  # type: str
        # 公告。
        self.notice = notice  # type: str
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 直播回放地址。
        self.playback_url = playback_url  # type: str
        # https协议的直播回放地址
        self.playback_url_https = playback_url_https  # type: str
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[GetLiveRoomResponseBodyResultPluginInstanceInfoList]
        # 直播推流地址。
        self.push_url = push_url  # type: str
        # 访问用户人次。
        self.pv = pv  # type: long
        # 房间ID。
        self.room_id = room_id  # type: str
        # rtmp协议的播放地址
        self.rtmp_url = rtmp_url  # type: str
        # 直播开始时间，单位：毫秒。
        self.start_time = start_time  # type: long
        # 直播状态，0-在播 1-下播。
        self.status = status  # type: int
        # 标题。
        self.title = title  # type: str
        # 访问用户数。
        self.uv = uv  # type: long

    def validate(self):
        if self.artc_info:
            self.artc_info.validate()
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLiveRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artc_info is not None:
            result['ArtcInfo'] = self.artc_info.to_map()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.hls_url_https is not None:
            result['HlsUrlHttps'] = self.hls_url_https
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.live_url_https is not None:
            result['LiveUrlHttps'] = self.live_url_https
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.playback_url_https is not None:
            result['PlaybackUrlHttps'] = self.playback_url_https
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtcInfo') is not None:
            temp_model = GetLiveRoomResponseBodyResultArtcInfo()
            self.artc_info = temp_model.from_map(m['ArtcInfo'])
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('HlsUrlHttps') is not None:
            self.hls_url_https = m.get('HlsUrlHttps')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('LiveUrlHttps') is not None:
            self.live_url_https = m.get('LiveUrlHttps')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('PlaybackUrlHttps') is not None:
            self.playback_url_https = m.get('PlaybackUrlHttps')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetLiveRoomResponseBodyResultPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class GetLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: GetLiveRoomResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveRoomResponseBody, self).to_map()
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
            temp_model = GetLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveRoomResponse, self).to_map()
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
            temp_model = GetLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomStatisticsRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveRoomStatisticsResponseBodyResult(TeaModel):
    def __init__(self, end_time=None, like_count=None, live_id=None, message_count=None, online_count=None, pv=None,
                 start_time=None, status=None, uv=None, watch_live_time=None):
        # 直播结束时间，单位：毫秒。
        self.end_time = end_time  # type: long
        # 点赞数。
        self.like_count = like_count  # type: long
        # 直播ID。
        self.live_id = live_id  # type: str
        # 互动消息数。
        self.message_count = message_count  # type: long
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 访问用户人次。
        self.pv = pv  # type: long
        # 直播开始时间，单位：毫秒。
        self.start_time = start_time  # type: long
        # 直播状态，0-已创建 1-直播中 2-已关闭。
        self.status = status  # type: int
        # 访问用户数。
        self.uv = uv  # type: long
        # 总观看时长，单位：毫秒。
        self.watch_live_time = watch_live_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomStatisticsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.like_count is not None:
            result['LikeCount'] = self.like_count
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')
        return self


class GetLiveRoomStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: GetLiveRoomStatisticsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveRoomStatisticsResponseBody, self).to_map()
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
            temp_model = GetLiveRoomStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveRoomStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveRoomStatisticsResponse, self).to_map()
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
            temp_model = GetLiveRoomStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRoomUserStatisticsRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, page_number=None, page_size=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number  # type: str
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomUserStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList(TeaModel):
    def __init__(self, comment_count=None, like_count=None, user_id=None, watch_live_time=None):
        self.comment_count = comment_count  # type: int
        self.like_count = like_count  # type: int
        # 用户ID。
        self.user_id = user_id  # type: str
        # 观看时长，单位：毫秒。
        self.watch_live_time = watch_live_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_count is not None:
            result['CommentCount'] = self.comment_count
        if self.like_count is not None:
            result['LikeCount'] = self.like_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watch_live_time is not None:
            result['WatchLiveTime'] = self.watch_live_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommentCount') is not None:
            self.comment_count = m.get('CommentCount')
        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatchLiveTime') is not None:
            self.watch_live_time = m.get('WatchLiveTime')
        return self


class GetLiveRoomUserStatisticsResponseBodyResult(TeaModel):
    def __init__(self, has_more=None, live_id=None, page_total=None, total_count=None, user_statistics_list=None):
        # 是否还有下一页。
        self.has_more = has_more  # type: bool
        # 直播ID。
        self.live_id = live_id  # type: str
        # 用户总页数。
        self.page_total = page_total  # type: int
        # 用户总数
        self.total_count = total_count  # type: int
        # 用户观看数据列表。
        self.user_statistics_list = user_statistics_list  # type: list[GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList]

    def validate(self):
        if self.user_statistics_list:
            for k in self.user_statistics_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLiveRoomUserStatisticsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserStatisticsList'] = []
        if self.user_statistics_list is not None:
            for k in self.user_statistics_list:
                result['UserStatisticsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_statistics_list = []
        if m.get('UserStatisticsList') is not None:
            for k in m.get('UserStatisticsList'):
                temp_model = GetLiveRoomUserStatisticsResponseBodyResultUserStatisticsList()
                self.user_statistics_list.append(temp_model.from_map(k))
        return self


class GetLiveRoomUserStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: GetLiveRoomUserStatisticsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLiveRoomUserStatisticsResponseBody, self).to_map()
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
            temp_model = GetLiveRoomUserStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveRoomUserStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLiveRoomUserStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveRoomUserStatisticsResponse, self).to_map()
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
            temp_model = GetLiveRoomUserStatisticsResponseBody()
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
    def __init__(self, create_time=None, extension=None, plugin_id=None, plugin_type=None):
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class GetRoomResponseBodyResultRoomInfo(TeaModel):
    def __init__(self, admin_id_list=None, app_id=None, create_time=None, extension=None, notice=None,
                 online_count=None, plugin_instance_info_list=None, pv=None, room_id=None, room_owner_id=None, template_id=None,
                 title=None, uv=None):
        # 管理员ID列表。
        self.admin_id_list = admin_id_list  # type: list[str]
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 房间拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 房间公告。
        self.notice = notice  # type: str
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList]
        # 访问用户人次。
        self.pv = pv  # type: long
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房主用户id。
        self.room_owner_id = room_owner_id  # type: str
        # 创建房间使用的模板id。
        self.template_id = template_id  # type: str
        # 房间标题。
        self.title = title  # type: str
        # 访问用户数。
        self.uv = uv  # type: long

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
        if self.admin_id_list is not None:
            result['AdminIdList'] = self.admin_id_list
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdminIdList') is not None:
            self.admin_id_list = m.get('AdminIdList')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStandardRoomHttpsCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        # 证书ID
        self.certificate_id = certificate_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStandardRoomHttpsCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class GetStandardRoomHttpsCertificateResponseBodyResult(TeaModel):
    def __init__(self, certificate_name=None, create_time=None, domain_name=None, expire_time=None):
        # 证书名称
        self.certificate_name = certificate_name  # type: str
        # 证书创建时间
        self.create_time = create_time  # type: str
        # 使用证书的确切域名
        self.domain_name = domain_name  # type: str
        # 证书过期时间
        self.expire_time = expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStandardRoomHttpsCertificateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetStandardRoomHttpsCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: GetStandardRoomHttpsCertificateResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetStandardRoomHttpsCertificateResponseBody, self).to_map()
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
            temp_model = GetStandardRoomHttpsCertificateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetStandardRoomHttpsCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStandardRoomHttpsCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStandardRoomHttpsCertificateResponse, self).to_map()
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
            temp_model = GetStandardRoomHttpsCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStandardRoomJumpUrlRequest(TeaModel):
    def __init__(self, app_id=None, app_key=None, biz_id=None, biz_type=None, platform=None, user_id=None,
                 user_nick=None):
        # 用户的应用ID，在控制台创建应用时生成
        self.app_id = app_id  # type: str
        # 终端设备类型,通过控制台创建和查询
        self.app_key = app_key  # type: str
        # 资源ID：根据业务类型来定，比如直播ID，课堂ID等
        self.biz_id = biz_id  # type: str
        # 业务类型：互动直播live，互动课堂class
        self.biz_type = biz_type  # type: str
        # 平台：win, mac, android, ios, web
        self.platform = platform  # type: str
        # 用户UserId,在AppId下单独唯一
        self.user_id = user_id  # type: str
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
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStandardRoomJumpUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetStandardRoomJumpUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickRoomUserRequest(TeaModel):
    def __init__(self, app_id=None, block_time=None, kick_user=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        self.block_time = block_time  # type: long
        # 被踢出房间的用户ID。
        self.kick_user = kick_user  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id  # type: str
        # 操作人的用户ID，用于表示谁执行了踢人操作。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickRoomUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.block_time is not None:
            result['BlockTime'] = self.block_time
        if self.kick_user is not None:
            result['KickUser'] = self.kick_user
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BlockTime') is not None:
            self.block_time = m.get('BlockTime')
        if m.get('KickUser') is not None:
            self.kick_user = m.get('KickUser')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class KickRoomUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickRoomUserResponseBody, self).to_map()
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


class KickRoomUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: KickRoomUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KickRoomUserResponse, self).to_map()
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
            temp_model = KickRoomUserResponseBody()
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
    def __init__(self, app_template_creator=None, app_template_id=None, app_template_name=None,
                 component_list=None, config_list=None, create_time=None, integration_mode=None, scene=None, sdk_info=None,
                 standard_room_info=None, status=None):
        # 应用模板创建者
        self.app_template_creator = app_template_creator  # type: str
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]
        # 配置列表
        self.config_list = config_list  # type: list[ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList]
        # 创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 应用模板场景，电商business，课堂classroom
        self.scene = scene  # type: str
        # SDK信息
        self.sdk_info = sdk_info  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str
        # 应用模板使用状态
        self.status = status  # type: str

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
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppTemplatesResponseBodyResult(TeaModel):
    def __init__(self, app_template_info_list=None, page_total=None, total_count=None):
        # 应用模板信息列表
        self.app_template_info_list = app_template_info_list  # type: list[ListAppTemplatesResponseBodyResultAppTemplateInfoList]
        # 总页数
        self.page_total = page_total  # type: int
        # 总条目数
        self.total_count = total_count  # type: int

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
        result['AppTemplateInfoList'] = []
        if self.app_template_info_list is not None:
            for k in self.app_template_info_list:
                result['AppTemplateInfoList'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_template_info_list = []
        if m.get('AppTemplateInfoList') is not None:
            for k in m.get('AppTemplateInfoList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoList()
                self.app_template_info_list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
    def __init__(self, apply_link_mic_user_list=None, has_more=None, page_total=None, total_count=None):
        # 会议申请连麦用户列表。
        self.apply_link_mic_user_list = apply_link_mic_user_list  # type: list[str]
        # 是否还有下一页成员列表。
        self.has_more = has_more  # type: bool
        # 改会议的申请连麦成员总页数。
        self.page_total = page_total  # type: int
        # 该会议的申请连麦成员总数。
        self.total_count = total_count  # type: int

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
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyLinkMicUserList') is not None:
            self.apply_link_mic_user_list = m.get('ApplyLinkMicUserList')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplyLinkMicUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListApplyLinkMicUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, app_ids=None, integration_mode=None, page_number=None, page_size=None, status=None):
        # 过滤的应用id列表
        self.app_ids = app_ids  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int
        # 应用状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppsResponseBodyResultAppInfoList(TeaModel):
    def __init__(self, app_config_status=None, app_id=None, app_key=None, app_name=None, app_status=None,
                 app_template_id=None, app_template_name=None, component_list=None, create_time=None, integration_mode=None,
                 standard_room_info=None):
        # 应用配置状态
        self.app_config_status = app_config_status  # type: str
        # 应用唯一标识符
        self.app_id = app_id  # type: str
        # 应用Key
        self.app_key = app_key  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # 应用状态
        self.app_status = app_status  # type: str
        # 模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 模板名称
        self.app_template_name = app_template_name  # type: str
        # 应用组件列表
        self.component_list = component_list  # type: list[str]
        # 应用创建时间
        self.create_time = create_time  # type: str
        # 集成方式：- 一体化SDK：paasSDK - 样板间：standardRoom
        self.integration_mode = integration_mode  # type: str
        # 样板间信息
        self.standard_room_info = standard_room_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsResponseBodyResultAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_config_status is not None:
            result['AppConfigStatus'] = self.app_config_status
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_mode is not None:
            result['IntegrationMode'] = self.integration_mode
        if self.standard_room_info is not None:
            result['StandardRoomInfo'] = self.standard_room_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppConfigStatus') is not None:
            self.app_config_status = m.get('AppConfigStatus')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationMode') is not None:
            self.integration_mode = m.get('IntegrationMode')
        if m.get('StandardRoomInfo') is not None:
            self.standard_room_info = m.get('StandardRoomInfo')
        return self


class ListAppsResponseBodyResult(TeaModel):
    def __init__(self, app_info_list=None, page_total=None, total_count=None):
        # App信息列表
        self.app_info_list = app_info_list  # type: list[ListAppsResponseBodyResultAppInfoList]
        # 总页数
        self.page_total = page_total  # type: int
        # 总条目数
        self.total_count = total_count  # type: int

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
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListAppsResponseBodyResultAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ListClassesRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, status=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int
        # 课程状态，0-未开课 1-上课中 2-已下课，不传则返回所有课程。
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClassesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListClassesResponseBodyResultClassList(TeaModel):
    def __init__(self, class_id=None, conf_id=None, create_nickname=None, create_user_id=None, end_time=None,
                 live_id=None, room_id=None, start_time=None, status=None, title=None, whiteboard_id=None,
                 whiteboard_record_id=None):
        # 课堂唯一标识，由调用CreateClass返回。
        self.class_id = class_id  # type: str
        # 连麦会议唯一标识。
        self.conf_id = conf_id  # type: str
        # 创建人昵称。
        self.create_nickname = create_nickname  # type: str
        # 创建人ID。
        self.create_user_id = create_user_id  # type: str
        # 下课时间戳，毫秒。
        self.end_time = end_time  # type: long
        # 直播的唯一标识ID。
        self.live_id = live_id  # type: str
        # 房间ID
        self.room_id = room_id  # type: str
        # 开始上课时间戳，毫秒。
        self.start_time = start_time  # type: long
        # 课堂状态，0:未开始 1:上课中 2:已下课。
        self.status = status  # type: int
        # 课堂标题。
        self.title = title  # type: str
        # 白板ID
        self.whiteboard_id = whiteboard_id  # type: str
        # 白板录制ID
        self.whiteboard_record_id = whiteboard_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClassesResponseBodyResultClassList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.conf_id is not None:
            result['ConfId'] = self.conf_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id
        if self.whiteboard_record_id is not None:
            result['WhiteboardRecordId'] = self.whiteboard_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ConfId') is not None:
            self.conf_id = m.get('ConfId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')
        if m.get('WhiteboardRecordId') is not None:
            self.whiteboard_record_id = m.get('WhiteboardRecordId')
        return self


class ListClassesResponseBodyResult(TeaModel):
    def __init__(self, class_list=None, has_more=None, page_total=None, total_count=None):
        # 课程列表信息。
        self.class_list = class_list  # type: list[ListClassesResponseBodyResultClassList]
        # 是否还有下一页。
        self.has_more = has_more  # type: bool
        # 课程总页数。
        self.page_total = page_total  # type: int
        # 课程总数。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.class_list:
            for k in self.class_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClassesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassList'] = []
        if self.class_list is not None:
            for k in self.class_list:
                result['ClassList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.class_list = []
        if m.get('ClassList') is not None:
            for k in m.get('ClassList'):
                temp_model = ListClassesResponseBodyResultClassList()
                self.class_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClassesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建课程返回的结果。
        self.result = result  # type: ListClassesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListClassesResponseBody, self).to_map()
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
            temp_model = ListClassesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListClassesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClassesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClassesResponse, self).to_map()
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
            temp_model = ListClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommentsRequest(TeaModel):
    def __init__(self, app_id=None, page_num=None, page_size=None, room_id=None, sort_type=None, user_id=None):
        # 用户的应用ID，在控制台创建应用时生成。包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 查询弹幕消息列表的分页页数。应该从1开始，每次分页拉取时递增。
        self.page_num = page_num  # type: int
        # 查询弹幕消息列表的分页大小。最小不得小于1，最大不得超过100。如果超过100，会被截断为前100条。
        self.page_size = page_size  # type: int
        # 房间的唯一标识，在调用CreateRoom时返回。
        self.room_id = room_id  # type: str
        # 查询弹幕消息列表的排序方式。取值仅限0和1，其中0表示按照弹幕消息创建时间递增的顺序拉取，1表示按照弹幕消息创建时间递减的时间拉取。
        self.sort_type = sort_type  # type: int
        # 操作人用户ID，表示谁执行了查询弹幕消息列表的操作。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListCommentsResponseBodyResultCommentVOList(TeaModel):
    def __init__(self, app_id=None, comment_id=None, content=None, create_at=None, extension=None, room_id=None,
                 sender_id=None, sender_nick=None):
        # 应用ID。
        self.app_id = app_id  # type: str
        # 弹幕消息的唯一ID标识。
        self.comment_id = comment_id  # type: str
        # 弹幕消息的内容。
        self.content = content  # type: str
        # 弹幕消息的创建时间，Unix时间戳，单位：毫秒。
        self.create_at = create_at  # type: long
        # 扩展字段。
        self.extension = extension  # type: dict[str, str]
        # 房间ID。
        self.room_id = room_id  # type: str
        # 弹幕消息的发送者ID标识。
        self.sender_id = sender_id  # type: str
        # 弹幕消息发送者的昵称。
        self.sender_nick = sender_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommentsResponseBodyResultCommentVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.comment_id is not None:
            result['CommentId'] = self.comment_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_at is not None:
            result['CreateAt'] = self.create_at
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommentId') is not None:
            self.comment_id = m.get('CommentId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class ListCommentsResponseBodyResult(TeaModel):
    def __init__(self, comment_volist=None, has_more=None, page_total=None, total_count=None):
        # 弹幕消息列表。
        self.comment_volist = comment_volist  # type: list[ListCommentsResponseBodyResultCommentVOList]
        # 是否还有下一页数据。true表示还有，false表示没有。
        self.has_more = has_more  # type: bool
        # 分页查询弹幕消息列表的总页数。
        self.page_total = page_total  # type: int
        # 弹幕消息的总数。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.comment_volist:
            for k in self.comment_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommentVOList'] = []
        if self.comment_volist is not None:
            for k in self.comment_volist:
                result['CommentVOList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.comment_volist = []
        if m.get('CommentVOList') is not None:
            for k in m.get('CommentVOList'):
                temp_model = ListCommentsResponseBodyResultCommentVOList()
                self.comment_volist.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommentsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用查询弹幕消息列表的返回结果。
        self.result = result  # type: ListCommentsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListCommentsResponseBody, self).to_map()
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
            temp_model = ListCommentsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListCommentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCommentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommentsResponse, self).to_map()
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
            temp_model = ListCommentsResponseBody()
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
    def __init__(self, component_name=None, component_type=None, in_use=None):
        # 组件名称
        self.component_name = component_name  # type: str
        # 组件类型
        self.component_type = component_type  # type: str
        # 是否使用
        self.in_use = in_use  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultComponentCategoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.in_use is not None:
            result['InUse'] = self.in_use
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        return self


class ListComponentsResponseBodyResultComponentCategory(TeaModel):
    def __init__(self, list=None, type=None):
        # 类别下的组件列表
        self.list = list  # type: list[ListComponentsResponseBodyResultComponentCategoryList]
        # 组件类别
        self.type = type  # type: str

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListComponentsResponseBodyResultComponentCategoryList()
                self.list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListComponentsResponseBodyResultConfigGroup(TeaModel):
    def __init__(self, category=None, key=None, value=None):
        self.category = category  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultConfigGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListComponentsResponseBodyResultSceneListComponentCategoryList(TeaModel):
    def __init__(self, component_name=None, component_type=None, in_use=None):
        # 组件名称
        self.component_name = component_name  # type: str
        # 组件类型
        self.component_type = component_type  # type: str
        # 是否使用
        self.in_use = in_use  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyResultSceneListComponentCategoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.in_use is not None:
            result['InUse'] = self.in_use
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        return self


class ListComponentsResponseBodyResultSceneListComponentCategory(TeaModel):
    def __init__(self, list=None, type=None):
        # 类别下的组件列表
        self.list = list  # type: list[ListComponentsResponseBodyResultSceneListComponentCategoryList]
        # 组件类别
        self.type = type  # type: str

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListComponentsResponseBodyResultSceneListComponentCategoryList()
                self.list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListComponentsResponseBodyResultSceneList(TeaModel):
    def __init__(self, component_category=None, scene=None):
        # 组件信息
        self.component_category = component_category  # type: list[ListComponentsResponseBodyResultSceneListComponentCategory]
        # 场景类别
        self.scene = scene  # type: str

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
        result['ComponentCategory'] = []
        if self.component_category is not None:
            for k in self.component_category:
                result['ComponentCategory'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component_category = []
        if m.get('ComponentCategory') is not None:
            for k in m.get('ComponentCategory'):
                temp_model = ListComponentsResponseBodyResultSceneListComponentCategory()
                self.component_category.append(temp_model.from_map(k))
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ListComponentsResponseBodyResult(TeaModel):
    def __init__(self, component_category=None, config_group=None, scene_list=None):
        # 组件信息
        self.component_category = component_category  # type: list[ListComponentsResponseBodyResultComponentCategory]
        # 配置信息
        self.config_group = config_group  # type: list[ListComponentsResponseBodyResultConfigGroup]
        # 场景列表
        self.scene_list = scene_list  # type: list[ListComponentsResponseBodyResultSceneList]

    def validate(self):
        if self.component_category:
            for k in self.component_category:
                if k:
                    k.validate()
        if self.config_group:
            for k in self.config_group:
                if k:
                    k.validate()
        if self.scene_list:
            for k in self.scene_list:
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
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
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
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = ListComponentsResponseBodyResultSceneList()
                self.scene_list.append(temp_model.from_map(k))
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListComponentsResponseBody()
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
    def __init__(self, status=None, user_id=None):
        # 用户状态。
        self.status = status  # type: str
        # 用户ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConferenceUsersResponseBodyResultConferenceUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListConferenceUsersResponseBodyResult(TeaModel):
    def __init__(self, conference_user_list=None, has_more=None, page_total=None, total_count=None):
        # 会议用户列表。
        self.conference_user_list = conference_user_list  # type: list[ListConferenceUsersResponseBodyResultConferenceUserList]
        # 是否还有数据
        self.has_more = has_more  # type: bool
        # 总页数
        self.page_total = page_total  # type: int
        # 总条目数
        self.total_count = total_count  # type: int

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
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
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
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConferenceUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListConferenceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRoomsRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, status=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int
        # 直播状态，0-在播 1-下播，不传则返回所有直播。
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRoomsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLiveRoomsResponseBodyResultLiveList(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, chat_id=None, cover_url=None, extension=None,
                 live_id=None, notice=None, online_count=None, pv=None, room_id=None, status=None, title=None, uv=None):
        # 主播ID。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用ID。
        self.app_id = app_id  # type: str
        # 聊天ID。
        self.chat_id = chat_id  # type: str
        # 封面。
        self.cover_url = cover_url  # type: str
        # 直播拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 直播ID。
        self.live_id = live_id  # type: str
        # 公告。
        self.notice = notice  # type: str
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 访问用户人次。
        self.pv = pv  # type: long
        # 房间ID。
        self.room_id = room_id  # type: str
        # 直播状态，0-在播 1-下播。
        self.status = status  # type: int
        # 标题。
        self.title = title  # type: str
        # 访问用户数。
        self.uv = uv  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRoomsResponseBodyResultLiveList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListLiveRoomsResponseBodyResult(TeaModel):
    def __init__(self, has_more=None, live_list=None, page_total=None, total_count=None):
        # 是否还有下一页。
        self.has_more = has_more  # type: bool
        # 直播列表信息。
        self.live_list = live_list  # type: list[ListLiveRoomsResponseBodyResultLiveList]
        # 直播总页数。
        self.page_total = page_total  # type: int
        # 直播总数。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLiveRoomsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListLiveRoomsResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLiveRoomsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: ListLiveRoomsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListLiveRoomsResponseBody, self).to_map()
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
            temp_model = ListLiveRoomsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListLiveRoomsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLiveRoomsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLiveRoomsResponse, self).to_map()
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
            temp_model = ListLiveRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRoomsByIdRequest(TeaModel):
    def __init__(self, app_id=None, live_id_list=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID列表。
        self.live_id_list = live_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRoomsByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id_list is not None:
            result['LiveIdList'] = self.live_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveIdList') is not None:
            self.live_id_list = m.get('LiveIdList')
        return self


class ListLiveRoomsByIdShrinkRequest(TeaModel):
    def __init__(self, app_id=None, live_id_list_shrink=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID列表。
        self.live_id_list_shrink = live_id_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRoomsByIdShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id_list_shrink is not None:
            result['LiveIdList'] = self.live_id_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveIdList') is not None:
            self.live_id_list_shrink = m.get('LiveIdList')
        return self


class ListLiveRoomsByIdResponseBodyResultLiveList(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, chat_id=None, cover_url=None, extension=None,
                 live_id=None, notice=None, online_count=None, pv=None, room_id=None, status=None, title=None, uv=None):
        # 主播ID。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用ID。
        self.app_id = app_id  # type: str
        # 聊天ID。
        self.chat_id = chat_id  # type: str
        # 封面。
        self.cover_url = cover_url  # type: str
        # 直播拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 直播ID。
        self.live_id = live_id  # type: str
        # 公告。
        self.notice = notice  # type: str
        # 在线用户数。
        self.online_count = online_count  # type: long
        # 访问用户人次。
        self.pv = pv  # type: long
        # 房间ID。
        self.room_id = room_id  # type: str
        # 直播状态，0-在播 1-下播。
        self.status = status  # type: int
        # 标题。
        self.title = title  # type: str
        # 访问用户数。
        self.uv = uv  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRoomsByIdResponseBodyResultLiveList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListLiveRoomsByIdResponseBodyResult(TeaModel):
    def __init__(self, live_list=None):
        # 直播列表信息。
        self.live_list = live_list  # type: list[ListLiveRoomsByIdResponseBodyResultLiveList]

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLiveRoomsByIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListLiveRoomsByIdResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        return self


class ListLiveRoomsByIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: ListLiveRoomsByIdResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListLiveRoomsByIdResponseBody, self).to_map()
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
            temp_model = ListLiveRoomsByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListLiveRoomsByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLiveRoomsByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLiveRoomsByIdResponse, self).to_map()
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
            temp_model = ListLiveRoomsByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomUsersRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, room_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number  # type: int
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size  # type: int
        # 房间ID，最大长度36个字符。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class ListRoomUsersResponseBodyResultRoomUserList(TeaModel):
    def __init__(self, extension=None, nick=None, user_id=None):
        # 用户拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 用户昵称。
        self.nick = nick  # type: str
        # 用户唯一标识。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomUsersResponseBodyResultRoomUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRoomUsersResponseBodyResult(TeaModel):
    def __init__(self, has_more=None, page_total=None, room_user_list=None, total_count=None):
        # 是否还有下一页用户列表。
        self.has_more = has_more  # type: bool
        # 该房间的用户总页数。
        self.page_total = page_total  # type: int
        # 房间用户列表信息。
        self.room_user_list = room_user_list  # type: list[ListRoomUsersResponseBodyResultRoomUserList]
        # 该房间的用户总数。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.room_user_list:
            for k in self.room_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRoomUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['RoomUserList'] = []
        if self.room_user_list is not None:
            for k in self.room_user_list:
                result['RoomUserList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.room_user_list = []
        if m.get('RoomUserList') is not None:
            for k in m.get('RoomUserList'):
                temp_model = ListRoomUsersResponseBodyResultRoomUserList()
                self.room_user_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRoomUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # API请求的返回结果结构体。
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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRoomUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRoomUsersResponseBody()
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
    def __init__(self, create_time=None, extension=None, plugin_id=None, plugin_type=None):
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: long
        # 插件拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 插件实例唯一标识。
        self.plugin_id = plugin_id  # type: str
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class ListRoomsResponseBodyResultRoomInfoList(TeaModel):
    def __init__(self, app_id=None, create_time=None, extension=None, notice=None, online_count=None,
                 plugin_instance_info_list=None, room_id=None, room_owner_id=None, template_id=None, title=None, uv=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time  # type: str
        # 房间拓展字段。
        self.extension = extension  # type: dict[str, str]
        # 房间公告。
        self.notice = notice  # type: str
        # 用户在线数。
        self.online_count = online_count  # type: long
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list  # type: list[ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList]
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房主用户id。
        self.room_owner_id = room_owner_id  # type: str
        # 创建房间使用的模板id。
        self.template_id = template_id  # type: str
        # 房间标题。
        self.title = title  # type: str
        # 用户访问数。
        self.uv = uv  # type: long

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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['Uv'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        return self


class ListRoomsResponseBodyResult(TeaModel):
    def __init__(self, has_more=None, page_total=None, room_info_list=None, total_count=None):
        # 是否还有下一页房间列表。
        self.has_more = has_more  # type: bool
        # 该应用的房间总页数。
        self.page_total = page_total  # type: int
        # 房间列表信息。
        self.room_info_list = room_info_list  # type: list[ListRoomsResponseBodyResultRoomInfoList]
        # 该应用的房间总数。
        self.total_count = total_count  # type: int

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
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['RoomInfoList'] = []
        if self.room_info_list is not None:
            for k in self.room_info_list:
                result['RoomInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.room_info_list = []
        if m.get('RoomInfoList') is not None:
            for k in m.get('RoomInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRoomsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveWordRequest(TeaModel):
    def __init__(self, app_id=None):
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSensitiveWordRequest, self).to_map()
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


class ListSensitiveWordResponseBodyResult(TeaModel):
    def __init__(self, word_list=None):
        self.word_list = word_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSensitiveWordResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word_list is not None:
            result['WordList'] = self.word_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WordList') is not None:
            self.word_list = m.get('WordList')
        return self


class ListSensitiveWordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 调用发送直播间弹幕的返回结果。
        self.result = result  # type: ListSensitiveWordResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSensitiveWordResponseBody, self).to_map()
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
            temp_model = ListSensitiveWordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSensitiveWordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSensitiveWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSensitiveWordResponse, self).to_map()
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
            temp_model = ListSensitiveWordResponseBody()
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
    def __init__(self, anchor_id=None, live_id=None, live_url=None, push_url=None, status=None):
        # 主播ID
        self.anchor_id = anchor_id  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 直播拉流地址
        self.live_url = live_url  # type: str
        # 直播推流地址
        self.push_url = push_url  # type: str
        # 直播状态：Created-已创建未开播，Living-直播中，End-直播结束
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishLiveResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PublishLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishLiveRoomRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PublishLiveRoomResponseBodyResult(TeaModel):
    def __init__(self, live_id=None, live_url=None, push_url=None):
        # 直播ID。
        self.live_id = live_id  # type: str
        # 直播拉流地址。
        self.live_url = live_url  # type: str
        # 直播推流地址。
        self.push_url = push_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishLiveRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        return self


class PublishLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建场景化直播返回的结果。
        self.result = result  # type: PublishLiveRoomResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(PublishLiveRoomResponseBody, self).to_map()
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
            temp_model = PublishLiveRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishLiveRoomResponse, self).to_map()
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
            temp_model = PublishLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectLinkMicRequest(TeaModel):
    def __init__(self, conference_id=None, from_user_id=None, to_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 同意者用户ID
        self.from_user_id = from_user_id  # type: str
        # 被同意用户ID
        self.to_user_id = to_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectLinkMicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectLinkMicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RejectLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMemberRequest(TeaModel):
    def __init__(self, conference_id=None, from_user_id=None, to_user_id=None):
        # 会议唯一标识
        self.conference_id = conference_id  # type: str
        # 邀请者用户ID
        self.from_user_id = from_user_id  # type: str
        # 被邀请用户ID
        self.to_user_id = to_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCommentRequest(TeaModel):
    def __init__(self, app_id=None, content=None, extension=None, room_id=None, sender_id=None, sender_nick=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 发送的文本内容。最大的长度不超过256个字节。
        self.content = content  # type: str
        # 扩展字段，服务端仅做透传。
        self.extension = extension  # type: dict[str, str]
        # 直播间唯一标识，在调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.sender_id = sender_id  # type: str
        # 弹幕消息发送者的昵称。
        self.sender_nick = sender_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class SendCommentShrinkRequest(TeaModel):
    def __init__(self, app_id=None, content=None, extension_shrink=None, room_id=None, sender_id=None,
                 sender_nick=None):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id  # type: str
        # 发送的文本内容。最大的长度不超过256个字节。
        self.content = content  # type: str
        # 扩展字段，服务端仅做透传。
        self.extension_shrink = extension_shrink  # type: str
        # 直播间唯一标识，在调用CreateRoom返回。
        self.room_id = room_id  # type: str
        # 弹幕发送者的用户ID，最大长度不超过32个字节。
        self.sender_id = sender_id  # type: str
        # 弹幕消息发送者的昵称。
        self.sender_nick = sender_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        return self


class SendCommentResponseBodyResultCommentVO(TeaModel):
    def __init__(self, comment_id=None, content=None, create_at=None, extension=None, sender_id=None,
                 sender_nick=None):
        # 弹幕的唯一ID。
        self.comment_id = comment_id  # type: str
        # 弹幕的内容。
        self.content = content  # type: str
        # 弹幕的创建时间，Unix时间戳，单位：毫秒。
        self.create_at = create_at  # type: long
        # 扩展字段。
        self.extension = extension  # type: dict[str, str]
        # 弹幕的发送者ID标识。
        self.sender_id = sender_id  # type: str
        # 弹幕发送者的昵称。
        self.sender_nick = sender_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommentResponseBodyResultCommentVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment_id is not None:
            result['CommentId'] = self.comment_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_at is not None:
            result['CreateAt'] = self.create_at
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommentId') is not None:
            self.comment_id = m.get('CommentId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToAllRequest(TeaModel):
    def __init__(self, app_id=None, body=None, room_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 消息体内容。
        self.body = body  # type: str
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCustomMessageToAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCustomMessageToAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToUsersRequest(TeaModel):
    def __init__(self, app_id=None, body=None, receiver_list=None, room_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 消息体内容。
        self.body = body  # type: str
        # 消息指定的接收人ID列表。
        self.receiver_list = receiver_list  # type: list[str]
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomMessageToUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.receiver_list is not None:
            result['ReceiverList'] = self.receiver_list
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ReceiverList') is not None:
            self.receiver_list = m.get('ReceiverList')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCustomMessageToUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCustomMessageToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserAdminRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id  # type: str
        # 用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserAdminRequest, self).to_map()
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


class SetUserAdminResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserAdminResponseBody, self).to_map()
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


class SetUserAdminResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetUserAdminResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserAdminResponse, self).to_map()
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
            temp_model = SetUserAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopClassRequest(TeaModel):
    def __init__(self, app_id=None, class_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 课堂唯一标识。
        self.class_id = class_id  # type: str
        # 操作者用户ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopClassResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopClassResponseBody, self).to_map()
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


class StopClassResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopClassResponse, self).to_map()
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
            temp_model = StopClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, room_id=None, user_id=None):
        # 租户名
        self.app_id = app_id  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 房间ID，最大长度36位
        self.room_id = room_id  # type: str
        # 创建直播用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRoomRequest(TeaModel):
    def __init__(self, app_id=None, live_id=None, user_id=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveRoomResponseBody, self).to_map()
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


class StopLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopLiveRoomResponse, self).to_map()
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
            temp_model = StopLiveRoomResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class UpdateAppTemplateRequest(TeaModel):
    def __init__(self, app_template_id=None, app_template_name=None, component_list=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list = component_list  # type: list[str]

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
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class UpdateAppTemplateShrinkRequest(TeaModel):
    def __init__(self, app_template_id=None, app_template_name=None, component_list_shrink=None):
        # 应用模板唯一标识
        self.app_template_id = app_template_id  # type: str
        # 应用模板名称
        self.app_template_name = app_template_name  # type: str
        # 组件列表
        self.component_list_shrink = component_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list_shrink is not None:
            result['ComponentList'] = self.component_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list_shrink = m.get('ComponentList')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppTemplateResponseBody()
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


class UpdateAppTemplateConfigResponseBodyResultConfigLogs(TeaModel):
    def __init__(self, code=None, message=None):
        # 日志标示
        self.code = code  # type: str
        # 日志内容
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppTemplateConfigResponseBodyResultConfigLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateAppTemplateConfigResponseBodyResult(TeaModel):
    def __init__(self, config_logs=None):
        # 配置日志列表
        self.config_logs = config_logs  # type: list[UpdateAppTemplateConfigResponseBodyResultConfigLogs]

    def validate(self):
        if self.config_logs:
            for k in self.config_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAppTemplateConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigLogs'] = []
        if self.config_logs is not None:
            for k in self.config_logs:
                result['ConfigLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_logs = []
        if m.get('ConfigLogs') is not None:
            for k in m.get('ConfigLogs'):
                temp_model = UpdateAppTemplateConfigResponseBodyResultConfigLogs()
                self.config_logs.append(temp_model.from_map(k))
        return self


class UpdateAppTemplateConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: UpdateAppTemplateConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateAppTemplateConfigResponseBody, self).to_map()
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
            temp_model = UpdateAppTemplateConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateAppTemplateConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppTemplateConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppTemplateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClassRequest(TeaModel):
    def __init__(self, app_id=None, class_id=None, create_nickname=None, create_user_id=None, title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 课堂唯一标识。
        self.class_id = class_id  # type: str
        # 创建人用户昵称，1~32个字符。
        self.create_nickname = create_nickname  # type: str
        # 创建人用户ID，仅支持中英文数字，下划线，中划线，1~36个字符。
        self.create_user_id = create_user_id  # type: str
        # 课堂标题，1~32个字符。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.create_nickname is not None:
            result['CreateNickname'] = self.create_nickname
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('CreateNickname') is not None:
            self.create_nickname = m.get('CreateNickname')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateClassResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClassResponseBody, self).to_map()
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


class UpdateClassResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClassResponse, self).to_map()
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
            temp_model = UpdateClassResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRequest(TeaModel):
    def __init__(self, introduction=None, live_id=None, title=None):
        # 直播简介，支持中英文，最大长度2048位
        self.introduction = introduction  # type: str
        # 直播资源的唯一标识ID
        self.live_id = live_id  # type: str
        # 直播标题，支持中英文，最大长度256位
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRoomRequest(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, cover_url=None, extension=None, live_id=None,
                 notice=None, title=None, user_id=None):
        # 主播id，仅支持英文和数字，最大长度36位。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 封面，支持图片地址链接格式
        self.cover_url = cover_url  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension  # type: dict[str, str]
        # 直播ID。
        self.live_id = live_id  # type: str
        # 公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveRoomShrinkRequest(TeaModel):
    def __init__(self, anchor_id=None, anchor_nick=None, app_id=None, cover_url=None, extension_shrink=None,
                 live_id=None, notice=None, title=None, user_id=None):
        # 主播id，仅支持英文和数字，最大长度36位。
        self.anchor_id = anchor_id  # type: str
        # 主播昵称。
        self.anchor_nick = anchor_nick  # type: str
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 封面，支持图片地址链接格式
        self.cover_url = cover_url  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension_shrink = extension_shrink  # type: str
        # 直播ID。
        self.live_id = live_id  # type: str
        # 公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 标题，支持中英文，最大长度32位。
        self.title = title  # type: str
        # 操作人ID。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.anchor_nick is not None:
            result['AnchorNick'] = self.anchor_nick
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('AnchorNick') is not None:
            self.anchor_nick = m.get('AnchorNick')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveRoomResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveRoomResponseBody, self).to_map()
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


class UpdateLiveRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLiveRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLiveRoomResponse, self).to_map()
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
            temp_model = UpdateLiveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoomRequest(TeaModel):
    def __init__(self, app_id=None, extension=None, notice=None, room_id=None, room_owner_id=None, title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension  # type: dict[str, str]
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateRoomShrinkRequest(TeaModel):
    def __init__(self, app_id=None, extension_shrink=None, notice=None, room_id=None, room_owner_id=None, title=None):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id  # type: str
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension_shrink = extension_shrink  # type: str
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice  # type: str
        # 房间唯一标识。
        self.room_id = room_id  # type: str
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id  # type: str
        # 房间标题，支持中英文，最大长度32位。
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateRoomResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyDomainOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


