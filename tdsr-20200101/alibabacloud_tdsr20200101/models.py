# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddMosaicsRequest(TeaModel):
    def __init__(self, mark_position=None, sub_scene_id=None):
        # 马赛克位置数据
        self.mark_position = mark_position  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMosaicsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mark_position is not None:
            result['MarkPosition'] = self.mark_position
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MarkPosition') is not None:
            self.mark_position = m.get('MarkPosition')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class AddMosaicsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMosaicsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddMosaicsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddMosaicsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMosaicsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddMosaicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProjectRequest(TeaModel):
    def __init__(self, business_id=None, name=None):
        # 业务id
        self.business_id = business_id  # type: long
        # 项目名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AddProjectResponseBody(TeaModel):
    def __init__(self, code=None, id=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 项目ID
        self.id = id  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRelativePositionRequest(TeaModel):
    def __init__(self, relative_position=None, scene_id=None):
        # 相对位置信息
        self.relative_position = relative_position  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRelativePositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relative_position is not None:
            result['RelativePosition'] = self.relative_position
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelativePosition') is not None:
            self.relative_position = m.get('RelativePosition')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AddRelativePositionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRelativePositionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRelativePositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRelativePositionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRelativePositionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddRelativePositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRoomPlanRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRoomPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AddRoomPlanResponseBodyData(TeaModel):
    def __init__(self, access_id=None, callback=None, dir=None, expire=None, host=None, policy=None, signature=None):
        # accessId
        self.access_id = access_id  # type: str
        # 上传回调
        self.callback = callback  # type: str
        # 授权路径
        self.dir = dir  # type: str
        # 授权失效时间(s)
        self.expire = expire  # type: str
        # 上传地址
        self.host = host  # type: str
        # 授权
        self.policy = policy  # type: str
        # 签名
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRoomPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class AddRoomPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 文件上传凭据
        self.data = data  # type: AddRoomPlanResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddRoomPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddRoomPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRoomPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRoomPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRoomPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddRoomPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSceneRequest(TeaModel):
    def __init__(self, customer_uid=None, name=None, project_id=None, type=None):
        self.customer_uid = customer_uid  # type: str
        # 场景名称
        self.name = name  # type: str
        # 项目ID
        self.project_id = project_id  # type: str
        # 场景类型 3D模型：MODEL_3D  全景图片：PIC  全景视频：VIDEO 混合：MIX
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddSceneResponseBody(TeaModel):
    def __init__(self, code=None, id=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 场景ID
        self.id = id  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSubSceneRequest(TeaModel):
    def __init__(self, name=None, scene_id=None, upload_type=None):
        # 子场景名称
        self.name = name  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 类型 图片：IMAGE 视频：VIDEO
        self.upload_type = upload_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class AddSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, id=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 子场景ID
        self.id = id  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserPropertyRequest(TeaModel):
    def __init__(self, uid=None):
        # 用户uid
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CheckUserPropertyResponseBody(TeaModel):
    def __init__(self, code=None, match=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 用户属性是否匹配
        self.match = match  # type: bool
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.match is not None:
            result['Match'] = self.match
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUserPropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckUserPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUserPropertyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckUserPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopySceneRequest(TeaModel):
    def __init__(self, scene_id=None, scene_name=None):
        # 场景Id
        self.scene_id = scene_id  # type: str
        # 新场景名称
        self.scene_name = scene_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopySceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class CopySceneResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopySceneResponseBodyData, self).to_map()
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


class CopySceneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: CopySceneResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CopySceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CopySceneResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CopySceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopySceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopySceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopySceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailProjectRequest(TeaModel):
    def __init__(self, id=None):
        # 项目Id
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailProjectResponseBody(TeaModel):
    def __init__(self, business_id=None, business_name=None, code=None, gmt_create=None, gmt_modified=None, id=None,
                 message=None, name=None, request_id=None, success=None, token=None):
        # 业务ID
        self.business_id = business_id  # type: long
        # 业务名称
        self.business_name = business_name  # type: str
        # 返回码
        self.code = code  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 项目ID
        self.id = id  # type: str
        # 错误消息
        self.message = message  # type: str
        # 项目名称
        self.name = name  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # Token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.code is not None:
            result['Code'] = self.code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DetailProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetailProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetailProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailSceneRequest(TeaModel):
    def __init__(self, id=None):
        # 场景Id
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailSceneResponseBody(TeaModel):
    def __init__(self, code=None, cover_url=None, gmt_create=None, gmt_modified=None, id=None, message=None,
                 name=None, preview_token=None, published=None, request_id=None, source_num=None, sub_scene_num=None,
                 success=None, type=None):
        # 返回码
        self.code = code  # type: long
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 主场景Id
        self.id = id  # type: str
        # 错误消息
        self.message = message  # type: str
        # 场景名称
        self.name = name  # type: str
        # 预览Token
        self.preview_token = preview_token  # type: str
        # 是否已发布 true：已发布：false：未发布
        self.published = published  # type: bool
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 资源数
        self.source_num = source_num  # type: long
        # 子场景数
        self.sub_scene_num = sub_scene_num  # type: long
        # 是否请求成功
        self.success = success  # type: bool
        # 场景类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.published is not None:
            result['Published'] = self.published
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_num is not None:
            result['SourceNum'] = self.source_num
        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Published') is not None:
            self.published = m.get('Published')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')
        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetailSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetailSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetailSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailSubSceneRequest(TeaModel):
    def __init__(self, id=None):
        # 子场景ID
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, cover_url=None, cubemap_path=None, gmt_create=None, gmt_modified=None, id=None,
                 image_url=None, layout_data=None, message=None, name=None, origin_url=None, request_id=None, resource_id=None,
                 status=None, success=None, type=None, url=None):
        # 返回码
        self.code = code  # type: long
        # 图片路径/视频封面路径
        self.cover_url = cover_url  # type: str
        # 切图路径
        self.cubemap_path = cubemap_path  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 子场景id
        self.id = id  # type: str
        # 矫正后图的路径
        self.image_url = image_url  # type: str
        # 墙线标注数据
        self.layout_data = layout_data  # type: str
        # 错误消息
        self.message = message  # type: str
        # 子场景名称
        self.name = name  # type: str
        # 原图路径
        self.origin_url = origin_url  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 图片ID/视频ID
        self.resource_id = resource_id  # type: str
        # 子场景状态
        self.status = status  # type: long
        # 是否请求成功
        self.success = success  # type: bool
        # 资源类型
        self.type = type  # type: str
        # 图片路径/视频路径
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.cubemap_path is not None:
            result['CubemapPath'] = self.cubemap_path
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CubemapPath') is not None:
            self.cubemap_path = m.get('CubemapPath')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetailSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetailSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetailSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        # 项目ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropProjectRequest, self).to_map()
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


class DropProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID与入参中requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DropProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DropProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DropProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropSceneRequest(TeaModel):
    def __init__(self, id=None):
        # 主场景id
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DropSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DropSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DropSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DropSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropSubSceneRequest(TeaModel):
    def __init__(self, id=None):
        # 子场景ID
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DropSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DropSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DropSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DropSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DropSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnDataRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetConnDataResponseBodyList(TeaModel):
    def __init__(self, id=None, map_id=None, type=None):
        # ID
        self.id = id  # type: str
        # 关联的ID
        self.map_id = map_id  # type: str
        # outer:外关联 inner：内关联 stair：楼梯关联
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnDataResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.map_id is not None:
            result['MapId'] = self.map_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetConnDataResponseBody(TeaModel):
    def __init__(self, code=None, extend=None, list=None, message=None, request_id=None, success=None, version=None):
        # 返回码
        self.code = code  # type: long
        # 扩展信息
        self.extend = extend  # type: str
        # 关联信息
        self.list = list  # type: list[GetConnDataResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 版本
        self.version = version  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConnDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.extend is not None:
            result['Extend'] = self.extend
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetConnDataResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetConnDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConnDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCopySceneTaskStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCopySceneTaskStatusRequest, self).to_map()
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


class GetCopySceneTaskStatusResponseBodyData(TeaModel):
    def __init__(self, progress=None, status=None):
        # 任务进度
        self.progress = progress  # type: long
        # 任务状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCopySceneTaskStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetCopySceneTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetCopySceneTaskStatusResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCopySceneTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCopySceneTaskStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCopySceneTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCopySceneTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCopySceneTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCopySceneTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotConfigRequest(TeaModel):
    def __init__(self, domain=None, enabled=None, preview_token=None, type=None):
        self.domain = domain  # type: str
        self.enabled = enabled  # type: bool
        self.preview_token = preview_token  # type: str
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotspotConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotspotConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHotspotConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotSceneDataRequest(TeaModel):
    def __init__(self, domain=None, enabled=None, preview_token=None, type=None):
        # 自定义oss域名（可为cdn域名）
        self.domain = domain  # type: str
        # 是否开启自用资源访问
        self.enabled = enabled  # type: bool
        # 预览token
        self.preview_token = preview_token  # type: str
        # 0 未发布， 1 已发布
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotSceneDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotSceneDataResponseBodyData(TeaModel):
    def __init__(self, model_token=None, preview_data=None, preview_token=None, scene_type=None):
        # 模型token（sgm token）
        self.model_token = model_token  # type: str
        # html转译后的预览数据，包含图片、子场景ID等信息
        self.preview_data = preview_data  # type: str
        # 预览token
        self.preview_token = preview_token  # type: str
        # 3D模型：MODEL_3D 全景图片：PIC 全景视频：VIDEO
        self.scene_type = scene_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotSceneDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        if self.preview_data is not None:
            result['PreviewData'] = self.preview_data
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        if m.get('PreviewData') is not None:
            self.preview_data = m.get('PreviewData')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class GetHotspotSceneDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetHotspotSceneDataResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotspotSceneDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHotspotSceneDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotSceneDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotspotSceneDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotspotSceneDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHotspotSceneDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotTagRequest(TeaModel):
    def __init__(self, domain=None, enabled=None, preview_token=None, sub_scene_uuid=None, type=None):
        self.domain = domain  # type: str
        self.enabled = enabled  # type: bool
        self.preview_token = preview_token  # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotTagResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, object_string=None, request_id=None, success=None):
        self.data = data  # type: str
        self.err_message = err_message  # type: str
        self.object_string = object_string  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotspotTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.object_string is not None:
            result['ObjectString'] = self.object_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ObjectString') is not None:
            self.object_string = m.get('ObjectString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotspotTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotspotTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHotspotTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayoutDataRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLayoutDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetLayoutDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 标注信息
        self.data = data  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLayoutDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLayoutDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLayoutDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLayoutDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOriginLayoutDataRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOriginLayoutDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetOriginLayoutDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 标注数据
        self.data = data  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOriginLayoutDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOriginLayoutDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOriginLayoutDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOriginLayoutDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOriginLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssPolicyRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetOssPolicyResponseBody(TeaModel):
    def __init__(self, access_id=None, callback=None, code=None, dir=None, expire=None, host=None, message=None,
                 policy=None, request_id=None, signature=None, success=None):
        # accessId
        self.access_id = access_id  # type: str
        # 上传回调
        self.callback = callback  # type: str
        # 返回码
        self.code = code  # type: long
        # 授权路径
        self.dir = dir  # type: str
        # 授权失效时间(s)
        self.expire = expire  # type: str
        # 上传地址
        self.host = host  # type: str
        # 错误消息
        self.message = message  # type: str
        # 授权
        self.policy = policy  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 签名
        self.signature = signature  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.code is not None:
            result['Code'] = self.code
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.message is not None:
            result['Message'] = self.message
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOssPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOssPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOssPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPackSceneTaskStatusRequest(TeaModel):
    def __init__(self, task_id=None, type=None):
        # 任务ID
        self.task_id = task_id  # type: str
        # 操作类型：download（下载），sync（同步）
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackSceneTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPackSceneTaskStatusResponseBodyData(TeaModel):
    def __init__(self, progress=None, status=None):
        # 任务进度
        self.progress = progress  # type: long
        # 任务状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackSceneTaskStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetPackSceneTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetPackSceneTaskStatusResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPackSceneTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPackSceneTaskStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPackSceneTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPackSceneTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPackSceneTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPackSceneTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRectifyImageRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRectifyImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetRectifyImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, url=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 图片地址
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRectifyImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRectifyImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRectifyImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRectifyImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRectifyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneBuildTaskStatusRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSceneBuildTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetSceneBuildTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, error_msg=None, message=None, request_id=None, scene_id=None,
                 status=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 任务失败错误码
        self.error_code = error_code  # type: str
        # 任务失败错误消息
        self.error_msg = error_msg  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 未开始  init 处理中 失败     failed   processing  完成     succeed 取消     canceled
        self.status = status  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSceneBuildTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSceneBuildTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSceneBuildTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSceneBuildTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSceneBuildTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenePackUrlRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePackUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetScenePackUrlResponseBodyData(TeaModel):
    def __init__(self, expire=None, url=None, valid=None):
        # 失效日期
        self.expire = expire  # type: str
        # 打包文件地址
        self.url = url  # type: str
        # 是否有效
        self.valid = valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePackUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.url is not None:
            result['Url'] = self.url
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetScenePackUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetScenePackUrlResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScenePackUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetScenePackUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenePackUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScenePackUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScenePackUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScenePackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenePreviewDataRequest(TeaModel):
    def __init__(self, domain=None, enabled=None, preview_token=None, show_tag=None):
        # 自定义oss域名（可为cdn域名）
        self.domain = domain  # type: str
        # 是否开启自用资源访问（默认false）
        self.enabled = enabled  # type: bool
        # 预览token
        self.preview_token = preview_token  # type: str
        # 是否返回热点数据（默认false）
        self.show_tag = show_tag  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.show_tag is not None:
            result['ShowTag'] = self.show_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('ShowTag') is not None:
            self.show_tag = m.get('ShowTag')
        return self


class GetScenePreviewDataResponseBodyDataModelPanoListPosition(TeaModel):
    def __init__(self, rotation=None, spot=None, viewpoint=None):
        # 当前点位在场景中的旋转四元素
        self.rotation = rotation  # type: list[float]
        # 当前点位在场景中的坐标
        self.spot = spot  # type: list[float]
        # 当前子场景名标签在场景中的坐标
        self.viewpoint = viewpoint  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataModelPanoListPosition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotation is not None:
            result['Rotation'] = self.rotation
        if self.spot is not None:
            result['Spot'] = self.spot
        if self.viewpoint is not None:
            result['Viewpoint'] = self.viewpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')
        if m.get('Spot') is not None:
            self.spot = m.get('Spot')
        if m.get('Viewpoint') is not None:
            self.viewpoint = m.get('Viewpoint')
        return self


class GetScenePreviewDataResponseBodyDataModelPanoList(TeaModel):
    def __init__(self, cur_room_pic_list=None, enabled=None, floor_idx=None, id=None, main_image=None,
                 neighbours=None, position=None, raw_name=None, resource=None, room_idx=None, sub_scene_id=None, token=None,
                 virtual_id=None, virtual_name=None):
        # 当前房间的所有点位
        self.cur_room_pic_list = cur_room_pic_list  # type: list[str]
        # 当前点位是否渲染，false不渲染，场景无法跳转
        self.enabled = enabled  # type: bool
        # 楼层号
        self.floor_idx = floor_idx  # type: str
        # 点位ID
        self.id = id  # type: str
        # 单房间多图情况下，是否为主图，默认true
        self.main_image = main_image  # type: bool
        # 当前房间邻近可视的点位id
        self.neighbours = neighbours  # type: list[str]
        # 位置数据
        self.position = position  # type: GetScenePreviewDataResponseBodyDataModelPanoListPosition
        # 一个名称，无实际意义
        self.raw_name = raw_name  # type: str
        # 全景贴图路径
        self.resource = resource  # type: str
        # 房间号
        self.room_idx = room_idx  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str
        # token
        self.token = token  # type: str
        # 图片虚拟ID
        self.virtual_id = virtual_id  # type: str
        # 图片名称
        self.virtual_name = virtual_name  # type: str

    def validate(self):
        if self.position:
            self.position.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataModelPanoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_room_pic_list is not None:
            result['CurRoomPicList'] = self.cur_room_pic_list
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.floor_idx is not None:
            result['FloorIdx'] = self.floor_idx
        if self.id is not None:
            result['Id'] = self.id
        if self.main_image is not None:
            result['MainImage'] = self.main_image
        if self.neighbours is not None:
            result['Neighbours'] = self.neighbours
        if self.position is not None:
            result['Position'] = self.position.to_map()
        if self.raw_name is not None:
            result['RawName'] = self.raw_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.room_idx is not None:
            result['RoomIdx'] = self.room_idx
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.token is not None:
            result['Token'] = self.token
        if self.virtual_id is not None:
            result['VirtualId'] = self.virtual_id
        if self.virtual_name is not None:
            result['VirtualName'] = self.virtual_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurRoomPicList') is not None:
            self.cur_room_pic_list = m.get('CurRoomPicList')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('FloorIdx') is not None:
            self.floor_idx = m.get('FloorIdx')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MainImage') is not None:
            self.main_image = m.get('MainImage')
        if m.get('Neighbours') is not None:
            self.neighbours = m.get('Neighbours')
        if m.get('Position') is not None:
            temp_model = GetScenePreviewDataResponseBodyDataModelPanoListPosition()
            self.position = temp_model.from_map(m['Position'])
        if m.get('RawName') is not None:
            self.raw_name = m.get('RawName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RoomIdx') is not None:
            self.room_idx = m.get('RoomIdx')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VirtualId') is not None:
            self.virtual_id = m.get('VirtualId')
        if m.get('VirtualName') is not None:
            self.virtual_name = m.get('VirtualName')
        return self


class GetScenePreviewDataResponseBodyDataModel(TeaModel):
    def __init__(self, model_path=None, pano_list=None, texture_model_path=None, texture_pano_path=None):
        # 模型地址
        self.model_path = model_path  # type: str
        # 点位数据
        self.pano_list = pano_list  # type: list[GetScenePreviewDataResponseBodyDataModelPanoList]
        # 模型的贴图路径
        self.texture_model_path = texture_model_path  # type: str
        # 漫游后预览图片路径
        self.texture_pano_path = texture_pano_path  # type: str

    def validate(self):
        if self.pano_list:
            for k in self.pano_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['ModelPath'] = self.model_path
        result['PanoList'] = []
        if self.pano_list is not None:
            for k in self.pano_list:
                result['PanoList'].append(k.to_map() if k else None)
        if self.texture_model_path is not None:
            result['TextureModelPath'] = self.texture_model_path
        if self.texture_pano_path is not None:
            result['TexturePanoPath'] = self.texture_pano_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')
        self.pano_list = []
        if m.get('PanoList') is not None:
            for k in m.get('PanoList'):
                temp_model = GetScenePreviewDataResponseBodyDataModelPanoList()
                self.pano_list.append(temp_model.from_map(k))
        if m.get('TextureModelPath') is not None:
            self.texture_model_path = m.get('TextureModelPath')
        if m.get('TexturePanoPath') is not None:
            self.texture_pano_path = m.get('TexturePanoPath')
        return self


class GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig(TeaModel):
    def __init__(self, custom_text=None, type=None):
        self.custom_text = custom_text  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_text is not None:
            result['CustomText'] = self.custom_text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomText') is not None:
            self.custom_text = m.get('CustomText')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetScenePreviewDataResponseBodyDataTagsConfig(TeaModel):
    def __init__(self, background_color=None, button_config=None, content=None, form_img_size=None,
                 form_jump_type=None, form_select_img_type=None, images=None, is_tag_visible_by_3d=None, link=None, pano_id=None,
                 position=None, position_pano_cube=None, related_pano_ids=None, scene_id=None, title=None, video=None):
        # 背景色
        self.background_color = background_color  # type: str
        # 按钮配置
        self.button_config = button_config  # type: GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig
        # 内容
        self.content = content  # type: str
        self.form_img_size = form_img_size  # type: list[long]
        self.form_jump_type = form_jump_type  # type: bool
        self.form_select_img_type = form_select_img_type  # type: str
        # 图片链接
        self.images = images  # type: list[str]
        # 是否在鸟瞰模式下显示
        self.is_tag_visible_by_3d = is_tag_visible_by_3d  # type: bool
        # 超链接
        self.link = link  # type: str
        # 点位ID
        self.pano_id = pano_id  # type: str
        # 坐标
        self.position = position  # type: list[float]
        self.position_pano_cube = position_pano_cube  # type: list[float]
        self.related_pano_ids = related_pano_ids  # type: list[str]
        # 场景ID
        self.scene_id = scene_id  # type: long
        # 标题
        self.title = title  # type: str
        # 视频链接
        self.video = video  # type: str

    def validate(self):
        if self.button_config:
            self.button_config.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataTagsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.button_config is not None:
            result['ButtonConfig'] = self.button_config.to_map()
        if self.content is not None:
            result['Content'] = self.content
        if self.form_img_size is not None:
            result['FormImgSize'] = self.form_img_size
        if self.form_jump_type is not None:
            result['FormJumpType'] = self.form_jump_type
        if self.form_select_img_type is not None:
            result['FormSelectImgType'] = self.form_select_img_type
        if self.images is not None:
            result['Images'] = self.images
        if self.is_tag_visible_by_3d is not None:
            result['IsTagVisibleBy3d'] = self.is_tag_visible_by_3d
        if self.link is not None:
            result['Link'] = self.link
        if self.pano_id is not None:
            result['PanoId'] = self.pano_id
        if self.position is not None:
            result['Position'] = self.position
        if self.position_pano_cube is not None:
            result['PositionPanoCube'] = self.position_pano_cube
        if self.related_pano_ids is not None:
            result['RelatedPanoIds'] = self.related_pano_ids
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.title is not None:
            result['Title'] = self.title
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('ButtonConfig') is not None:
            temp_model = GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig()
            self.button_config = temp_model.from_map(m['ButtonConfig'])
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FormImgSize') is not None:
            self.form_img_size = m.get('FormImgSize')
        if m.get('FormJumpType') is not None:
            self.form_jump_type = m.get('FormJumpType')
        if m.get('FormSelectImgType') is not None:
            self.form_select_img_type = m.get('FormSelectImgType')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('IsTagVisibleBy3d') is not None:
            self.is_tag_visible_by_3d = m.get('IsTagVisibleBy3d')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('PanoId') is not None:
            self.pano_id = m.get('PanoId')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('PositionPanoCube') is not None:
            self.position_pano_cube = m.get('PositionPanoCube')
        if m.get('RelatedPanoIds') is not None:
            self.related_pano_ids = m.get('RelatedPanoIds')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class GetScenePreviewDataResponseBodyDataTags(TeaModel):
    def __init__(self, config=None, id=None, position=None, position_pano_cube=None, type=None):
        # 配置
        self.config = config  # type: GetScenePreviewDataResponseBodyDataTagsConfig
        # 标签ID
        self.id = id  # type: str
        # 坐标
        self.position = position  # type: list[float]
        self.position_pano_cube = position_pano_cube  # type: list[float]
        # 热点类型
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.position is not None:
            result['Position'] = self.position
        if self.position_pano_cube is not None:
            result['PositionPanoCube'] = self.position_pano_cube
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = GetScenePreviewDataResponseBodyDataTagsConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('PositionPanoCube') is not None:
            self.position_pano_cube = m.get('PositionPanoCube')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetScenePreviewDataResponseBodyData(TeaModel):
    def __init__(self, model=None, tags=None):
        # 模型数据
        self.model = model  # type: GetScenePreviewDataResponseBodyDataModel
        # 热点数据
        self.tags = tags  # type: list[GetScenePreviewDataResponseBodyDataTags]

    def validate(self):
        if self.model:
            self.model.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Model') is not None:
            temp_model = GetScenePreviewDataResponseBodyDataModel()
            self.model = temp_model.from_map(m['Model'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetScenePreviewDataResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetScenePreviewDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetScenePreviewDataResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetScenePreviewDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenePreviewDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScenePreviewDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScenePreviewDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScenePreviewDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenePreviewInfoRequest(TeaModel):
    def __init__(self, domain=None, enabled=None, model_token=None):
        # 自定义oss域名（可为cdn域名）
        self.domain = domain  # type: str
        # 是否开启自用资源访问
        self.enabled = enabled  # type: bool
        # 模型token
        self.model_token = model_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        return self


class GetScenePreviewInfoResponseBodyData(TeaModel):
    def __init__(self, model_path=None, pano_list=None, texture_model_path=None, texture_pano_path=None):
        # 模型地址
        self.model_path = model_path  # type: str
        # html转译后的预览数据
        self.pano_list = pano_list  # type: str
        # 模型的贴图路径
        self.texture_model_path = texture_model_path  # type: str
        # 漫游后预览图片路径
        self.texture_pano_path = texture_pano_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['ModelPath'] = self.model_path
        if self.pano_list is not None:
            result['PanoList'] = self.pano_list
        if self.texture_model_path is not None:
            result['TextureModelPath'] = self.texture_model_path
        if self.texture_pano_path is not None:
            result['TexturePanoPath'] = self.texture_pano_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')
        if m.get('PanoList') is not None:
            self.pano_list = m.get('PanoList')
        if m.get('TextureModelPath') is not None:
            self.texture_model_path = m.get('TextureModelPath')
        if m.get('TexturePanoPath') is not None:
            self.texture_pano_path = m.get('TexturePanoPath')
        return self


class GetScenePreviewInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetScenePreviewInfoResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScenePreviewInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetScenePreviewInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenePreviewInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScenePreviewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScenePreviewInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScenePreviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenePreviewResourceRequest(TeaModel):
    def __init__(self, preview_token=None):
        # 预览token
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        return self


class GetScenePreviewResourceResponseBodyDataResourceDirectory(TeaModel):
    def __init__(self, model_config=None, orthomap_config=None, root_path=None):
        self.model_config = model_config  # type: str
        self.orthomap_config = orthomap_config  # type: str
        self.root_path = root_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScenePreviewResourceResponseBodyDataResourceDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config
        if self.orthomap_config is not None:
            result['OrthomapConfig'] = self.orthomap_config
        if self.root_path is not None:
            result['RootPath'] = self.root_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelConfig') is not None:
            self.model_config = m.get('ModelConfig')
        if m.get('OrthomapConfig') is not None:
            self.orthomap_config = m.get('OrthomapConfig')
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')
        return self


class GetScenePreviewResourceResponseBodyData(TeaModel):
    def __init__(self, name=None, resource_directory=None, version=None):
        self.name = name  # type: str
        self.resource_directory = resource_directory  # type: GetScenePreviewResourceResponseBodyDataResourceDirectory
        self.version = version  # type: str

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super(GetScenePreviewResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceDirectory') is not None:
            temp_model = GetScenePreviewResourceResponseBodyDataResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetScenePreviewResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetScenePreviewResourceResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScenePreviewResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetScenePreviewResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenePreviewResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScenePreviewResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScenePreviewResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScenePreviewResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSingleConnDataRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSingleConnDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetSingleConnDataResponseBodyList(TeaModel):
    def __init__(self, id=None, map_id=None, type=None):
        # ID
        self.id = id  # type: str
        # 关联ID
        self.map_id = map_id  # type: str
        # outer:外关联 inner：内关联 stair：楼梯关联
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSingleConnDataResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.map_id is not None:
            result['MapId'] = self.map_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSingleConnDataResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, success=None, version=None):
        # 返回码
        self.code = code  # type: long
        # 关联信息
        self.list = list  # type: list[GetSingleConnDataResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 版本
        self.version = version  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSingleConnDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetSingleConnDataResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetSingleConnDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSingleConnDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSingleConnDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSingleConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSourcePackStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSourcePackStatusRequest, self).to_map()
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


class GetSourcePackStatusResponseBodyData(TeaModel):
    def __init__(self, progress=None, status=None):
        # 任务进度
        self.progress = progress  # type: long
        # 任务状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSourcePackStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetSourcePackStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, url=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: GetSourcePackStatusResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 压缩包的地址
        self.url = url  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSourcePackStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSourcePackStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetSourcePackStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSourcePackStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSourcePackStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSourcePackStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubSceneTaskStatusRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubSceneTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetSubSceneTaskStatusResponseBodyList(TeaModel):
    def __init__(self, error_code=None, error_msg=None, id=None, scene_id=None, status=None, sub_scene_id=None,
                 type=None):
        # 任务失败错误码
        self.error_code = error_code  # type: str
        # 任务失败错误信息
        self.error_msg = error_msg  # type: str
        # 任务ID
        self.id = id  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 未开始  init 处理中   processing   失败     failure  完成     succeed  取消     canceled
        self.status = status  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str
        # 墙线预测: wall_line   切图: cut_image 重建: build  直角优化：right_angle_optimization 其他：other
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubSceneTaskStatusResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.id is not None:
            result['Id'] = self.id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSubSceneTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 任务信息
        self.list = list  # type: list[GetSubSceneTaskStatusResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSubSceneTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetSubSceneTaskStatusResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubSceneTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubSceneTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubSceneTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubSceneTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusRequest, self).to_map()
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


class GetTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, error_msg=None, message=None, request_id=None, status=None,
                 success=None, type=None):
        # 返回码
        self.code = code  # type: long
        # 任务执行失败错误码
        self.error_code = error_code  # type: str
        # 任务执行失败错误消息
        self.error_msg = error_msg  # type: str
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 未开始 :init 处理中 : processing    失败 :failure   完成 :succeed  取消 :canceled
        self.status = status  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 墙线预测: wall_line 切图: cut_image   重建: build  直角优化：right_angle_optimization  其他：other
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWindowConfigRequest(TeaModel):
    def __init__(self, preview_token=None):
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWindowConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        return self


class GetWindowConfigResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, object_string=None, request_id=None, success=None):
        self.data = data  # type: dict[str, any]
        self.err_message = err_message  # type: str
        self.object_string = object_string  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWindowConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.object_string is not None:
            result['ObjectString'] = self.object_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ObjectString') is not None:
            self.object_string = m.get('ObjectString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWindowConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWindowConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWindowConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWindowConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LabelBuildRequest(TeaModel):
    def __init__(self, mode=None, model_style=None, optimize_wall_width=None, plan_style=None, scene_id=None,
                 wall_height=None):
        # 重建模式：MANUAL：手动（云端），默认，SEMI_AUTOMATIC：半自动（移动端）
        self.mode = mode  # type: str
        # 模型效果 PATCH：切片模型（默认） DEPTH：深度模型 VIRTUAL：虚拟模型 MOBILE：移动重建模型
        self.model_style = model_style  # type: str
        # 墙宽优化，OFF:关闭（默认） NORMAL：标准 ENHANCED：加强
        self.optimize_wall_width = optimize_wall_width  # type: str
        # 户型图，DEFAULT（默认），STANDARD（标准）
        self.plan_style = plan_style  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 墙高，默认0不设置，范围200-1000. 单位cm
        self.wall_height = wall_height  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(LabelBuildRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.model_style is not None:
            result['ModelStyle'] = self.model_style
        if self.optimize_wall_width is not None:
            result['OptimizeWallWidth'] = self.optimize_wall_width
        if self.plan_style is not None:
            result['PlanStyle'] = self.plan_style
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.wall_height is not None:
            result['WallHeight'] = self.wall_height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ModelStyle') is not None:
            self.model_style = m.get('ModelStyle')
        if m.get('OptimizeWallWidth') is not None:
            self.optimize_wall_width = m.get('OptimizeWallWidth')
        if m.get('PlanStyle') is not None:
            self.plan_style = m.get('PlanStyle')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('WallHeight') is not None:
            self.wall_height = m.get('WallHeight')
        return self


class LabelBuildResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 重建任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LabelBuildResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class LabelBuildResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LabelBuildResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LabelBuildResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LabelBuildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkImageRequest(TeaModel):
    def __init__(self, camera_height=None, file_name=None, platform=None, sub_scene_id=None):
        # 相机高度 单位 cm
        self.camera_height = camera_height  # type: int
        # 图片或者视频名称xxx.jpg
        self.file_name = file_name  # type: str
        # 平台标识，默认PC
        self.platform = platform  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LinkImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class LinkImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, resource_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 图片/视频ID
        self.resource_id = resource_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LinkImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LinkImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LinkImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LinkImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LinkImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(self, name=None, page_num=None, page_size=None):
        # 项目名称（使用name%搜索）
        self.name = name  # type: str
        # 页码
        self.page_num = page_num  # type: long
        # 页长
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListProjectResponseBodyList(TeaModel):
    def __init__(self, business_id=None, business_name=None, create_time=None, id=None, modified_time=None,
                 name=None, token=None):
        # 业务ID
        self.business_id = business_id  # type: long
        # 业务名称
        self.business_name = business_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: long
        # 项目ID
        self.id = id  # type: str
        # 最后修改时间
        self.modified_time = modified_time  # type: long
        # 项目名称
        self.name = name  # type: str
        # Token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(self, code=None, count=None, current_page=None, has_next=None, list=None, message=None,
                 request_id=None, success=None, total_page=None):
        # 返回码
        self.code = code  # type: long
        # count
        self.count = count  # type: long
        # 当前页
        self.current_page = current_page  # type: long
        # 是否有下一页
        self.has_next = has_next  # type: bool
        # 项目数据
        self.list = list  # type: list[ListProjectResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 总页数
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListProjectResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneRequest(TeaModel):
    def __init__(self, name=None, page_num=None, page_size=None, project_id=None):
        # 主场景名称
        self.name = name  # type: str
        # 当前页
        self.page_num = page_num  # type: long
        # 页长
        self.page_size = page_size  # type: long
        # 所有项目Id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListSceneResponseBodyList(TeaModel):
    def __init__(self, cover_url=None, gmt_create=None, gmt_modified=None, id=None, name=None, preview_token=None,
                 published=None, source_num=None, sub_scene_num=None, type=None):
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 主场景Id
        self.id = id  # type: str
        # 场景名称
        self.name = name  # type: str
        # 预览Token
        self.preview_token = preview_token  # type: str
        # 是否已发布 true：已发布：false：未发布
        self.published = published  # type: bool
        # 资源数
        self.source_num = source_num  # type: long
        # 子场景数
        self.sub_scene_num = sub_scene_num  # type: long
        # 场景类型 3D模型：MODEL_3D  全景图片：PIC  全景视频：VIDEO
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSceneResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.published is not None:
            result['Published'] = self.published
        if self.source_num is not None:
            result['SourceNum'] = self.source_num
        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Published') is not None:
            self.published = m.get('Published')
        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')
        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSceneResponseBody(TeaModel):
    def __init__(self, code=None, count=None, current_page=None, has_next=None, list=None, message=None,
                 request_id=None, success=None, total_page=None):
        # 返回码
        self.code = code  # type: long
        # 数据总数
        self.count = count  # type: long
        # 当前页
        self.current_page = current_page  # type: long
        # 是否有下一页
        self.has_next = has_next  # type: bool
        # 主场景数据
        self.list = list  # type: list[ListSceneResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 总页数
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSceneResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubSceneRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, scene_id=None, show_layout_data=None, sort_field=None):
        # 页码
        self.page_num = page_num  # type: long
        # 页长
        self.page_size = page_size  # type: long
        # 场景ID
        self.scene_id = scene_id  # type: str
        self.show_layout_data = show_layout_data  # type: bool
        # 排序字段，默认：NAME（名称），SEQUENCE（自定义排序）
        self.sort_field = sort_field  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.show_layout_data is not None:
            result['ShowLayoutData'] = self.show_layout_data
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ShowLayoutData') is not None:
            self.show_layout_data = m.get('ShowLayoutData')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        return self


class ListSubSceneResponseBodyList(TeaModel):
    def __init__(self, base_image_url=None, cover_url=None, cubemap_path=None, deleted=None, gmt_create=None,
                 gmt_modified=None, id=None, layout_data=None, name=None, origin_url=None, resource_id=None, resource_name=None,
                 status=None, type=None, url=None):
        # 2k基准图路径
        self.base_image_url = base_image_url  # type: str
        # 图片路径/视频封面路径
        self.cover_url = cover_url  # type: str
        # 切图的路径
        self.cubemap_path = cubemap_path  # type: str
        # 是否删除
        self.deleted = deleted  # type: bool
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 子场景ID
        self.id = id  # type: str
        # 标注数据
        self.layout_data = layout_data  # type: str
        # 子场景名称
        self.name = name  # type: str
        # 原图地址
        self.origin_url = origin_url  # type: str
        # 图片ID/视频ID
        self.resource_id = resource_id  # type: str
        # 资源名称
        self.resource_name = resource_name  # type: str
        # 子场景状态 1.未重建，      * 2.中间模型重建中，      * 3.中间模型重建完成，      * 4.待重建，      * 5.服务商重建中，      * 6.服务商重建完成，      * 7.已发布      * 8.发布中
        self.status = status  # type: long
        # 上传资源类型
        self.type = type  # type: str
        # 图片路径/视频路径
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubSceneResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_image_url is not None:
            result['BaseImageUrl'] = self.base_image_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.cubemap_path is not None:
            result['CubemapPath'] = self.cubemap_path
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data
        if self.name is not None:
            result['Name'] = self.name
        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseImageUrl') is not None:
            self.base_image_url = m.get('BaseImageUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CubemapPath') is not None:
            self.cubemap_path = m.get('CubemapPath')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, count=None, current_page=None, has_next=None, list=None, message=None,
                 request_id=None, success=None, total_page=None):
        # 返回码
        self.code = code  # type: long
        # 数据总条数
        self.count = count  # type: long
        # 当前页
        self.current_page = current_page  # type: long
        # 是否有下一页
        self.has_next = has_next  # type: bool
        # 子场景列表集
        self.list = list  # type: list[ListSubSceneResponseBodyList]
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 总页数
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSubSceneResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OptimizeRightAngleRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OptimizeRightAngleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class OptimizeRightAngleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OptimizeRightAngleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OptimizeRightAngleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OptimizeRightAngleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OptimizeRightAngleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OptimizeRightAngleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PackSceneRequest(TeaModel):
    def __init__(self, scene_id=None, type=None):
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 操作类型：download（下载），sync（同步）
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PackSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PackSceneResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PackSceneResponseBodyData, self).to_map()
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


class PackSceneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: PackSceneResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PackSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = PackSceneResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PackSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PackSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PackSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PackSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PackSourceRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PackSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class PackSourceResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PackSourceResponseBodyData, self).to_map()
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


class PackSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        self.data = data  # type: PackSourceResponseBodyData
        # 错误消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PackSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = PackSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PackSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PackSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PackSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PackSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredImageRequest(TeaModel):
    def __init__(self, correct_vertical=None, count_detect_door=None, detect_door=None, sub_scene_id=None):
        # 是否垂直矫正
        self.correct_vertical = correct_vertical  # type: bool
        # 门数量(DetectDoor为false时，可为0)
        self.count_detect_door = count_detect_door  # type: long
        # 是否门预测
        self.detect_door = detect_door  # type: bool
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.correct_vertical is not None:
            result['CorrectVertical'] = self.correct_vertical
        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door
        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CorrectVertical') is not None:
            self.correct_vertical = m.get('CorrectVertical')
        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')
        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class PredImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PredImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictionWallLineRequest(TeaModel):
    def __init__(self, camera_height=None, url=None):
        # 相机高度 单位 cm
        self.camera_height = camera_height  # type: long
        # 图片地址
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictionWallLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PredictionWallLineResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sub_scene_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictionWallLineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredictionWallLineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PredictionWallLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredictionWallLineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredictionWallLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishHotspotRequest(TeaModel):
    def __init__(self, param_tag=None, sub_scene_uuid=None):
        self.param_tag = param_tag  # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishHotspotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        return self


class PublishHotspotResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, request_id=None, success=None):
        self.data = data  # type: dict[str, any]
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishHotspotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishHotspotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishHotspotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishHotspotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishHotspotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishSceneRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class PublishSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, preview_url=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 预览链接
        self.preview_url = preview_url  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishStatusRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class PublishStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, status=None, success=None, sync_status=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 任务运行状态
        self.status = status  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 文件同步状态
        self.sync_status = sync_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class PublishStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryOriginImageRequest(TeaModel):
    def __init__(self, sub_scene_id=None):
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryOriginImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class RecoveryOriginImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryOriginImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecoveryOriginImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecoveryOriginImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoveryOriginImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecoveryOriginImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RectVerticalRequest(TeaModel):
    def __init__(self, count_detect_door=None, detect_door=None, sub_scene_id=None, vertical_rect=None):
        # 需要预测的门的数量
        self.count_detect_door = count_detect_door  # type: int
        # 是否开启门预测
        self.detect_door = detect_door  # type: bool
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str
        # 矫正数据
        self.vertical_rect = vertical_rect  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RectVerticalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door
        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.vertical_rect is not None:
            result['VerticalRect'] = self.vertical_rect
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')
        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('VerticalRect') is not None:
            self.vertical_rect = m.get('VerticalRect')
        return self


class RectVerticalResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 错误消息
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RectVerticalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RectVerticalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RectVerticalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RectVerticalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RectVerticalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RectifyImageRequest(TeaModel):
    def __init__(self, camera_height=None, url=None):
        # 相机高度 单位 cm
        self.camera_height = camera_height  # type: long
        # 图片地址
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RectifyImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RectifyImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sub_scene_id=None, success=None, task_id=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RectifyImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RectifyImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RectifyImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RectifyImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RectifyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSubSceneRequest(TeaModel):
    def __init__(self, id=None):
        # 子场景ID
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RollbackSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RollbackSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RollbackSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveHotspotConfigRequest(TeaModel):
    def __init__(self, param_tag=None, preview_token=None):
        self.param_tag = param_tag  # type: str
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveHotspotConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        return self


class SaveHotspotConfigResponseBody(TeaModel):
    def __init__(self, err_message=None, request_id=None, success=None):
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveHotspotConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveHotspotConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveHotspotConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveHotspotConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveHotspotConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveHotspotTagRequest(TeaModel):
    def __init__(self, param_tag=None, sub_scene_uuid=None):
        self.param_tag = param_tag  # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveHotspotTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        return self


class SaveHotspotTagResponseBody(TeaModel):
    def __init__(self, err_message=None, request_id=None, success=None):
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveHotspotTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveHotspotTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveHotspotTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveHotspotTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveHotspotTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScenePublishRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScenePublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ScenePublishResponseBody(TeaModel):
    def __init__(self, code=None, message=None, preview_url=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 预览链接
        self.preview_url = preview_url  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScenePublishResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScenePublishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScenePublishResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScenePublishResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScenePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempPreviewRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempPreviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class TempPreviewResponseBody(TeaModel):
    def __init__(self, code=None, message=None, preview_url=None, request_id=None, scene_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 预览链接
        self.preview_url = preview_url  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempPreviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TempPreviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TempPreviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TempPreviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TempPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempPreviewStatusRequest(TeaModel):
    def __init__(self, scene_id=None):
        # 任务ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempPreviewStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class TempPreviewStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, status=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 状态标识
        self.status = status  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempPreviewStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TempPreviewStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TempPreviewStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TempPreviewStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TempPreviewStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnDataRequest(TeaModel):
    def __init__(self, conn_data=None, scene_id=None):
        # 关联数据
        self.conn_data = conn_data  # type: str
        # 场景ID
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_data is not None:
            result['ConnData'] = self.conn_data
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnData') is not None:
            self.conn_data = m.get('ConnData')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class UpdateConnDataResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConnDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConnDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConnDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayoutDataRequest(TeaModel):
    def __init__(self, layout_data=None, sub_scene_id=None):
        # 标注数据
        self.layout_data = layout_data  # type: str
        # 子场景ID
        self.sub_scene_id = sub_scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLayoutDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class UpdateLayoutDataResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLayoutDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLayoutDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLayoutDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLayoutDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, business_id=None, id=None, name=None):
        # 业务Id
        self.business_id = business_id  # type: str
        # 项目id
        self.id = id  # type: str
        # 项目名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdateSceneRequest(TeaModel):
    def __init__(self, id=None, name=None):
        # 场景Id
        self.id = id  # type: str
        # 场景名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubSceneRequest(TeaModel):
    def __init__(self, id=None, name=None, view_point=None):
        # 子场景ID
        self.id = id  # type: str
        # 子场景名称
        self.name = name  # type: str
        # 视角坐标，目前支持3元坐标，4元坐标，例如：[0.94005,0.13397,-0.3136,0.782992]
        self.view_point = view_point  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.view_point is not None:
            result['ViewPoint'] = self.view_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ViewPoint') is not None:
            self.view_point = m.get('ViewPoint')
        return self


class UpdateSubSceneShrinkRequest(TeaModel):
    def __init__(self, id=None, name=None, view_point_shrink=None):
        # 子场景ID
        self.id = id  # type: str
        # 子场景名称
        self.name = name  # type: str
        # 视角坐标，目前支持3元坐标，4元坐标，例如：[0.94005,0.13397,-0.3136,0.782992]
        self.view_point_shrink = view_point_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.view_point_shrink is not None:
            result['ViewPoint'] = self.view_point_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ViewPoint') is not None:
            self.view_point_shrink = m.get('ViewPoint')
        return self


class UpdateSubSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSubSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSubSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubSceneSeqRequest(TeaModel):
    def __init__(self, scene_id=None, sort_sub_scene_ids=None):
        # 子场景ID
        self.scene_id = scene_id  # type: str
        self.sort_sub_scene_ids = sort_sub_scene_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneSeqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.sort_sub_scene_ids is not None:
            result['SortSubSceneIds'] = self.sort_sub_scene_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SortSubSceneIds') is not None:
            self.sort_sub_scene_ids = m.get('SortSubSceneIds')
        return self


class UpdateSubSceneSeqShrinkRequest(TeaModel):
    def __init__(self, scene_id=None, sort_sub_scene_ids_shrink=None):
        # 子场景ID
        self.scene_id = scene_id  # type: str
        self.sort_sub_scene_ids_shrink = sort_sub_scene_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneSeqShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.sort_sub_scene_ids_shrink is not None:
            result['SortSubSceneIds'] = self.sort_sub_scene_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SortSubSceneIds') is not None:
            self.sort_sub_scene_ids_shrink = m.get('SortSubSceneIds')
        return self


class UpdateSubSceneSeqResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 返回码
        self.code = code  # type: long
        # 错误消息
        self.message = message  # type: str
        # 请求ID，与入参requestId对应
        self.request_id = request_id  # type: str
        # 是否请求成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubSceneSeqResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSubSceneSeqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSubSceneSeqResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubSceneSeqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSubSceneSeqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


