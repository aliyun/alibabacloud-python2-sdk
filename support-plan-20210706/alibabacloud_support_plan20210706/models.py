# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EnterpriseDingtalkGroupMember(TeaModel):
    def __init__(self, is_admin=None, mobile=None, name=None):
        # 是否企业钉群管理员
        self.is_admin = is_admin  # type: bool
        # 成员手机号
        self.mobile = mobile  # type: str
        # 成员姓名
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnterpriseDingtalkGroupMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersRequest(TeaModel):
    def __init__(self, open_group_id=None):
        # 企业服务群ID
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None, data=None):
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求结果返回码
        self.code = code  # type: str
        # 企业服务群成员列表
        self.data = data  # type: list[EnterpriseDingtalkGroupMember]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersResponseBody, self).to_map()
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = EnterpriseDingtalkGroupMember()
                self.data.append(temp_model.from_map(k))
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnterpriseDingtalkGroupCustomerMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersResponse, self).to_map()
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
            temp_model = ListEnterpriseDingtalkGroupCustomerMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseDingtalkGroupsResponseBodyData(TeaModel):
    def __init__(self, open_group_id=None, group_name=None):
        # 钉群ID
        self.open_group_id = open_group_id  # type: str
        # 钉群名
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ListEnterpriseDingtalkGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None, data=None):
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求结果返回码
        self.code = code  # type: str
        # 服务钉群数组
        self.data = data  # type: list[ListEnterpriseDingtalkGroupsResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponseBody, self).to_map()
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEnterpriseDingtalkGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListEnterpriseDingtalkGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnterpriseDingtalkGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponse, self).to_map()
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
            temp_model = ListEnterpriseDingtalkGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(self, open_group_id=None, mobiles=None):
        self.open_group_id = open_group_id  # type: str
        self.mobiles = mobiles  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest(TeaModel):
    def __init__(self, open_group_id=None, mobiles_shrink=None):
        self.open_group_id = open_group_id  # type: str
        self.mobiles_shrink = mobiles_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None):
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求结果返回码
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody, self).to_map()
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


class DeleteEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberResponse, self).to_map()
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
            temp_model = DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(self, open_group_id=None, mobile=None):
        self.open_group_id = open_group_id  # type: str
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None, data=None):
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求结果返回码
        self.code = code  # type: str
        # 成员信息列表
        self.data = data  # type: EnterpriseDingtalkGroupMember

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberResponseBody, self).to_map()
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = EnterpriseDingtalkGroupMember()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnterpriseDingtalkGroupCustomerMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberResponse, self).to_map()
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
            temp_model = GetEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupRequest(TeaModel):
    def __init__(self, open_group_id=None):
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupResponseBodyData(TeaModel):
    def __init__(self, open_group_id=None, group_name=None):
        # 企业服务群的ID
        self.open_group_id = open_group_id  # type: str
        # 企业服务群的群名
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetEnterpriseDingtalkGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, data=None, code=None):
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        self.data = data  # type: GetEnterpriseDingtalkGroupResponseBodyData
        # 接口请求结果返回码
        self.code = code  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetEnterpriseDingtalkGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetEnterpriseDingtalkGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnterpriseDingtalkGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponse, self).to_map()
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
            temp_model = GetEnterpriseDingtalkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


