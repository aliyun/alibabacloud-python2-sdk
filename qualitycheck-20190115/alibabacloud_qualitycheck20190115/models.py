# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddBusinessCategoryRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBusinessCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddBusinessCategoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBusinessCategoryResponseBody, self).to_map()
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


class AddBusinessCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddBusinessCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBusinessCategoryResponse, self).to_map()
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
            temp_model = AddBusinessCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRuleCategoryRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRuleCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddRuleCategoryResponseBodyData(TeaModel):
    def __init__(self, select=None):
        self.select = select  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRuleCategoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        return self


class AddRuleCategoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AddRuleCategoryResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddRuleCategoryResponseBody, self).to_map()
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
            temp_model = AddRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRuleCategoryResponse, self).to_map()
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
            temp_model = AddRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddThesaurusForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddThesaurusForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddThesaurusForApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddThesaurusForApiResponseBody, self).to_map()
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


class AddThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddThesaurusForApiResponse, self).to_map()
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
            temp_model = AddThesaurusForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignReviewerRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssignReviewerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AssignReviewerResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssignReviewerResponseBody, self).to_map()
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


class AssignReviewerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssignReviewerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssignReviewerResponse, self).to_map()
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
            temp_model = AssignReviewerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsrVocabRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsrVocabRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateAsrVocabResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsrVocabResponseBody, self).to_map()
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


class CreateAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAsrVocabResponse, self).to_map()
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
            temp_model = CreateAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSkillGroupConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSkillGroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSkillGroupConfigResponseBody, self).to_map()
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


class CreateSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSkillGroupConfigResponse, self).to_map()
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
            temp_model = CreateSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskAssignRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskAssignRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskAssignRuleResponseBody, self).to_map()
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


class CreateTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskAssignRuleResponse, self).to_map()
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
            temp_model = CreateTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
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


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserResponse, self).to_map()
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWarningConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWarningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateWarningConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWarningConfigResponseBody, self).to_map()
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


class CreateWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWarningConfigResponse, self).to_map()
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
            temp_model = CreateWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelRuleCategoryRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelRuleCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DelRuleCategoryResponseBodyData(TeaModel):
    def __init__(self, select=None):
        self.select = select  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelRuleCategoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        return self


class DelRuleCategoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DelRuleCategoryResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DelRuleCategoryResponseBody, self).to_map()
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
            temp_model = DelRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DelRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DelRuleCategoryResponse, self).to_map()
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
            temp_model = DelRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelThesaurusForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelThesaurusForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DelThesaurusForApiResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelThesaurusForApiResponseBody, self).to_map()
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


class DelThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DelThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DelThesaurusForApiResponse, self).to_map()
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
            temp_model = DelThesaurusForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsrVocabRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsrVocabRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteAsrVocabResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsrVocabResponseBody, self).to_map()
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


class DeleteAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAsrVocabResponse, self).to_map()
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
            temp_model = DeleteAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBusinessCategoryRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBusinessCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteBusinessCategoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBusinessCategoryResponseBody, self).to_map()
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


class DeleteBusinessCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBusinessCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBusinessCategoryResponse, self).to_map()
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
            temp_model = DeleteBusinessCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizationConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteCustomizationConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizationConfigResponseBody, self).to_map()
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


class DeleteCustomizationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCustomizationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomizationConfigResponse, self).to_map()
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
            temp_model = DeleteCustomizationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSetResponseBody, self).to_map()
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


class DeleteDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSetResponse, self).to_map()
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
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrecisionTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrecisionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeletePrecisionTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrecisionTaskResponseBody, self).to_map()
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


class DeletePrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrecisionTaskResponse, self).to_map()
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
            temp_model = DeletePrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScoreForApiResponseBody, self).to_map()
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


class DeleteScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScoreForApiResponse, self).to_map()
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
            temp_model = DeleteScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSkillGroupConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSkillGroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSkillGroupConfigResponseBody, self).to_map()
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


class DeleteSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSkillGroupConfigResponse, self).to_map()
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
            temp_model = DeleteSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteSubScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubScoreForApiResponseBody, self).to_map()
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


class DeleteSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubScoreForApiResponse, self).to_map()
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
            temp_model = DeleteSubScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskAssignRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTaskAssignRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTaskAssignRuleResponseBody, self).to_map()
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


class DeleteTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTaskAssignRuleResponse, self).to_map()
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
            temp_model = DeleteTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
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


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWarningConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWarningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteWarningConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWarningConfigResponseBody, self).to_map()
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


class DeleteWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWarningConfigResponse, self).to_map()
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
            temp_model = DeleteWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditThesaurusForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditThesaurusForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class EditThesaurusForApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditThesaurusForApiResponseBody, self).to_map()
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


class EditThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditThesaurusForApiResponse, self).to_map()
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
            temp_model = EditThesaurusForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsrVocabRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsrVocabRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetAsrVocabResponseBodyDataWordsWord(TeaModel):
    def __init__(self, weight=None, word=None):
        self.weight = weight  # type: int
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsrVocabResponseBodyDataWordsWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class GetAsrVocabResponseBodyDataWords(TeaModel):
    def __init__(self, word=None):
        self.word = word  # type: list[GetAsrVocabResponseBodyDataWordsWord]

    def validate(self):
        if self.word:
            for k in self.word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAsrVocabResponseBodyDataWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Word'] = []
        if self.word is not None:
            for k in self.word:
                result['Word'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.word = []
        if m.get('Word') is not None:
            for k in m.get('Word'):
                temp_model = GetAsrVocabResponseBodyDataWordsWord()
                self.word.append(temp_model.from_map(k))
        return self


class GetAsrVocabResponseBodyData(TeaModel):
    def __init__(self, name=None, words=None):
        self.name = name  # type: str
        self.words = words  # type: GetAsrVocabResponseBodyDataWords

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        _map = super(GetAsrVocabResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.words is not None:
            result['Words'] = self.words.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Words') is not None:
            temp_model = GetAsrVocabResponseBodyDataWords()
            self.words = temp_model.from_map(m['Words'])
        return self


class GetAsrVocabResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetAsrVocabResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAsrVocabResponseBody, self).to_map()
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
            temp_model = GetAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsrVocabResponse, self).to_map()
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
            temp_model = GetAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBusinessCategoryListRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBusinessCategoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo(TeaModel):
    def __init__(self, bid=None, business_name=None, service_type=None):
        self.bid = bid  # type: int
        self.business_name = business_name  # type: str
        self.service_type = service_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class GetBusinessCategoryListResponseBodyData(TeaModel):
    def __init__(self, business_category_basic_info=None):
        self.business_category_basic_info = business_category_basic_info  # type: list[GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo]

    def validate(self):
        if self.business_category_basic_info:
            for k in self.business_category_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetBusinessCategoryListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k in m.get('BusinessCategoryBasicInfo'):
                temp_model = GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k))
        return self


class GetBusinessCategoryListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetBusinessCategoryListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetBusinessCategoryListResponseBody, self).to_map()
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
            temp_model = GetBusinessCategoryListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBusinessCategoryListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBusinessCategoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBusinessCategoryListResponse, self).to_map()
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
            temp_model = GetBusinessCategoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomizationConfigListRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomizationConfigListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo(TeaModel):
    def __init__(self, create_time=None, mode_customization_id=None, model_id=None, model_name=None,
                 model_status=None, task_type=None):
        self.create_time = create_time  # type: str
        self.mode_customization_id = mode_customization_id  # type: str
        self.model_id = model_id  # type: long
        self.model_name = model_name  # type: str
        self.model_status = model_status  # type: int
        self.task_type = task_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetCustomizationConfigListResponseBodyData(TeaModel):
    def __init__(self, model_customization_data_set_po=None):
        self.model_customization_data_set_po = model_customization_data_set_po  # type: list[GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo]

    def validate(self):
        if self.model_customization_data_set_po:
            for k in self.model_customization_data_set_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCustomizationConfigListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelCustomizationDataSetPo'] = []
        if self.model_customization_data_set_po is not None:
            for k in self.model_customization_data_set_po:
                result['ModelCustomizationDataSetPo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.model_customization_data_set_po = []
        if m.get('ModelCustomizationDataSetPo') is not None:
            for k in m.get('ModelCustomizationDataSetPo'):
                temp_model = GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo()
                self.model_customization_data_set_po.append(temp_model.from_map(k))
        return self


class GetCustomizationConfigListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCustomizationConfigListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCustomizationConfigListResponseBody, self).to_map()
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
            temp_model = GetCustomizationConfigListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomizationConfigListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCustomizationConfigListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomizationConfigListResponse, self).to_map()
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
            temp_model = GetCustomizationConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHitResultRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHitResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetHitResultResponseBodyDataResultInfo(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHitResultResponseBodyDataResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetHitResultResponseBodyData(TeaModel):
    def __init__(self, result_info=None):
        self.result_info = result_info  # type: list[GetHitResultResponseBodyDataResultInfo]

    def validate(self):
        if self.result_info:
            for k in self.result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHitResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k in self.result_info:
                result['ResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k in m.get('ResultInfo'):
                temp_model = GetHitResultResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k))
        return self


class GetHitResultResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: GetHitResultResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHitResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = GetHitResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHitResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHitResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHitResultResponse, self).to_map()
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
            temp_model = GetHitResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNextResultToVerifyRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNextResultToVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource(TeaModel):
    def __init__(self, line=None, position=None):
        self.line = line  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine
        self.position = position  # type: int

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget(TeaModel):
    def __init__(self, line=None, position=None):
        self.line = line  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine
        self.position = position  # type: int

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta(TeaModel):
    def __init__(self, source=None, target=None, type=None):
        self.source = source  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource
        self.target = target  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget
        self.type = type  # type: str

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas(TeaModel):
    def __init__(self, delta=None):
        self.delta = delta  # type: list[GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta]

    def validate(self):
        if self.delta:
            for k in self.delta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delta'] = []
        if self.delta is not None:
            for k in self.delta:
                result['Delta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k in m.get('Delta'):
                temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta()
                self.delta.append(temp_model.from_map(k))
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(self, begin=None, begin_time=None, deltas=None, emotion_value=None, end=None, hour_min_sec=None,
                 identity=None, incorrect_words=None, role=None, silence_duration=None, source_role=None, source_words=None,
                 speech_rate=None, words=None):
        self.begin = begin  # type: long
        self.begin_time = begin_time  # type: str
        self.deltas = deltas  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.hour_min_sec = hour_min_sec  # type: str
        self.identity = identity  # type: str
        self.incorrect_words = incorrect_words  # type: int
        self.role = role  # type: str
        self.silence_duration = silence_duration  # type: int
        self.source_role = source_role  # type: str
        self.source_words = source_words  # type: str
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        if self.deltas:
            self.deltas.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialoguesDialogue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.deltas is not None:
            result['Deltas'] = self.deltas.to_map()
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.source_words is not None:
            result['SourceWords'] = self.source_words
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Deltas') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas()
            self.deltas = temp_model.from_map(m['Deltas'])
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('SourceWords') is not None:
            self.source_words = m.get('SourceWords')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetNextResultToVerifyResponseBodyDataDialogues(TeaModel):
    def __init__(self, dialogue=None):
        self.dialogue = dialogue  # type: list[GetNextResultToVerifyResponseBodyDataDialoguesDialogue]

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyDataDialogues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k in self.dialogue:
                result['Dialogue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k in m.get('Dialogue'):
                temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class GetNextResultToVerifyResponseBodyData(TeaModel):
    def __init__(self, audio_scheme=None, audio_url=None, dialogues=None, duration=None, file_id=None,
                 file_name=None, incorrect_words=None, index=None, precision=None, status=None, total_count=None,
                 update_time=None, verified=None, verified_count=None):
        self.audio_scheme = audio_scheme  # type: str
        self.audio_url = audio_url  # type: str
        self.dialogues = dialogues  # type: GetNextResultToVerifyResponseBodyDataDialogues
        self.duration = duration  # type: int
        self.file_id = file_id  # type: str
        self.file_name = file_name  # type: str
        self.incorrect_words = incorrect_words  # type: int
        self.index = index  # type: int
        self.precision = precision  # type: float
        self.status = status  # type: int
        self.total_count = total_count  # type: int
        self.update_time = update_time  # type: str
        self.verified = verified  # type: bool
        self.verified_count = verified_count  # type: int

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.index is not None:
            result['Index'] = self.index
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified is not None:
            result['Verified'] = self.verified
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('Dialogues') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Verified') is not None:
            self.verified = m.get('Verified')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class GetNextResultToVerifyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetNextResultToVerifyResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponseBody, self).to_map()
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
            temp_model = GetNextResultToVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNextResultToVerifyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNextResultToVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNextResultToVerifyResponse, self).to_map()
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
            temp_model = GetNextResultToVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrecisionTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrecisionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetPrecisionTaskResponseBodyDataPrecisionsPrecision(TeaModel):
    def __init__(self, model_id=None, model_name=None, precision=None, status=None, task_id=None):
        self.model_id = model_id  # type: long
        self.model_name = model_name  # type: str
        self.precision = precision  # type: float
        self.status = status  # type: int
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrecisionTaskResponseBodyDataPrecisionsPrecision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetPrecisionTaskResponseBodyDataPrecisions(TeaModel):
    def __init__(self, precision=None):
        self.precision = precision  # type: list[GetPrecisionTaskResponseBodyDataPrecisionsPrecision]

    def validate(self):
        if self.precision:
            for k in self.precision:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPrecisionTaskResponseBodyDataPrecisions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Precision'] = []
        if self.precision is not None:
            for k in self.precision:
                result['Precision'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.precision = []
        if m.get('Precision') is not None:
            for k in m.get('Precision'):
                temp_model = GetPrecisionTaskResponseBodyDataPrecisionsPrecision()
                self.precision.append(temp_model.from_map(k))
        return self


class GetPrecisionTaskResponseBodyData(TeaModel):
    def __init__(self, data_set_id=None, data_set_name=None, duration=None, incorrect_words=None, name=None,
                 precisions=None, source=None, status=None, task_id=None, total_count=None, update_time=None,
                 verified_count=None):
        self.data_set_id = data_set_id  # type: long
        self.data_set_name = data_set_name  # type: str
        self.duration = duration  # type: int
        self.incorrect_words = incorrect_words  # type: int
        self.name = name  # type: str
        self.precisions = precisions  # type: GetPrecisionTaskResponseBodyDataPrecisions
        self.source = source  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.total_count = total_count  # type: int
        self.update_time = update_time  # type: str
        self.verified_count = verified_count  # type: int

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        _map = super(GetPrecisionTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.name is not None:
            result['Name'] = self.name
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Precisions') is not None:
            temp_model = GetPrecisionTaskResponseBodyDataPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class GetPrecisionTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetPrecisionTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPrecisionTaskResponseBody, self).to_map()
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
            temp_model = GetPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrecisionTaskResponse, self).to_map()
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
            temp_model = GetPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResultRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultResponseBodyDataResultInfoAgent(TeaModel):
    def __init__(self, id=None, name=None, skill_group=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.skill_group = skill_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoAgent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        return self


class GetResultResponseBodyDataResultInfoAsrResultAsrResult(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, role=None, speech_rate=None, words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = role  # type: str
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoAsrResultAsrResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultResponseBodyDataResultInfoAsrResult(TeaModel):
    def __init__(self, asr_result=None):
        self.asr_result = asr_result  # type: list[GetResultResponseBodyDataResultInfoAsrResultAsrResult]

    def validate(self):
        if self.asr_result:
            for k in self.asr_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoAsrResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['AsrResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k in m.get('AsrResult'):
                temp_model = GetResultResponseBodyDataResultInfoAsrResultAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord(TeaModel):
    def __init__(self, cid=None, from_=None, to=None, val=None):
        self.cid = cid  # type: str
        self.from_ = from_  # type: int
        self.to = to  # type: int
        self.val = val  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords(TeaModel):
    def __init__(self, key_word=None):
        self.key_word = key_word  # type: list[GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord]

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyWord'] = []
        if self.key_word is not None:
            for k in self.key_word:
                result['KeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_word = []
        if m.get('KeyWord') is not None:
            for k in m.get('KeyWord'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, role=None, words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: int
        self.role = role  # type: str
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit(TeaModel):
    def __init__(self, cid=None, key_words=None, phrase=None):
        self.cid = cid  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid
        self.key_words = key_words  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords
        self.phrase = phrase  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase

    def validate(self):
        if self.cid:
            self.cid.validate()
        if self.key_words:
            self.key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid()
            self.cid = temp_model.from_map(m['Cid'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Phrase') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHits(TeaModel):
    def __init__(self, hit=None):
        self.hit = hit  # type: list[GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit]

    def validate(self):
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResultHits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hit'] = []
        if self.hit is not None:
            for k in self.hit:
                result['Hit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k in m.get('Hit'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit()
                self.hit.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResult(TeaModel):
    def __init__(self, hits=None, name=None, review_result=None, rid=None, type=None):
        self.hits = hits  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHits
        self.name = name  # type: str
        self.review_result = review_result  # type: int
        self.rid = rid  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.hits:
            self.hits.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResultHitResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hits is not None:
            result['Hits'] = self.hits.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hits') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHits()
            self.hits = temp_model.from_map(m['Hits'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultResponseBodyDataResultInfoHitResult(TeaModel):
    def __init__(self, hit_result=None):
        self.hit_result = hit_result  # type: list[GetResultResponseBodyDataResultInfoHitResultHitResult]

    def validate(self):
        if self.hit_result:
            for k in self.hit_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitResult'] = []
        if self.hit_result is not None:
            for k in self.hit_result:
                result['HitResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k in m.get('HitResult'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResult()
                self.hit_result.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitScoreHitScore(TeaModel):
    def __init__(self, rule_id=None, score_id=None, score_name=None, score_number=None):
        self.rule_id = rule_id  # type: str
        self.score_id = score_id  # type: str
        self.score_name = score_name  # type: str
        self.score_number = score_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitScoreHitScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_number is not None:
            result['ScoreNumber'] = self.score_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreNumber') is not None:
            self.score_number = m.get('ScoreNumber')
        return self


class GetResultResponseBodyDataResultInfoHitScore(TeaModel):
    def __init__(self, hit_score=None):
        self.hit_score = hit_score  # type: list[GetResultResponseBodyDataResultInfoHitScoreHitScore]

    def validate(self):
        if self.hit_score:
            for k in self.hit_score:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoHitScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitScore'] = []
        if self.hit_score is not None:
            for k in self.hit_score:
                result['HitScore'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit_score = []
        if m.get('HitScore') is not None:
            for k in m.get('HitScore'):
                temp_model = GetResultResponseBodyDataResultInfoHitScoreHitScore()
                self.hit_score.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoRecording(TeaModel):
    def __init__(self, business=None, call_id=None, call_time=None, call_type=None, callee=None, caller=None,
                 data_set_name=None, dialogue_size=None, duration=None, id=None, name=None, primary_id=None, remark_1=None,
                 remark_10=None, remark_11=None, remark_12=None, remark_13=None, remark_2=None, remark_3=None, remark_4=None,
                 remark_5=None, remark_6=None, remark_7=None, remark_8=None, remark_9=None, url=None):
        self.business = business  # type: str
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.call_type = call_type  # type: int
        self.callee = callee  # type: str
        self.caller = caller  # type: str
        self.data_set_name = data_set_name  # type: str
        self.dialogue_size = dialogue_size  # type: int
        self.duration = duration  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.primary_id = primary_id  # type: str
        self.remark_1 = remark_1  # type: str
        self.remark_10 = remark_10  # type: str
        self.remark_11 = remark_11  # type: str
        self.remark_12 = remark_12  # type: str
        self.remark_13 = remark_13  # type: str
        self.remark_2 = remark_2  # type: str
        self.remark_3 = remark_3  # type: str
        self.remark_4 = remark_4  # type: str
        self.remark_5 = remark_5  # type: long
        self.remark_6 = remark_6  # type: str
        self.remark_7 = remark_7  # type: str
        self.remark_8 = remark_8  # type: str
        self.remark_9 = remark_9  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfoRecording, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.dialogue_size is not None:
            result['DialogueSize'] = self.dialogue_size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.remark_10 is not None:
            result['Remark10'] = self.remark_10
        if self.remark_11 is not None:
            result['Remark11'] = self.remark_11
        if self.remark_12 is not None:
            result['Remark12'] = self.remark_12
        if self.remark_13 is not None:
            result['Remark13'] = self.remark_13
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.remark_4 is not None:
            result['Remark4'] = self.remark_4
        if self.remark_5 is not None:
            result['Remark5'] = self.remark_5
        if self.remark_6 is not None:
            result['Remark6'] = self.remark_6
        if self.remark_7 is not None:
            result['Remark7'] = self.remark_7
        if self.remark_8 is not None:
            result['Remark8'] = self.remark_8
        if self.remark_9 is not None:
            result['Remark9'] = self.remark_9
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DialogueSize') is not None:
            self.dialogue_size = m.get('DialogueSize')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('Remark10') is not None:
            self.remark_10 = m.get('Remark10')
        if m.get('Remark11') is not None:
            self.remark_11 = m.get('Remark11')
        if m.get('Remark12') is not None:
            self.remark_12 = m.get('Remark12')
        if m.get('Remark13') is not None:
            self.remark_13 = m.get('Remark13')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Remark4') is not None:
            self.remark_4 = m.get('Remark4')
        if m.get('Remark5') is not None:
            self.remark_5 = m.get('Remark5')
        if m.get('Remark6') is not None:
            self.remark_6 = m.get('Remark6')
        if m.get('Remark7') is not None:
            self.remark_7 = m.get('Remark7')
        if m.get('Remark8') is not None:
            self.remark_8 = m.get('Remark8')
        if m.get('Remark9') is not None:
            self.remark_9 = m.get('Remark9')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetResultResponseBodyDataResultInfo(TeaModel):
    def __init__(self, agent=None, asr_result=None, assignment_time=None, comments=None, create_time=None,
                 create_time_long=None, error_message=None, hit_result=None, hit_score=None, last_data_id=None, recording=None,
                 resolver=None, review_result=None, review_status=None, review_time=None, review_time_long=None,
                 review_type=None, reviewer=None, score=None, status=None, task_id=None, task_name=None):
        self.agent = agent  # type: GetResultResponseBodyDataResultInfoAgent
        self.asr_result = asr_result  # type: GetResultResponseBodyDataResultInfoAsrResult
        self.assignment_time = assignment_time  # type: str
        self.comments = comments  # type: str
        self.create_time = create_time  # type: str
        self.create_time_long = create_time_long  # type: str
        self.error_message = error_message  # type: str
        self.hit_result = hit_result  # type: GetResultResponseBodyDataResultInfoHitResult
        self.hit_score = hit_score  # type: GetResultResponseBodyDataResultInfoHitScore
        self.last_data_id = last_data_id  # type: str
        self.recording = recording  # type: GetResultResponseBodyDataResultInfoRecording
        self.resolver = resolver  # type: str
        self.review_result = review_result  # type: int
        self.review_status = review_status  # type: int
        self.review_time = review_time  # type: str
        self.review_time_long = review_time_long  # type: str
        self.review_type = review_type  # type: int
        self.reviewer = reviewer  # type: str
        self.score = score  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            self.asr_result.validate()
        if self.hit_result:
            self.hit_result.validate()
        if self.hit_score:
            self.hit_score.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyDataResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        if self.asr_result is not None:
            result['AsrResult'] = self.asr_result.to_map()
        if self.assignment_time is not None:
            result['AssignmentTime'] = self.assignment_time
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.hit_result is not None:
            result['HitResult'] = self.hit_result.to_map()
        if self.hit_score is not None:
            result['HitScore'] = self.hit_score.to_map()
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.review_time_long is not None:
            result['ReviewTimeLong'] = self.review_time_long
        if self.review_type is not None:
            result['ReviewType'] = self.review_type
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.score is not None:
            result['Score'] = self.score
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAgent()
            self.agent = temp_model.from_map(m['Agent'])
        if m.get('AsrResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAsrResult()
            self.asr_result = temp_model.from_map(m['AsrResult'])
        if m.get('AssignmentTime') is not None:
            self.assignment_time = m.get('AssignmentTime')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HitResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResult()
            self.hit_result = temp_model.from_map(m['HitResult'])
        if m.get('HitScore') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitScore()
            self.hit_score = temp_model.from_map(m['HitScore'])
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('Recording') is not None:
            temp_model = GetResultResponseBodyDataResultInfoRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('ReviewTimeLong') is not None:
            self.review_time_long = m.get('ReviewTimeLong')
        if m.get('ReviewType') is not None:
            self.review_type = m.get('ReviewType')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetResultResponseBodyData(TeaModel):
    def __init__(self, result_info=None):
        self.result_info = result_info  # type: list[GetResultResponseBodyDataResultInfo]

    def validate(self):
        if self.result_info:
            for k in self.result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k in self.result_info:
                result['ResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k in m.get('ResultInfo'):
                temp_model = GetResultResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k))
        return self


class GetResultResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, result_count_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: GetResultResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.result_count_id = result_count_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = GetResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResultResponse, self).to_map()
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
            temp_model = GetResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResultCallbackRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultCallbackResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultCallbackResponseBody, self).to_map()
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


class GetResultCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResultCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResultCallbackResponse, self).to_map()
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
            temp_model = GetResultCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResultToReviewRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultToReviewResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(self, begin=None, begin_time=None, emotion_value=None, end=None, hour_min_sec=None, identity=None,
                 role=None, silence_duration=None, speech_rate=None, words=None):
        self.begin = begin  # type: long
        self.begin_time = begin_time  # type: str
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.hour_min_sec = hour_min_sec  # type: str
        self.identity = identity  # type: str
        self.role = role  # type: str
        self.silence_duration = silence_duration  # type: int
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataDialoguesDialogue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultToReviewResponseBodyDataDialogues(TeaModel):
    def __init__(self, dialogue=None):
        self.dialogue = dialogue  # type: list[GetResultToReviewResponseBodyDataDialoguesDialogue]

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataDialogues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k in self.dialogue:
                result['Dialogue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k in m.get('Dialogue'):
                temp_model = GetResultToReviewResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories(TeaModel):
    def __init__(self, comments=None, operation_time=None, operation_type=None, operator=None, operator_name=None):
        self.comments = comments  # type: str
        self.operation_time = operation_time  # type: str
        self.operation_type = operation_type  # type: int
        self.operator = operator  # type: long
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories(TeaModel):
    def __init__(self, complain_histories=None):
        self.complain_histories = complain_histories  # type: list[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories]

    def validate(self):
        if self.complain_histories:
            for k in self.complain_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k in self.complain_histories:
                result['ComplainHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k in m.get('ComplainHistories'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(self, cid=None, from_=None, pid=None, tid=None, to=None, val=None):
        self.cid = cid  # type: str
        self.from_ = from_  # type: int
        self.pid = pid  # type: int
        self.tid = tid  # type: str
        self.to = to  # type: int
        self.val = val  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.to is not None:
            result['To'] = self.to
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(TeaModel):
    def __init__(self, key_word=None):
        self.key_word = key_word  # type: list[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord]

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyWord'] = []
        if self.key_word is not None:
            for k in self.key_word:
                result['KeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_word = []
        if m.get('KeyWord') is not None:
            for k in m.get('KeyWord'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, identity=None, pid=None, role=None, words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.identity = identity  # type: str
        self.pid = pid  # type: int
        self.role = role  # type: str
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.role is not None:
            result['Role'] = self.role
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(self, cid=None, key_words=None, phrase=None):
        self.cid = cid  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid
        self.key_words = key_words  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords
        self.phrase = phrase  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase

    def validate(self):
        if self.cid:
            self.cid.validate()
        if self.key_words:
            self.key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Phrase') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(TeaModel):
    def __init__(self, condition_hit_info=None):
        self.condition_hit_info = condition_hit_info  # type: list[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo]

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k in self.condition_hit_info:
                result['ConditionHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k in m.get('ConditionHitInfo'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo(TeaModel):
    def __init__(self, hit_id=None, review_result=None, review_time=None, reviewer=None, rid=None):
        self.hit_id = hit_id  # type: str
        self.review_result = review_result  # type: int
        self.review_time = review_time  # type: str
        self.reviewer = reviewer  # type: str
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_id is not None:
            result['HitId'] = self.hit_id
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(self, auto_review=None, complain_histories=None, complainable=None, condition_hit_info_list=None,
                 review_info=None, rid=None, rule_name=None, score_id=None, score_num=None, score_sub_id=None,
                 score_sub_name=None):
        self.auto_review = auto_review  # type: int
        self.complain_histories = complain_histories  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories
        self.complainable = complainable  # type: bool
        self.condition_hit_info_list = condition_hit_info_list  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList
        self.review_info = review_info  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str
        self.score_id = score_id  # type: long
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.score_sub_name = score_sub_name  # type: str

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ConditionHitInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('ReviewInfo') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m['ReviewInfo'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(self, hit_rule_review_info=None):
        self.hit_rule_review_info = hit_rule_review_info  # type: list[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo]

    def validate(self):
        if self.hit_rule_review_info:
            for k in self.hit_rule_review_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataHitRuleReviewInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitRuleReviewInfo'] = []
        if self.hit_rule_review_info is not None:
            for k in self.hit_rule_review_info:
                result['HitRuleReviewInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit_rule_review_info = []
        if m.get('HitRuleReviewInfo') is not None:
            for k in m.get('HitRuleReviewInfo'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories(TeaModel):
    def __init__(self, comments=None, operation_time=None, operation_type=None, operator=None, operator_name=None):
        self.comments = comments  # type: str
        self.operation_time = operation_time  # type: str
        self.operation_type = operation_type  # type: int
        self.operator = operator  # type: long
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories(TeaModel):
    def __init__(self, complain_histories=None):
        self.complain_histories = complain_histories  # type: list[GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories]

    def validate(self):
        if self.complain_histories:
            for k in self.complain_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k in self.complain_histories:
                result['ComplainHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k in m.get('ComplainHistories'):
                temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo(TeaModel):
    def __init__(self, complain_histories=None, complainable=None, score_id=None, score_num=None, score_sub_id=None,
                 score_sub_name=None):
        self.complain_histories = complain_histories  # type: GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories
        self.complainable = complainable  # type: bool
        self.score_id = score_id  # type: long
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.score_sub_name = score_sub_name  # type: str

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoList(TeaModel):
    def __init__(self, manual_score_info=None):
        self.manual_score_info = manual_score_info  # type: list[GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo]

    def validate(self):
        if self.manual_score_info:
            for k in self.manual_score_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataManualScoreInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManualScoreInfo'] = []
        if self.manual_score_info is not None:
            for k in self.manual_score_info:
                result['ManualScoreInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.manual_score_info = []
        if m.get('ManualScoreInfo') is not None:
            for k in m.get('ManualScoreInfo'):
                temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo()
                self.manual_score_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory(TeaModel):
    def __init__(self, complain_result=None, old_score=None, operator_name=None, review_result=None, score=None,
                 time_str=None, type=None):
        self.complain_result = complain_result  # type: int
        self.old_score = old_score  # type: int
        self.operator_name = operator_name  # type: str
        self.review_result = review_result  # type: int
        self.score = score  # type: int
        self.time_str = time_str  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complain_result is not None:
            result['ComplainResult'] = self.complain_result
        if self.old_score is not None:
            result['OldScore'] = self.old_score
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.score is not None:
            result['Score'] = self.score
        if self.time_str is not None:
            result['TimeStr'] = self.time_str
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComplainResult') is not None:
            self.complain_result = m.get('ComplainResult')
        if m.get('OldScore') is not None:
            self.old_score = m.get('OldScore')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TimeStr') is not None:
            self.time_str = m.get('TimeStr')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultToReviewResponseBodyDataReviewHistoryList(TeaModel):
    def __init__(self, review_history=None):
        self.review_history = review_history  # type: list[GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory]

    def validate(self):
        if self.review_history:
            for k in self.review_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyDataReviewHistoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewHistory'] = []
        if self.review_history is not None:
            for k in self.review_history:
                result['ReviewHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.review_history = []
        if m.get('ReviewHistory') is not None:
            for k in m.get('ReviewHistory'):
                temp_model = GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory()
                self.review_history.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyData(TeaModel):
    def __init__(self, audio_scheme=None, audio_url=None, comments=None, dialogues=None, file_id=None,
                 file_merge_name=None, hit_rule_review_info_list=None, manual_score_info_list=None, review_history_list=None,
                 status=None, total_score=None, vid=None):
        self.audio_scheme = audio_scheme  # type: str
        self.audio_url = audio_url  # type: str
        self.comments = comments  # type: str
        self.dialogues = dialogues  # type: GetResultToReviewResponseBodyDataDialogues
        self.file_id = file_id  # type: str
        self.file_merge_name = file_merge_name  # type: str
        self.hit_rule_review_info_list = hit_rule_review_info_list  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoList
        self.manual_score_info_list = manual_score_info_list  # type: GetResultToReviewResponseBodyDataManualScoreInfoList
        self.review_history_list = review_history_list  # type: GetResultToReviewResponseBodyDataReviewHistoryList
        self.status = status  # type: int
        self.total_score = total_score  # type: int
        self.vid = vid  # type: str

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_info_list:
            self.manual_score_info_list.validate()
        if self.review_history_list:
            self.review_history_list.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.manual_score_info_list is not None:
            result['ManualScoreInfoList'] = self.manual_score_info_list.to_map()
        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Dialogues') is not None:
            temp_model = GetResultToReviewResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('ManualScoreInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoList()
            self.manual_score_info_list = temp_model.from_map(m['ManualScoreInfoList'])
        if m.get('ReviewHistoryList') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewHistoryList()
            self.review_history_list = temp_model.from_map(m['ReviewHistoryList'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetResultToReviewResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetResultToReviewResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponseBody, self).to_map()
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
            temp_model = GetResultToReviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultToReviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResultToReviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResultToReviewResponse, self).to_map()
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
            temp_model = GetResultToReviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList(TeaModel):
    def __init__(self, business_category_name_list=None):
        self.business_category_name_list = business_category_name_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        return self


class GetRuleResponseBodyDataRulesRuleInfo(TeaModel):
    def __init__(self, auto_review=None, business_category_name_list=None, comments=None, create_empid=None,
                 create_time=None, end_time=None, is_delete=None, is_online=None, last_update_empid=None, last_update_time=None,
                 name=None, rid=None, rule_lambda=None, rule_score_type=None, score_id=None, score_name=None,
                 score_sub_id=None, score_sub_name=None, start_time=None, status=None, type=None, weight=None):
        self.auto_review = auto_review  # type: int
        self.business_category_name_list = business_category_name_list  # type: GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList
        self.comments = comments  # type: str
        self.create_empid = create_empid  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.is_delete = is_delete  # type: int
        self.is_online = is_online  # type: int
        self.last_update_empid = last_update_empid  # type: str
        self.last_update_time = last_update_time  # type: str
        self.name = name  # type: str
        self.rid = rid  # type: str
        self.rule_lambda = rule_lambda  # type: str
        self.rule_score_type = rule_score_type  # type: int
        self.score_id = score_id  # type: int
        self.score_name = score_name  # type: str
        self.score_sub_id = score_sub_id  # type: int
        self.score_sub_name = score_sub_name  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.weight = weight  # type: str

    def validate(self):
        if self.business_category_name_list:
            self.business_category_name_list.validate()

    def to_map(self):
        _map = super(GetRuleResponseBodyDataRulesRuleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list.to_map()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('BusinessCategoryNameList') is not None:
            temp_model = GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList()
            self.business_category_name_list = temp_model.from_map(m['BusinessCategoryNameList'])
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class GetRuleResponseBodyDataRules(TeaModel):
    def __init__(self, rule_info=None):
        self.rule_info = rule_info  # type: list[GetRuleResponseBodyDataRulesRuleInfo]

    def validate(self):
        if self.rule_info:
            for k in self.rule_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleInfo'] = []
        if self.rule_info is not None:
            for k in self.rule_info:
                result['RuleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_info = []
        if m.get('RuleInfo') is not None:
            for k in m.get('RuleInfo'):
                temp_model = GetRuleResponseBodyDataRulesRuleInfo()
                self.rule_info.append(temp_model.from_map(k))
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(self, rules=None):
        self.rules = rules  # type: GetRuleResponseBodyDataRules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super(GetRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rules') is not None:
            temp_model = GetRuleResponseBodyDataRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRuleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRuleResponseBody, self).to_map()
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
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleResponse, self).to_map()
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
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleCategoryRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleCategoryResponseBodyDataRuleCountInfo(TeaModel):
    def __init__(self, select=None, type=None, type_name=None):
        self.select = select  # type: bool
        self.type = type  # type: int
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleCategoryResponseBodyDataRuleCountInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetRuleCategoryResponseBodyData(TeaModel):
    def __init__(self, rule_count_info=None):
        self.rule_count_info = rule_count_info  # type: list[GetRuleCategoryResponseBodyDataRuleCountInfo]

    def validate(self):
        if self.rule_count_info:
            for k in self.rule_count_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleCategoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleCountInfo'] = []
        if self.rule_count_info is not None:
            for k in self.rule_count_info:
                result['RuleCountInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_count_info = []
        if m.get('RuleCountInfo') is not None:
            for k in m.get('RuleCountInfo'):
                temp_model = GetRuleCategoryResponseBodyDataRuleCountInfo()
                self.rule_count_info.append(temp_model.from_map(k))
        return self


class GetRuleCategoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRuleCategoryResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRuleCategoryResponseBody, self).to_map()
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
            temp_model = GetRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleCategoryResponse, self).to_map()
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
            temp_model = GetRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleDetailRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor(TeaModel):
    def __init__(self, anchor_cid=None, hit_time=None, location=None):
        self.anchor_cid = anchor_cid  # type: str
        self.hit_time = hit_time  # type: int
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_cid is not None:
            result['AnchorCid'] = self.anchor_cid
        if self.hit_time is not None:
            result['HitTime'] = self.hit_time
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorCid') is not None:
            self.anchor_cid = m.get('AnchorCid')
        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange(TeaModel):
    def __init__(self, from_=None, to=None):
        self.from_ = from_  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange(TeaModel):
    def __init__(self, absolute=None, anchor=None, range=None, role=None):
        self.absolute = absolute  # type: bool
        self.anchor = anchor  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor
        self.range = range  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange
        self.role = role  # type: str

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.absolute is not None:
            result['Absolute'] = self.absolute
        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')
        if m.get('Anchor') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Range') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo(TeaModel):
    def __init__(self, ant_model_info=None):
        self.ant_model_info = ant_model_info  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AntModelInfo') is not None:
            self.ant_model_info = m.get('AntModelInfo')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes(TeaModel):
    def __init__(self, excludes=None):
        self.excludes = excludes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords(TeaModel):
    def __init__(self, oper_key_word=None):
        self.oper_key_word = oper_key_word  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oper_key_word is not None:
            result['OperKeyWord'] = self.oper_key_word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperKeyWord') is not None:
            self.oper_key_word = m.get('OperKeyWord')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues(TeaModel):
    def __init__(self, pvalues=None):
        self.pvalues = pvalues  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pvalues') is not None:
            self.pvalues = m.get('Pvalues')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences(TeaModel):
    def __init__(self, reference=None):
        self.reference = reference  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference is not None:
            result['Reference'] = self.reference
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences(TeaModel):
    def __init__(self, similarly_sentence=None):
        self.similarly_sentence = similarly_sentence  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.similarly_sentence is not None:
            result['SimilarlySentence'] = self.similarly_sentence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SimilarlySentence') is not None:
            self.similarly_sentence = m.get('SimilarlySentence')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam(TeaModel):
    def __init__(self, ant_model_info=None, average=None, begin_type=None, check_type=None, compare_operator=None,
                 context_chat_match=None, delay_time=None, different_role=None, excludes=None, from_=None, from_end=None, hit_time=None,
                 in_sentence=None, interval=None, keyword_extension=None, keyword_match_size=None,
                 max_emotion_change_value=None, min_word_size=None, not_regex=None, oper_key_words=None, phrase=None, pvalues=None,
                 references=None, regex=None, score=None, similarity_threshold=None, similarly_sentences=None, target=None,
                 target_role=None, threshold=None, velocity_in_mint=None):
        self.ant_model_info = ant_model_info  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo
        self.average = average  # type: bool
        self.begin_type = begin_type  # type: str
        self.check_type = check_type  # type: int
        self.compare_operator = compare_operator  # type: str
        self.context_chat_match = context_chat_match  # type: bool
        self.delay_time = delay_time  # type: int
        self.different_role = different_role  # type: bool
        self.excludes = excludes  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes
        self.from_ = from_  # type: int
        self.from_end = from_end  # type: bool
        self.hit_time = hit_time  # type: int
        self.in_sentence = in_sentence  # type: bool
        self.interval = interval  # type: int
        self.keyword_extension = keyword_extension  # type: bool
        self.keyword_match_size = keyword_match_size  # type: int
        self.max_emotion_change_value = max_emotion_change_value  # type: int
        self.min_word_size = min_word_size  # type: int
        self.not_regex = not_regex  # type: str
        self.oper_key_words = oper_key_words  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords
        self.phrase = phrase  # type: str
        self.pvalues = pvalues  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues
        self.references = references  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences
        self.regex = regex  # type: str
        self.score = score  # type: int
        self.similarity_threshold = similarity_threshold  # type: float
        self.similarly_sentences = similarly_sentences  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences
        self.target = target  # type: int
        self.target_role = target_role  # type: str
        self.threshold = threshold  # type: float
        self.velocity_in_mint = velocity_in_mint  # type: int

    def validate(self):
        if self.ant_model_info:
            self.ant_model_info.validate()
        if self.excludes:
            self.excludes.validate()
        if self.oper_key_words:
            self.oper_key_words.validate()
        if self.pvalues:
            self.pvalues.validate()
        if self.references:
            self.references.validate()
        if self.similarly_sentences:
            self.similarly_sentences.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info.to_map()
        if self.average is not None:
            result['Average'] = self.average
        if self.begin_type is not None:
            result['BeginType'] = self.begin_type
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator
        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.different_role is not None:
            result['DifferentRole'] = self.different_role
        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.from_end is not None:
            result['FromEnd'] = self.from_end
        if self.hit_time is not None:
            result['HitTime'] = self.hit_time
        if self.in_sentence is not None:
            result['InSentence'] = self.in_sentence
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension
        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size
        if self.max_emotion_change_value is not None:
            result['MaxEmotionChangeValue'] = self.max_emotion_change_value
        if self.min_word_size is not None:
            result['MinWordSize'] = self.min_word_size
        if self.not_regex is not None:
            result['NotRegex'] = self.not_regex
        if self.oper_key_words is not None:
            result['OperKeyWords'] = self.oper_key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase
        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues.to_map()
        if self.references is not None:
            result['References'] = self.references.to_map()
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.score is not None:
            result['Score'] = self.score
        if self.similarity_threshold is not None:
            result['Similarity_threshold'] = self.similarity_threshold
        if self.similarly_sentences is not None:
            result['SimilarlySentences'] = self.similarly_sentences.to_map()
        if self.target is not None:
            result['Target'] = self.target
        if self.target_role is not None:
            result['TargetRole'] = self.target_role
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.velocity_in_mint is not None:
            result['VelocityInMint'] = self.velocity_in_mint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AntModelInfo') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo()
            self.ant_model_info = temp_model.from_map(m['AntModelInfo'])
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')
        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('DifferentRole') is not None:
            self.different_role = m.get('DifferentRole')
        if m.get('Excludes') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes()
            self.excludes = temp_model.from_map(m['Excludes'])
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('FromEnd') is not None:
            self.from_end = m.get('FromEnd')
        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')
        if m.get('InSentence') is not None:
            self.in_sentence = m.get('InSentence')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')
        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')
        if m.get('MaxEmotionChangeValue') is not None:
            self.max_emotion_change_value = m.get('MaxEmotionChangeValue')
        if m.get('MinWordSize') is not None:
            self.min_word_size = m.get('MinWordSize')
        if m.get('NotRegex') is not None:
            self.not_regex = m.get('NotRegex')
        if m.get('OperKeyWords') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords()
            self.oper_key_words = temp_model.from_map(m['OperKeyWords'])
        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')
        if m.get('Pvalues') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues()
            self.pvalues = temp_model.from_map(m['Pvalues'])
        if m.get('References') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences()
            self.references = temp_model.from_map(m['References'])
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Similarity_threshold') is not None:
            self.similarity_threshold = m.get('Similarity_threshold')
        if m.get('SimilarlySentences') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences()
            self.similarly_sentences = temp_model.from_map(m['SimilarlySentences'])
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VelocityInMint') is not None:
            self.velocity_in_mint = m.get('VelocityInMint')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo(TeaModel):
    def __init__(self, oid=None, oper_name=None, param=None, type=None):
        self.oid = oid  # type: str
        self.oper_name = oper_name  # type: str
        self.param = param  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam
        self.type = type  # type: str

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oid is not None:
            result['Oid'] = self.oid
        if self.oper_name is not None:
            result['OperName'] = self.oper_name
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Oid') is not None:
            self.oid = m.get('Oid')
        if m.get('OperName') is not None:
            self.oper_name = m.get('OperName')
        if m.get('Param') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators(TeaModel):
    def __init__(self, operator_basic_info=None):
        self.operator_basic_info = operator_basic_info  # type: list[GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo]

    def validate(self):
        if self.operator_basic_info:
            for k in self.operator_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperatorBasicInfo'] = []
        if self.operator_basic_info is not None:
            for k in self.operator_basic_info:
                result['OperatorBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.operator_basic_info = []
        if m.get('OperatorBasicInfo') is not None:
            for k in m.get('OperatorBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo()
                self.operator_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfo(TeaModel):
    def __init__(self, check_range=None, condition_info_cid=None, oper_lambda=None, operators=None):
        self.check_range = check_range  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange
        self.condition_info_cid = condition_info_cid  # type: str
        self.oper_lambda = oper_lambda  # type: str
        self.operators = operators  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            self.operators.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditionsConditionBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_range is not None:
            result['CheckRange'] = self.check_range.to_map()
        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid
        if self.oper_lambda is not None:
            result['OperLambda'] = self.oper_lambda
        if self.operators is not None:
            result['Operators'] = self.operators.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckRange') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m['CheckRange'])
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')
        if m.get('OperLambda') is not None:
            self.oper_lambda = m.get('OperLambda')
        if m.get('Operators') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators()
            self.operators = temp_model.from_map(m['Operators'])
        return self


class GetRuleDetailResponseBodyDataConditions(TeaModel):
    def __init__(self, condition_basic_info=None):
        self.condition_basic_info = condition_basic_info  # type: list[GetRuleDetailResponseBodyDataConditionsConditionBasicInfo]

    def validate(self):
        if self.condition_basic_info:
            for k in self.condition_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionBasicInfo'] = []
        if self.condition_basic_info is not None:
            for k in self.condition_basic_info:
                result['ConditionBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.condition_basic_info = []
        if m.get('ConditionBasicInfo') is not None:
            for k in m.get('ConditionBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo(TeaModel):
    def __init__(self, bid=None, business_name=None, service_type=None):
        self.bid = bid  # type: int
        self.business_name = business_name  # type: str
        self.service_type = service_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories(TeaModel):
    def __init__(self, business_category_basic_info=None):
        self.business_category_basic_info = business_category_basic_info  # type: list[GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo]

    def validate(self):
        if self.business_category_basic_info:
            for k in self.business_category_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k in m.get('BusinessCategoryBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers(TeaModel):
    def __init__(self, trigger=None):
        self.trigger = trigger  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfo(TeaModel):
    def __init__(self, business_categories=None, rid=None, rule_lambda=None, triggers=None):
        self.business_categories = business_categories  # type: GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories
        self.rid = rid  # type: str
        self.rule_lambda = rule_lambda  # type: str
        self.triggers = triggers  # type: GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers

    def validate(self):
        if self.business_categories:
            self.business_categories.validate()
        if self.triggers:
            self.triggers.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataRulesRuleBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_categories is not None:
            result['BusinessCategories'] = self.business_categories.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda
        if self.triggers is not None:
            result['Triggers'] = self.triggers.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCategories') is not None:
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories()
            self.business_categories = temp_model.from_map(m['BusinessCategories'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('Triggers') is not None:
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers()
            self.triggers = temp_model.from_map(m['Triggers'])
        return self


class GetRuleDetailResponseBodyDataRules(TeaModel):
    def __init__(self, rule_basic_info=None):
        self.rule_basic_info = rule_basic_info  # type: list[GetRuleDetailResponseBodyDataRulesRuleBasicInfo]

    def validate(self):
        if self.rule_basic_info:
            for k in self.rule_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k in self.rule_basic_info:
                result['RuleBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k in m.get('RuleBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyData(TeaModel):
    def __init__(self, conditions=None, count=None, page_number=None, page_size=None, rules=None):
        self.conditions = conditions  # type: GetRuleDetailResponseBodyDataConditions
        self.count = count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.rules = rules  # type: GetRuleDetailResponseBodyDataRules

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rules') is not None:
            temp_model = GetRuleDetailResponseBodyDataRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class GetRuleDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRuleDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBody, self).to_map()
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
            temp_model = GetRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRuleDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponse, self).to_map()
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
            temp_model = GetRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScoreInfoRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScoreInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam(TeaModel):
    def __init__(self, score_num=None, score_sub_id=None, score_sub_name=None, score_type=None):
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: int
        self.score_sub_name = score_sub_name  # type: str
        self.score_type = score_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        return self


class GetScoreInfoResponseBodyDataScorePoScoreInfos(TeaModel):
    def __init__(self, score_param=None):
        self.score_param = score_param  # type: list[GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam]

    def validate(self):
        if self.score_param:
            for k in self.score_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScoreInfoResponseBodyDataScorePoScoreInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScoreParam'] = []
        if self.score_param is not None:
            for k in self.score_param:
                result['ScoreParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.score_param = []
        if m.get('ScoreParam') is not None:
            for k in m.get('ScoreParam'):
                temp_model = GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam()
                self.score_param.append(temp_model.from_map(k))
        return self


class GetScoreInfoResponseBodyDataScorePo(TeaModel):
    def __init__(self, score_id=None, score_infos=None, score_name=None):
        self.score_id = score_id  # type: int
        self.score_infos = score_infos  # type: GetScoreInfoResponseBodyDataScorePoScoreInfos
        self.score_name = score_name  # type: str

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        _map = super(GetScoreInfoResponseBodyDataScorePo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreInfos') is not None:
            temp_model = GetScoreInfoResponseBodyDataScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m['ScoreInfos'])
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        return self


class GetScoreInfoResponseBodyData(TeaModel):
    def __init__(self, score_po=None):
        self.score_po = score_po  # type: list[GetScoreInfoResponseBodyDataScorePo]

    def validate(self):
        if self.score_po:
            for k in self.score_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScoreInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScorePo'] = []
        if self.score_po is not None:
            for k in self.score_po:
                result['ScorePo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.score_po = []
        if m.get('ScorePo') is not None:
            for k in m.get('ScorePo'):
                temp_model = GetScoreInfoResponseBodyDataScorePo()
                self.score_po.append(temp_model.from_map(k))
        return self


class GetScoreInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetScoreInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScoreInfoResponseBody, self).to_map()
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
            temp_model = GetScoreInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScoreInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetScoreInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScoreInfoResponse, self).to_map()
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
            temp_model = GetScoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetSkillGroupConfigResponseBodyDataAllRuleList(TeaModel):
    def __init__(self, rule_name_info=None):
        self.rule_name_info = rule_name_info  # type: list[GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo]

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBodyDataAllRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetSkillGroupConfigResponseBodyDataRuleList(TeaModel):
    def __init__(self, rule_name_info=None):
        self.rule_name_info = rule_name_info  # type: list[GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo]

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBodyDataRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class GetSkillGroupConfigResponseBodyData(TeaModel):
    def __init__(self, all_content_quality_check=None, all_rids=None, all_rule_list=None, create_time=None, id=None,
                 instance_id=None, model_id=None, model_name=None, name=None, quality_check_type=None, rid=None, rule_list=None,
                 skill_group_from=None, skill_group_id=None, skill_group_name=None, status=None, type=None, update_time=None,
                 vocab_id=None, vocab_name=None):
        self.all_content_quality_check = all_content_quality_check  # type: int
        self.all_rids = all_rids  # type: str
        self.all_rule_list = all_rule_list  # type: GetSkillGroupConfigResponseBodyDataAllRuleList
        self.create_time = create_time  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.model_id = model_id  # type: long
        self.model_name = model_name  # type: str
        self.name = name  # type: str
        self.quality_check_type = quality_check_type  # type: int
        self.rid = rid  # type: str
        self.rule_list = rule_list  # type: GetSkillGroupConfigResponseBodyDataRuleList
        self.skill_group_from = skill_group_from  # type: int
        self.skill_group_id = skill_group_id  # type: str
        self.skill_group_name = skill_group_name  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.update_time = update_time  # type: str
        self.vocab_id = vocab_id  # type: long
        self.vocab_name = vocab_name  # type: str

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('AllRuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class GetSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetSkillGroupConfigResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupConfigResponseBody, self).to_map()
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
            temp_model = GetSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupConfigResponse, self).to_map()
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
            temp_model = GetSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSyncResultRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetSyncResultResponseBodyDataAgent(TeaModel):
    def __init__(self, id=None, name=None, skill_group=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.skill_group = skill_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataAgent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        return self


class GetSyncResultResponseBodyDataAsrResult(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, role=None, silence_duration=None, speech_rate=None,
                 words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = role  # type: str
        self.silence_duration = silence_duration  # type: int
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataAsrResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetSyncResultResponseBodyDataHitResultHitsKeyWords(TeaModel):
    def __init__(self, cid=None, from_=None, to=None, val=None):
        self.cid = cid  # type: str
        self.from_ = from_  # type: int
        self.to = to  # type: int
        self.val = val  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataHitResultHitsKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class GetSyncResultResponseBodyDataHitResultHitsPhrase(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, role=None, silence_duration=None, speech_rate=None,
                 words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: int
        self.role = role  # type: str
        self.silence_duration = silence_duration  # type: int
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataHitResultHitsPhrase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetSyncResultResponseBodyDataHitResultHits(TeaModel):
    def __init__(self, cid=None, key_words=None, phrase=None):
        self.cid = cid  # type: list[str]
        self.key_words = key_words  # type: list[GetSyncResultResponseBodyDataHitResultHitsKeyWords]
        self.phrase = phrase  # type: GetSyncResultResponseBodyDataHitResultHitsPhrase

    def validate(self):
        if self.key_words:
            for k in self.key_words:
                if k:
                    k.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataHitResultHits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        result['KeyWords'] = []
        if self.key_words is not None:
            for k in self.key_words:
                result['KeyWords'].append(k.to_map() if k else None)
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        self.key_words = []
        if m.get('KeyWords') is not None:
            for k in m.get('KeyWords'):
                temp_model = GetSyncResultResponseBodyDataHitResultHitsKeyWords()
                self.key_words.append(temp_model.from_map(k))
        if m.get('Phrase') is not None:
            temp_model = GetSyncResultResponseBodyDataHitResultHitsPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetSyncResultResponseBodyDataHitResult(TeaModel):
    def __init__(self, hits=None, name=None, review_result=None, rid=None, type=None):
        self.hits = hits  # type: list[GetSyncResultResponseBodyDataHitResultHits]
        self.name = name  # type: str
        self.review_result = review_result  # type: int
        self.rid = rid  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataHitResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hits'] = []
        if self.hits is not None:
            for k in self.hits:
                result['Hits'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hits = []
        if m.get('Hits') is not None:
            for k in m.get('Hits'):
                temp_model = GetSyncResultResponseBodyDataHitResultHits()
                self.hits.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSyncResultResponseBodyDataRecording(TeaModel):
    def __init__(self, business=None, call_id=None, call_time=None, call_type=None, callee=None, caller=None,
                 data_set_name=None, duration=None, duration_audio=None, id=None, name=None, primary_id=None, remark_1=None,
                 remark_2=None, remark_3=None, url=None):
        self.business = business  # type: str
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.call_type = call_type  # type: int
        self.callee = callee  # type: str
        self.caller = caller  # type: str
        self.data_set_name = data_set_name  # type: str
        self.duration = duration  # type: long
        self.duration_audio = duration_audio  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.primary_id = primary_id  # type: str
        self.remark_1 = remark_1  # type: str
        self.remark_2 = remark_2  # type: str
        self.remark_3 = remark_3  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyncResultResponseBodyDataRecording, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_audio is not None:
            result['DurationAudio'] = self.duration_audio
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationAudio') is not None:
            self.duration_audio = m.get('DurationAudio')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetSyncResultResponseBodyData(TeaModel):
    def __init__(self, agent=None, asr_result=None, comments=None, create_time=None, error_message=None,
                 hit_result=None, recording=None, resolver=None, review_result=None, review_status=None, reviewer=None,
                 score=None, status=None, task_id=None, task_name=None):
        self.agent = agent  # type: GetSyncResultResponseBodyDataAgent
        self.asr_result = asr_result  # type: list[GetSyncResultResponseBodyDataAsrResult]
        self.comments = comments  # type: str
        self.create_time = create_time  # type: str
        self.error_message = error_message  # type: str
        self.hit_result = hit_result  # type: list[GetSyncResultResponseBodyDataHitResult]
        self.recording = recording  # type: GetSyncResultResponseBodyDataRecording
        self.resolver = resolver  # type: str
        self.review_result = review_result  # type: int
        self.review_status = review_status  # type: int
        self.reviewer = reviewer  # type: str
        self.score = score  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            for k in self.asr_result:
                if k:
                    k.validate()
        if self.hit_result:
            for k in self.hit_result:
                if k:
                    k.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        _map = super(GetSyncResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['AsrResult'].append(k.to_map() if k else None)
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['HitResult'] = []
        if self.hit_result is not None:
            for k in self.hit_result:
                result['HitResult'].append(k.to_map() if k else None)
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.score is not None:
            result['Score'] = self.score
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = GetSyncResultResponseBodyDataAgent()
            self.agent = temp_model.from_map(m['Agent'])
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k in m.get('AsrResult'):
                temp_model = GetSyncResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k in m.get('HitResult'):
                temp_model = GetSyncResultResponseBodyDataHitResult()
                self.hit_result.append(temp_model.from_map(k))
        if m.get('Recording') is not None:
            temp_model = GetSyncResultResponseBodyDataRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetSyncResultResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, result_count_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: list[GetSyncResultResponseBodyData]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.result_count_id = result_count_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSyncResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSyncResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSyncResultResponse, self).to_map()
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
            temp_model = GetSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThesaurusBySynonymForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList(TeaModel):
    def __init__(self, synonym_list=None):
        self.synonym_list = synonym_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synonym_list is not None:
            result['SynonymList'] = self.synonym_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SynonymList') is not None:
            self.synonym_list = m.get('SynonymList')
        return self


class GetThesaurusBySynonymForApiResponseBodyDataThesaurusPo(TeaModel):
    def __init__(self, business=None, id=None, synonym_list=None):
        self.business = business  # type: str
        self.id = id  # type: long
        self.synonym_list = synonym_list  # type: GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList

    def validate(self):
        if self.synonym_list:
            self.synonym_list.validate()

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiResponseBodyDataThesaurusPo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.id is not None:
            result['Id'] = self.id
        if self.synonym_list is not None:
            result['SynonymList'] = self.synonym_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SynonymList') is not None:
            temp_model = GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList()
            self.synonym_list = temp_model.from_map(m['SynonymList'])
        return self


class GetThesaurusBySynonymForApiResponseBodyData(TeaModel):
    def __init__(self, thesaurus_po=None):
        self.thesaurus_po = thesaurus_po  # type: list[GetThesaurusBySynonymForApiResponseBodyDataThesaurusPo]

    def validate(self):
        if self.thesaurus_po:
            for k in self.thesaurus_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThesaurusPo'] = []
        if self.thesaurus_po is not None:
            for k in self.thesaurus_po:
                result['ThesaurusPo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.thesaurus_po = []
        if m.get('ThesaurusPo') is not None:
            for k in m.get('ThesaurusPo'):
                temp_model = GetThesaurusBySynonymForApiResponseBodyDataThesaurusPo()
                self.thesaurus_po.append(temp_model.from_map(k))
        return self


class GetThesaurusBySynonymForApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetThesaurusBySynonymForApiResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiResponseBody, self).to_map()
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
            temp_model = GetThesaurusBySynonymForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetThesaurusBySynonymForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetThesaurusBySynonymForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetThesaurusBySynonymForApiResponse, self).to_map()
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
            temp_model = GetThesaurusBySynonymForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleComplaintRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleComplaintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class HandleComplaintResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleComplaintResponseBody, self).to_map()
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


class HandleComplaintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HandleComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HandleComplaintResponse, self).to_map()
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
            temp_model = HandleComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InsertScoreForApiResponseBodyData(TeaModel):
    def __init__(self, score_id=None, score_name=None):
        self.score_id = score_id  # type: long
        self.score_name = score_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertScoreForApiResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        return self


class InsertScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertScoreForApiResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertScoreForApiResponseBody, self).to_map()
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
            temp_model = InsertScoreForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertScoreForApiResponse, self).to_map()
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
            temp_model = InsertScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertSubScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertSubScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InsertSubScoreForApiResponseBodyData(TeaModel):
    def __init__(self, score_sub_id=None, score_sub_name=None):
        self.score_sub_id = score_sub_id  # type: long
        self.score_sub_name = score_sub_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertSubScoreForApiResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        return self


class InsertSubScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertSubScoreForApiResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertSubScoreForApiResponseBody, self).to_map()
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
            temp_model = InsertSubScoreForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertSubScoreForApiResponse, self).to_map()
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
            temp_model = InsertSubScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvalidRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvalidRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InvalidRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvalidRuleResponseBody, self).to_map()
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


class InvalidRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InvalidRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvalidRuleResponse, self).to_map()
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
            temp_model = InvalidRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsrVocabRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsrVocabRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListAsrVocabResponseBodyDataAsrVocab(TeaModel):
    def __init__(self, create_time=None, id=None, name=None, update_time=None, vocabulary_id=None):
        self.create_time = create_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.update_time = update_time  # type: str
        self.vocabulary_id = vocabulary_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsrVocabResponseBodyDataAsrVocab, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')
        return self


class ListAsrVocabResponseBodyData(TeaModel):
    def __init__(self, asr_vocab=None):
        self.asr_vocab = asr_vocab  # type: list[ListAsrVocabResponseBodyDataAsrVocab]

    def validate(self):
        if self.asr_vocab:
            for k in self.asr_vocab:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAsrVocabResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsrVocab'] = []
        if self.asr_vocab is not None:
            for k in self.asr_vocab:
                result['AsrVocab'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.asr_vocab = []
        if m.get('AsrVocab') is not None:
            for k in m.get('AsrVocab'):
                temp_model = ListAsrVocabResponseBodyDataAsrVocab()
                self.asr_vocab.append(temp_model.from_map(k))
        return self


class ListAsrVocabResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListAsrVocabResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAsrVocabResponseBody, self).to_map()
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
            temp_model = ListAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAsrVocabResponse, self).to_map()
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
            temp_model = ListAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotWordsTasksRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotWordsTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam(TeaModel):
    def __init__(self, data_set_ids=None, dialogue_id=None, end_index=None, end_time=None, role=None,
                 source_type=None, start_index=None, start_time=None):
        self.data_set_ids = data_set_ids  # type: str
        self.dialogue_id = dialogue_id  # type: long
        self.end_index = end_index  # type: int
        self.end_time = end_time  # type: str
        self.role = role  # type: int
        self.source_type = source_type  # type: int
        self.start_index = start_index  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_ids is not None:
            result['DataSetIds'] = self.data_set_ids
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.role is not None:
            result['Role'] = self.role
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSetIds') is not None:
            self.data_set_ids = m.get('DataSetIds')
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam(TeaModel):
    def __init__(self, excludes=None, extra_config_id=None, includes=None):
        self.excludes = excludes  # type: str
        self.extra_config_id = extra_config_id  # type: long
        self.includes = includes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes
        if self.extra_config_id is not None:
            result['ExtraConfigId'] = self.extra_config_id
        if self.includes is not None:
            result['Includes'] = self.includes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')
        if m.get('ExtraConfigId') is not None:
            self.extra_config_id = m.get('ExtraConfigId')
        if m.get('Includes') is not None:
            self.includes = m.get('Includes')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPo(TeaModel):
    def __init__(self, dialogue_param=None, end_time=None, instance_status=None, last_execution_time=None,
                 message=None, name=None, start_time=None, status=None, task_config_id=None, time_interval=None,
                 time_unit=None, type=None, words_param=None):
        self.dialogue_param = dialogue_param  # type: ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam
        self.end_time = end_time  # type: str
        self.instance_status = instance_status  # type: int
        self.last_execution_time = last_execution_time  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.task_config_id = task_config_id  # type: long
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: int
        self.type = type  # type: int
        self.words_param = words_param  # type: ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam

    def validate(self):
        if self.dialogue_param:
            self.dialogue_param.validate()
        if self.words_param:
            self.words_param.validate()

    def to_map(self):
        _map = super(ListHotWordsTasksResponseBodyDataHotWordsTaskPo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue_param is not None:
            result['DialogueParam'] = self.dialogue_param.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.last_execution_time is not None:
            result['LastExecutionTime'] = self.last_execution_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.type is not None:
            result['Type'] = self.type
        if self.words_param is not None:
            result['WordsParam'] = self.words_param.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DialogueParam') is not None:
            temp_model = ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam()
            self.dialogue_param = temp_model.from_map(m['DialogueParam'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LastExecutionTime') is not None:
            self.last_execution_time = m.get('LastExecutionTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WordsParam') is not None:
            temp_model = ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam()
            self.words_param = temp_model.from_map(m['WordsParam'])
        return self


class ListHotWordsTasksResponseBodyData(TeaModel):
    def __init__(self, hot_words_task_po=None):
        self.hot_words_task_po = hot_words_task_po  # type: list[ListHotWordsTasksResponseBodyDataHotWordsTaskPo]

    def validate(self):
        if self.hot_words_task_po:
            for k in self.hot_words_task_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotWordsTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotWordsTaskPo'] = []
        if self.hot_words_task_po is not None:
            for k in self.hot_words_task_po:
                result['HotWordsTaskPo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hot_words_task_po = []
        if m.get('HotWordsTaskPo') is not None:
            for k in m.get('HotWordsTaskPo'):
                temp_model = ListHotWordsTasksResponseBodyDataHotWordsTaskPo()
                self.hot_words_task_po.append(temp_model.from_map(k))
        return self


class ListHotWordsTasksResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: ListHotWordsTasksResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListHotWordsTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListHotWordsTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotWordsTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotWordsTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotWordsTasksResponse, self).to_map()
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
            temp_model = ListHotWordsTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrecisionTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrecisionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision(TeaModel):
    def __init__(self, create_time=None, model_id=None, model_name=None, precision=None, status=None, task_id=None):
        self.create_time = create_time  # type: str
        self.model_id = model_id  # type: long
        self.model_name = model_name  # type: str
        self.precision = precision  # type: float
        self.status = status  # type: int
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions(TeaModel):
    def __init__(self, precision=None):
        self.precision = precision  # type: list[ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision]

    def validate(self):
        if self.precision:
            for k in self.precision:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Precision'] = []
        if self.precision is not None:
            for k in self.precision:
                result['Precision'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.precision = []
        if m.get('Precision') is not None:
            for k in m.get('Precision'):
                temp_model = ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision()
                self.precision.append(temp_model.from_map(k))
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTask(TeaModel):
    def __init__(self, create_time=None, data_set_id=None, data_set_name=None, duration=None, incorrect_words=None,
                 name=None, precisions=None, source=None, status=None, task_id=None, total_count=None, update_time=None,
                 verified_count=None):
        self.create_time = create_time  # type: str
        self.data_set_id = data_set_id  # type: long
        self.data_set_name = data_set_name  # type: str
        self.duration = duration  # type: int
        self.incorrect_words = incorrect_words  # type: int
        self.name = name  # type: str
        self.precisions = precisions  # type: ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions
        self.source = source  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.total_count = total_count  # type: int
        self.update_time = update_time  # type: str
        self.verified_count = verified_count  # type: int

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        _map = super(ListPrecisionTaskResponseBodyDataPrecisionTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.name is not None:
            result['Name'] = self.name
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Precisions') is not None:
            temp_model = ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class ListPrecisionTaskResponseBodyData(TeaModel):
    def __init__(self, precision_task=None):
        self.precision_task = precision_task  # type: list[ListPrecisionTaskResponseBodyDataPrecisionTask]

    def validate(self):
        if self.precision_task:
            for k in self.precision_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrecisionTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrecisionTask'] = []
        if self.precision_task is not None:
            for k in self.precision_task:
                result['PrecisionTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.precision_task = []
        if m.get('PrecisionTask') is not None:
            for k in m.get('PrecisionTask'):
                temp_model = ListPrecisionTaskResponseBodyDataPrecisionTask()
                self.precision_task.append(temp_model.from_map(k))
        return self


class ListPrecisionTaskResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: ListPrecisionTaskResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPrecisionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrecisionTaskResponse, self).to_map()
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
            temp_model = ListPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListRolesResponseBodyDataRole(TeaModel):
    def __init__(self, create_time=None, display_name=None, id=None, level=None, name=None, update_time=None):
        self.create_time = create_time  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: long
        self.level = level  # type: int
        self.name = name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(self, role=None):
        self.role = role  # type: list[ListRolesResponseBodyDataRole]

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesResponseBodyDataRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListRolesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListRolesResponseBody, self).to_map()
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
            temp_model = ListRolesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRolesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRolesResponse, self).to_map()
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(self, business_category_name_list=None, comments=None, create_time=None, name=None, rid=None,
                 rule_type=None, type=None, type_name=None):
        self.business_category_name_list = business_category_name_list  # type: list[str]
        self.comments = comments  # type: str
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.rid = rid  # type: long
        self.rule_type = rule_type  # type: int
        self.type = type  # type: int
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: list[ListRulesResponseBodyData]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRulesResponse, self).to_map()
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSkillGroupConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList(TeaModel):
    def __init__(self, rule_name_info=None):
        self.rule_name_info = rule_name_info  # type: list[ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo]

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList(TeaModel):
    def __init__(self, rule_name_info=None):
        self.rule_name_info = rule_name_info  # type: list[ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo]

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen(TeaModel):
    def __init__(self, data_type=None, name=None, symbol=None, value=None):
        self.data_type = data_type  # type: int
        self.name = name  # type: str
        self.symbol = symbol  # type: int
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.name is not None:
            result['Name'] = self.name
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens(TeaModel):
    def __init__(self, skill_group_screen=None):
        self.skill_group_screen = skill_group_screen  # type: list[ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen]

    def validate(self):
        if self.skill_group_screen:
            for k in self.skill_group_screen:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroupScreen'] = []
        if self.skill_group_screen is not None:
            for k in self.skill_group_screen:
                result['SkillGroupScreen'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.skill_group_screen = []
        if m.get('SkillGroupScreen') is not None:
            for k in m.get('SkillGroupScreen'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen()
                self.skill_group_screen.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfig(TeaModel):
    def __init__(self, all_content_quality_check=None, all_rids=None, all_rule_list=None, create_time=None, id=None,
                 instance_id=None, model_id=None, model_name=None, name=None, quality_check_type=None, rid=None, rule_list=None,
                 screen_switch=None, skill_group_from=None, skill_group_id=None, skill_group_name=None, skill_group_screens=None,
                 status=None, type=None, update_time=None, vocab_id=None, vocab_name=None):
        self.all_content_quality_check = all_content_quality_check  # type: int
        self.all_rids = all_rids  # type: str
        self.all_rule_list = all_rule_list  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList
        self.create_time = create_time  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.model_id = model_id  # type: long
        self.model_name = model_name  # type: str
        self.name = name  # type: str
        self.quality_check_type = quality_check_type  # type: int
        self.rid = rid  # type: str
        self.rule_list = rule_list  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList
        self.screen_switch = screen_switch  # type: bool
        self.skill_group_from = skill_group_from  # type: int
        self.skill_group_id = skill_group_id  # type: str
        self.skill_group_name = skill_group_name  # type: str
        self.skill_group_screens = skill_group_screens  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens
        self.status = status  # type: int
        self.type = type  # type: int
        self.update_time = update_time  # type: str
        self.vocab_id = vocab_id  # type: long
        self.vocab_name = vocab_name  # type: str

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()
        if self.skill_group_screens:
            self.skill_group_screens.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyDataSkillGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.screen_switch is not None:
            result['ScreenSwitch'] = self.screen_switch
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.skill_group_screens is not None:
            result['SkillGroupScreens'] = self.skill_group_screens.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('AllRuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('ScreenSwitch') is not None:
            self.screen_switch = m.get('ScreenSwitch')
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('SkillGroupScreens') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens()
            self.skill_group_screens = temp_model.from_map(m['SkillGroupScreens'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class ListSkillGroupConfigResponseBodyData(TeaModel):
    def __init__(self, skill_group_config=None):
        self.skill_group_config = skill_group_config  # type: list[ListSkillGroupConfigResponseBodyDataSkillGroupConfig]

    def validate(self):
        if self.skill_group_config:
            for k in self.skill_group_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroupConfig'] = []
        if self.skill_group_config is not None:
            for k in self.skill_group_config:
                result['SkillGroupConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.skill_group_config = []
        if m.get('SkillGroupConfig') is not None:
            for k in m.get('SkillGroupConfig'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfig()
                self.skill_group_config.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListSkillGroupConfigResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponseBody, self).to_map()
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
            temp_model = ListSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSkillGroupConfigResponse, self).to_map()
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
            temp_model = ListSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskAssignRulesRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent(TeaModel):
    def __init__(self, agent_id=None, agent_name=None):
        self.agent_id = agent_id  # type: str
        self.agent_name = agent_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents(TeaModel):
    def __init__(self, agent=None):
        self.agent = agent  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent]

    def validate(self):
        if self.agent:
            for k in self.agent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agent'] = []
        if self.agent is not None:
            for k in self.agent:
                result['Agent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.agent = []
        if m.get('Agent') is not None:
            for k in m.get('Agent'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent()
                self.agent.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer(TeaModel):
    def __init__(self, reviewer_id=None, reviewer_name=None):
        self.reviewer_id = reviewer_id  # type: str
        self.reviewer_name = reviewer_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reviewer_id is not None:
            result['ReviewerId'] = self.reviewer_id
        if self.reviewer_name is not None:
            result['ReviewerName'] = self.reviewer_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewerId') is not None:
            self.reviewer_id = m.get('ReviewerId')
        if m.get('ReviewerName') is not None:
            self.reviewer_name = m.get('ReviewerName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers(TeaModel):
    def __init__(self, reviewer=None):
        self.reviewer = reviewer  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer]

    def validate(self):
        if self.reviewer:
            for k in self.reviewer:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Reviewer'] = []
        if self.reviewer is not None:
            for k in self.reviewer:
                result['Reviewer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.reviewer = []
        if m.get('Reviewer') is not None:
            for k in m.get('Reviewer'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer()
                self.reviewer.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo(TeaModel):
    def __init__(self, name=None, rid=None):
        self.name = name  # type: str
        self.rid = rid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules(TeaModel):
    def __init__(self, rule_basic_info=None):
        self.rule_basic_info = rule_basic_info  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo]

    def validate(self):
        if self.rule_basic_info:
            for k in self.rule_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k in self.rule_basic_info:
                result['RuleBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k in m.get('RuleBasicInfo'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent(TeaModel):
    def __init__(self, agent_id=None, agent_name=None):
        self.agent_id = agent_id  # type: str
        self.agent_name = agent_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents(TeaModel):
    def __init__(self, sampling_mode_agent=None):
        self.sampling_mode_agent = sampling_mode_agent  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent]

    def validate(self):
        if self.sampling_mode_agent:
            for k in self.sampling_mode_agent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SamplingModeAgent'] = []
        if self.sampling_mode_agent is not None:
            for k in self.sampling_mode_agent:
                result['SamplingModeAgent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sampling_mode_agent = []
        if m.get('SamplingModeAgent') is not None:
            for k in m.get('SamplingModeAgent'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent()
                self.sampling_mode_agent.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode(TeaModel):
    def __init__(self, any_number_of_draws=None, designated=None, dimension=None, limit=None, number_of_draws=None,
                 proportion=None, random_inspection_number=None, sampling_mode_agents=None):
        self.any_number_of_draws = any_number_of_draws  # type: int
        self.designated = designated  # type: bool
        self.dimension = dimension  # type: int
        self.limit = limit  # type: int
        self.number_of_draws = number_of_draws  # type: int
        self.proportion = proportion  # type: float
        self.random_inspection_number = random_inspection_number  # type: int
        self.sampling_mode_agents = sampling_mode_agents  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents

    def validate(self):
        if self.sampling_mode_agents:
            self.sampling_mode_agents.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.any_number_of_draws is not None:
            result['AnyNumberOfDraws'] = self.any_number_of_draws
        if self.designated is not None:
            result['Designated'] = self.designated
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.number_of_draws is not None:
            result['NumberOfDraws'] = self.number_of_draws
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.random_inspection_number is not None:
            result['RandomInspectionNumber'] = self.random_inspection_number
        if self.sampling_mode_agents is not None:
            result['SamplingModeAgents'] = self.sampling_mode_agents.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnyNumberOfDraws') is not None:
            self.any_number_of_draws = m.get('AnyNumberOfDraws')
        if m.get('Designated') is not None:
            self.designated = m.get('Designated')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NumberOfDraws') is not None:
            self.number_of_draws = m.get('NumberOfDraws')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('RandomInspectionNumber') is not None:
            self.random_inspection_number = m.get('RandomInspectionNumber')
        if m.get('SamplingModeAgents') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents()
            self.sampling_mode_agents = temp_model.from_map(m['SamplingModeAgents'])
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup(TeaModel):
    def __init__(self, skill_id=None, skill_name=None):
        self.skill_id = skill_id  # type: str
        self.skill_name = skill_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skill_id is not None:
            result['SkillId'] = self.skill_id
        if self.skill_name is not None:
            result['SkillName'] = self.skill_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')
        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups(TeaModel):
    def __init__(self, skill_group=None):
        self.skill_group = skill_group  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup]

    def validate(self):
        if self.skill_group:
            for k in self.skill_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroup'] = []
        if self.skill_group is not None:
            for k in self.skill_group:
                result['SkillGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.skill_group = []
        if m.get('SkillGroup') is not None:
            for k in m.get('SkillGroup'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup()
                self.skill_group.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo(TeaModel):
    def __init__(self, agents=None, agents_str=None, assignment_type=None, call_time_end=None, call_time_start=None,
                 call_type=None, create_time=None, duration_max=None, duration_min=None, enabled=None, priority=None,
                 reviewers=None, rule_id=None, rule_name=None, rules=None, sampling_mode=None, skill_groups=None,
                 skill_groups_str=None, update_time=None):
        self.agents = agents  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents
        self.agents_str = agents_str  # type: str
        self.assignment_type = assignment_type  # type: int
        self.call_time_end = call_time_end  # type: long
        self.call_time_start = call_time_start  # type: long
        self.call_type = call_type  # type: int
        self.create_time = create_time  # type: str
        self.duration_max = duration_max  # type: int
        self.duration_min = duration_min  # type: int
        self.enabled = enabled  # type: int
        self.priority = priority  # type: int
        self.reviewers = reviewers  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.rules = rules  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules
        self.sampling_mode = sampling_mode  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode
        self.skill_groups = skill_groups  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups
        self.skill_groups_str = skill_groups_str  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.agents:
            self.agents.validate()
        if self.reviewers:
            self.reviewers.validate()
        if self.rules:
            self.rules.validate()
        if self.sampling_mode:
            self.sampling_mode.validate()
        if self.skill_groups:
            self.skill_groups.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agents is not None:
            result['Agents'] = self.agents.to_map()
        if self.agents_str is not None:
            result['AgentsStr'] = self.agents_str
        if self.assignment_type is not None:
            result['AssignmentType'] = self.assignment_type
        if self.call_time_end is not None:
            result['CallTimeEnd'] = self.call_time_end
        if self.call_time_start is not None:
            result['CallTimeStart'] = self.call_time_start
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration_max is not None:
            result['DurationMax'] = self.duration_max
        if self.duration_min is not None:
            result['DurationMin'] = self.duration_min
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers.to_map()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.sampling_mode is not None:
            result['SamplingMode'] = self.sampling_mode.to_map()
        if self.skill_groups is not None:
            result['SkillGroups'] = self.skill_groups.to_map()
        if self.skill_groups_str is not None:
            result['SkillGroupsStr'] = self.skill_groups_str
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Agents') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents()
            self.agents = temp_model.from_map(m['Agents'])
        if m.get('AgentsStr') is not None:
            self.agents_str = m.get('AgentsStr')
        if m.get('AssignmentType') is not None:
            self.assignment_type = m.get('AssignmentType')
        if m.get('CallTimeEnd') is not None:
            self.call_time_end = m.get('CallTimeEnd')
        if m.get('CallTimeStart') is not None:
            self.call_time_start = m.get('CallTimeStart')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DurationMax') is not None:
            self.duration_max = m.get('DurationMax')
        if m.get('DurationMin') is not None:
            self.duration_min = m.get('DurationMin')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Reviewers') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers()
            self.reviewers = temp_model.from_map(m['Reviewers'])
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rules') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SamplingMode') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode()
            self.sampling_mode = temp_model.from_map(m['SamplingMode'])
        if m.get('SkillGroups') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups()
            self.skill_groups = temp_model.from_map(m['SkillGroups'])
        if m.get('SkillGroupsStr') is not None:
            self.skill_groups_str = m.get('SkillGroupsStr')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTaskAssignRulesResponseBodyData(TeaModel):
    def __init__(self, task_assign_rule_info=None):
        self.task_assign_rule_info = task_assign_rule_info  # type: list[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo]

    def validate(self):
        if self.task_assign_rule_info:
            for k in self.task_assign_rule_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskAssignRuleInfo'] = []
        if self.task_assign_rule_info is not None:
            for k in self.task_assign_rule_info:
                result['TaskAssignRuleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_assign_rule_info = []
        if m.get('TaskAssignRuleInfo') is not None:
            for k in m.get('TaskAssignRuleInfo'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo()
                self.task_assign_rule_info.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: ListTaskAssignRulesResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListTaskAssignRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTaskAssignRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTaskAssignRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskAssignRulesResponse, self).to_map()
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
            temp_model = ListTaskAssignRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListUsersResponseBodyDataUser(TeaModel):
    def __init__(self, ali_uid=None, create_time=None, description=None, display_name=None, id=None,
                 login_user_type=None, role_name=None, update_time=None, user_name=None):
        self.ali_uid = ali_uid  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: long
        self.login_user_type = login_user_type  # type: int
        self.role_name = role_name  # type: str
        self.update_time = update_time  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyDataUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.login_user_type is not None:
            result['LoginUserType'] = self.login_user_type
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginUserType') is not None:
            self.login_user_type = m.get('LoginUserType')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[ListUsersResponseBodyDataUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyDataUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.data = data  # type: ListUsersResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWarningConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWarningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel(TeaModel):
    def __init__(self, type=None, url=None):
        self.type = type  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoChannels(TeaModel):
    def __init__(self, channel=None):
        self.channel = channel  # type: list[ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel]

    def validate(self):
        if self.channel:
            for k in self.channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfoChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channel'] = []
        if self.channel is not None:
            for k in self.channel:
                result['Channel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.channel = []
        if m.get('Channel') is not None:
            for k in m.get('Channel'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel()
                self.channel.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRidList(TeaModel):
    def __init__(self, rid_list=None):
        self.rid_list = rid_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfoRidList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid_list is not None:
            result['RidList'] = self.rid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RidList') is not None:
            self.rid_list = m.get('RidList')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule(TeaModel):
    def __init__(self, rid=None, rule_name=None):
        self.rid = rid  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRuleList(TeaModel):
    def __init__(self, warning_rule=None):
        self.warning_rule = warning_rule  # type: list[ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule]

    def validate(self):
        if self.warning_rule:
            for k in self.warning_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfoRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WarningRule'] = []
        if self.warning_rule is not None:
            for k in self.warning_rule:
                result['WarningRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.warning_rule = []
        if m.get('WarningRule') is not None:
            for k in m.get('WarningRule'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule()
                self.warning_rule.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfo(TeaModel):
    def __init__(self, channels=None, config_id=None, config_name=None, create_time=None, rid_list=None,
                 rule_list=None, status=None, update_time=None):
        self.channels = channels  # type: ListWarningConfigResponseBodyDataWarningConfigInfoChannels
        self.config_id = config_id  # type: long
        self.config_name = config_name  # type: str
        self.create_time = create_time  # type: str
        self.rid_list = rid_list  # type: ListWarningConfigResponseBodyDataWarningConfigInfoRidList
        self.rule_list = rule_list  # type: ListWarningConfigResponseBodyDataWarningConfigInfoRuleList
        self.status = status  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        if self.channels:
            self.channels.validate()
        if self.rid_list:
            self.rid_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyDataWarningConfigInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rid_list is not None:
            result['RidList'] = self.rid_list.to_map()
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RidList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRidList()
            self.rid_list = temp_model.from_map(m['RidList'])
        if m.get('RuleList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWarningConfigResponseBodyData(TeaModel):
    def __init__(self, warning_config_info=None):
        self.warning_config_info = warning_config_info  # type: list[ListWarningConfigResponseBodyDataWarningConfigInfo]

    def validate(self):
        if self.warning_config_info:
            for k in self.warning_config_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WarningConfigInfo'] = []
        if self.warning_config_info is not None:
            for k in self.warning_config_info:
                result['WarningConfigInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.warning_config_info = []
        if m.get('WarningConfigInfo') is not None:
            for k in m.get('WarningConfigInfo'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfo()
                self.warning_config_info.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListWarningConfigResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponseBody, self).to_map()
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
            temp_model = ListWarningConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWarningConfigResponse, self).to_map()
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
            temp_model = ListWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartAsrTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartAsrTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class RestartAsrTaskResponseBodyDataRestartResult(TeaModel):
    def __init__(self, data=None, message=None, success=None):
        self.data = data  # type: str
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartAsrTaskResponseBodyDataRestartResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartAsrTaskResponseBodyData(TeaModel):
    def __init__(self, restart_result=None):
        self.restart_result = restart_result  # type: list[RestartAsrTaskResponseBodyDataRestartResult]

    def validate(self):
        if self.restart_result:
            for k in self.restart_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RestartAsrTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestartResult'] = []
        if self.restart_result is not None:
            for k in self.restart_result:
                result['RestartResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restart_result = []
        if m.get('RestartResult') is not None:
            for k in m.get('RestartResult'):
                temp_model = RestartAsrTaskResponseBodyDataRestartResult()
                self.restart_result.append(temp_model.from_map(k))
        return self


class RestartAsrTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RestartAsrTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RestartAsrTaskResponseBody, self).to_map()
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
            temp_model = RestartAsrTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartAsrTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartAsrTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartAsrTaskResponse, self).to_map()
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
            temp_model = RestartAsrTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveConfigDataSetRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveConfigDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SaveConfigDataSetResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveConfigDataSetResponseBody, self).to_map()
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


class SaveConfigDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveConfigDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveConfigDataSetResponse, self).to_map()
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
            temp_model = SaveConfigDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitComplaintRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitComplaintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitComplaintResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitComplaintResponseBody, self).to_map()
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


class SubmitComplaintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitComplaintResponse, self).to_map()
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
            temp_model = SubmitComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPrecisionTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPrecisionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitPrecisionTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPrecisionTaskResponseBody, self).to_map()
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


class SubmitPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitPrecisionTaskResponse, self).to_map()
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
            temp_model = SubmitPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitQualityCheckTaskRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitQualityCheckTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitQualityCheckTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitQualityCheckTaskResponseBody, self).to_map()
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


class SubmitQualityCheckTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitQualityCheckTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitQualityCheckTaskResponse, self).to_map()
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
            temp_model = SubmitQualityCheckTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitReviewInfoRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitReviewInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitReviewInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitReviewInfoResponseBody, self).to_map()
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


class SubmitReviewInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitReviewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitReviewInfoResponse, self).to_map()
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
            temp_model = SubmitReviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncQualityCheckRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncQualityCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SyncQualityCheckResponseBodyDataRulesHitHitKeyWords(TeaModel):
    def __init__(self, cid=None, from_=None, pid=None, to=None, val=None):
        self.cid = cid  # type: int
        self.from_ = from_  # type: int
        self.pid = pid  # type: int
        self.to = to  # type: int
        self.val = val  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncQualityCheckResponseBodyDataRulesHitHitKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class SyncQualityCheckResponseBodyDataRulesHitPhrase(TeaModel):
    def __init__(self, begin=None, emotion_value=None, end=None, identity=None, role=None, silence_duration=None,
                 speech_rate=None, words=None):
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.identity = identity  # type: str
        self.role = role  # type: str
        self.silence_duration = silence_duration  # type: int
        self.speech_rate = speech_rate  # type: int
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncQualityCheckResponseBodyDataRulesHitPhrase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class SyncQualityCheckResponseBodyDataRulesHit(TeaModel):
    def __init__(self, hit_key_words=None, phrase=None):
        self.hit_key_words = hit_key_words  # type: list[SyncQualityCheckResponseBodyDataRulesHitHitKeyWords]
        self.phrase = phrase  # type: SyncQualityCheckResponseBodyDataRulesHitPhrase

    def validate(self):
        if self.hit_key_words:
            for k in self.hit_key_words:
                if k:
                    k.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super(SyncQualityCheckResponseBodyDataRulesHit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitKeyWords'] = []
        if self.hit_key_words is not None:
            for k in self.hit_key_words:
                result['HitKeyWords'].append(k.to_map() if k else None)
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit_key_words = []
        if m.get('HitKeyWords') is not None:
            for k in m.get('HitKeyWords'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHitHitKeyWords()
                self.hit_key_words.append(temp_model.from_map(k))
        if m.get('Phrase') is not None:
            temp_model = SyncQualityCheckResponseBodyDataRulesHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class SyncQualityCheckResponseBodyDataRules(TeaModel):
    def __init__(self, hit=None, rid=None, rule_name=None):
        self.hit = hit  # type: list[SyncQualityCheckResponseBodyDataRulesHit]
        self.rid = rid  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SyncQualityCheckResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hit'] = []
        if self.hit is not None:
            for k in self.hit:
                result['Hit'].append(k.to_map() if k else None)
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k in m.get('Hit'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHit()
                self.hit.append(temp_model.from_map(k))
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class SyncQualityCheckResponseBodyData(TeaModel):
    def __init__(self, begin_time=None, rules=None, score=None, task_id=None, tid=None):
        self.begin_time = begin_time  # type: long
        self.rules = rules  # type: list[SyncQualityCheckResponseBodyDataRules]
        self.score = score  # type: int
        self.task_id = task_id  # type: str
        self.tid = tid  # type: str

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SyncQualityCheckResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SyncQualityCheckResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SyncQualityCheckResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SyncQualityCheckResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SyncQualityCheckResponseBody, self).to_map()
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
            temp_model = SyncQualityCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncQualityCheckResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncQualityCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncQualityCheckResponse, self).to_map()
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
            temp_model = SyncQualityCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAsrVocabRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAsrVocabRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateAsrVocabResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAsrVocabResponseBody, self).to_map()
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


class UpdateAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAsrVocabResponse, self).to_map()
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
            temp_model = UpdateAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRuleResponseBody, self).to_map()
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


class UpdateRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRuleResponse, self).to_map()
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
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateScoreForApiResponseBody, self).to_map()
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


class UpdateScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateScoreForApiResponse, self).to_map()
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
            temp_model = UpdateScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSkillGroupConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSkillGroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSkillGroupConfigResponseBody, self).to_map()
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


class UpdateSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSkillGroupConfigResponse, self).to_map()
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
            temp_model = UpdateSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubScoreForApiRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubScoreForApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSubScoreForApiResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubScoreForApiResponseBody, self).to_map()
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


class UpdateSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubScoreForApiResponse, self).to_map()
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
            temp_model = UpdateSubScoreForApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSyncQualityCheckDataRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSyncQualityCheckDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSyncQualityCheckDataResponseBodyData(TeaModel):
    def __init__(self, task_id=None, tid=None):
        self.task_id = task_id  # type: str
        self.tid = tid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSyncQualityCheckDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class UpdateSyncQualityCheckDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateSyncQualityCheckDataResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateSyncQualityCheckDataResponseBody, self).to_map()
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
            temp_model = UpdateSyncQualityCheckDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSyncQualityCheckDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSyncQualityCheckDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSyncQualityCheckDataResponse, self).to_map()
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
            temp_model = UpdateSyncQualityCheckDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskAssignRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskAssignRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskAssignRuleResponseBody, self).to_map()
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


class UpdateTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskAssignRuleResponse, self).to_map()
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
            temp_model = UpdateTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
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


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateUserConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserConfigResponseBody, self).to_map()
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


class UpdateUserConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserConfigResponse, self).to_map()
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
            temp_model = UpdateUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWarningConfigRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWarningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateWarningConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWarningConfigResponseBody, self).to_map()
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


class UpdateWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWarningConfigResponse, self).to_map()
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
            temp_model = UpdateWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadAudioDataRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadAudioDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadAudioDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadAudioDataResponseBody, self).to_map()
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


class UploadAudioDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadAudioDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadAudioDataResponse, self).to_map()
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
            temp_model = UploadAudioDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDataRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataResponseBody, self).to_map()
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


class UploadDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadDataResponse, self).to_map()
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
            temp_model = UploadDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDataSyncRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataSyncResponseBodyDataResultInfoHandScoreIdList(TeaModel):
    def __init__(self, hand_score_id_list=None):
        self.hand_score_id_list = hand_score_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoHandScoreIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            self.hand_score_id_list = m.get('HandScoreIdList')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo(TeaModel):
    def __init__(self, condition_info_cid=None):
        self.condition_info_cid = condition_info_cid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo(TeaModel):
    def __init__(self, condition_basic_info=None):
        self.condition_basic_info = condition_basic_info  # type: list[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo]

    def validate(self):
        if self.condition_basic_info:
            for k in self.condition_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionBasicInfo'] = []
        if self.condition_basic_info is not None:
            for k in self.condition_basic_info:
                result['ConditionBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.condition_basic_info = []
        if m.get('ConditionBasicInfo') is not None:
            for k in m.get('ConditionBasicInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids(TeaModel):
    def __init__(self, cid_item=None):
        self.cid_item = cid_item  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid_item is not None:
            result['CidItem'] = self.cid_item
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidItem') is not None:
            self.cid_item = m.get('CidItem')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord(TeaModel):
    def __init__(self, from_=None, pid=None, tid=None, to=None, val=None):
        self.from_ = from_  # type: int
        self.pid = pid  # type: int
        self.tid = tid  # type: str
        self.to = to  # type: int
        self.val = val  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.to is not None:
            result['To'] = self.to
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords(TeaModel):
    def __init__(self, hit_key_word=None):
        self.hit_key_word = hit_key_word  # type: list[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord]

    def validate(self):
        if self.hit_key_word:
            for k in self.hit_key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitKeyWord'] = []
        if self.hit_key_word is not None:
            for k in self.hit_key_word:
                result['HitKeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit_key_word = []
        if m.get('HitKeyWord') is not None:
            for k in m.get('HitKeyWord'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord()
                self.hit_key_word.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase(TeaModel):
    def __init__(self, begin=None, begin_time=None, end=None, identity=None, role=None, words=None):
        self.begin = begin  # type: long
        self.begin_time = begin_time  # type: str
        self.end = end  # type: long
        self.identity = identity  # type: str
        self.role = role  # type: str
        self.words = words  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end is not None:
            result['End'] = self.end
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.role is not None:
            result['Role'] = self.role
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo(TeaModel):
    def __init__(self, hit_cids=None, hit_key_words=None, phrase=None):
        self.hit_cids = hit_cids  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids
        self.hit_key_words = hit_key_words  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords
        self.phrase = phrase  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase

    def validate(self):
        if self.hit_cids:
            self.hit_cids.validate()
        if self.hit_key_words:
            self.hit_key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_cids is not None:
            result['HitCids'] = self.hit_cids.to_map()
        if self.hit_key_words is not None:
            result['HitKeyWords'] = self.hit_key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitCids') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids()
            self.hit_cids = temp_model.from_map(m['HitCids'])
        if m.get('HitKeyWords') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords()
            self.hit_key_words = temp_model.from_map(m['HitKeyWords'])
        if m.get('Phrase') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit(TeaModel):
    def __init__(self, condition_hit_info=None):
        self.condition_hit_info = condition_hit_info  # type: list[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo]

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k in self.condition_hit_info:
                result['ConditionHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k in m.get('ConditionHitInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo(TeaModel):
    def __init__(self, condition_info=None, hit=None, rid=None, tid=None):
        self.condition_info = condition_info  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo
        self.hit = hit  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit
        self.rid = rid  # type: str
        self.tid = tid  # type: str

    def validate(self):
        if self.condition_info:
            self.condition_info.validate()
        if self.hit:
            self.hit.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_info is not None:
            result['ConditionInfo'] = self.condition_info.to_map()
        if self.hit is not None:
            result['Hit'] = self.hit.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionInfo') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo()
            self.condition_info = temp_model.from_map(m['ConditionInfo'])
        if m.get('Hit') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit()
            self.hit = temp_model.from_map(m['Hit'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class UploadDataSyncResponseBodyDataResultInfoRules(TeaModel):
    def __init__(self, rule_hit_info=None):
        self.rule_hit_info = rule_hit_info  # type: list[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo]

    def validate(self):
        if self.rule_hit_info:
            for k in self.rule_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleHitInfo'] = []
        if self.rule_hit_info is not None:
            for k in self.rule_hit_info:
                result['RuleHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule_hit_info = []
        if m.get('RuleHitInfo') is not None:
            for k in m.get('RuleHitInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo()
                self.rule_hit_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfo(TeaModel):
    def __init__(self, hand_score_id_list=None, rules=None, score=None):
        self.hand_score_id_list = hand_score_id_list  # type: UploadDataSyncResponseBodyDataResultInfoHandScoreIdList
        self.rules = rules  # type: UploadDataSyncResponseBodyDataResultInfoRules
        self.score = score  # type: int

    def validate(self):
        if self.hand_score_id_list:
            self.hand_score_id_list.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyDataResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoHandScoreIdList()
            self.hand_score_id_list = temp_model.from_map(m['HandScoreIdList'])
        if m.get('Rules') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class UploadDataSyncResponseBodyData(TeaModel):
    def __init__(self, result_info=None):
        self.result_info = result_info  # type: list[UploadDataSyncResponseBodyDataResultInfo]

    def validate(self):
        if self.result_info:
            for k in self.result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k in self.result_info:
                result['ResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k in m.get('ResultInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UploadDataSyncResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponseBody, self).to_map()
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
            temp_model = UploadDataSyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataSyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadDataSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadDataSyncResponse, self).to_map()
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
            temp_model = UploadDataSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRuleRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadRuleResponseBodyData(TeaModel):
    def __init__(self, rid_info=None):
        self.rid_info = rid_info  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid_info is not None:
            result['RidInfo'] = self.rid_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RidInfo') is not None:
            self.rid_info = m.get('RidInfo')
        return self


class UploadRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UploadRuleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UploadRuleResponseBody, self).to_map()
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
            temp_model = UploadRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadRuleResponse, self).to_map()
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
            temp_model = UploadRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyFileRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifyFileResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyFileResponseBody, self).to_map()
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


class VerifyFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyFileResponse, self).to_map()
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
            temp_model = VerifyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySentenceRequest(TeaModel):
    def __init__(self, json_str=None):
        self.json_str = json_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifySentenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifySentenceResponseBodyDataDeltaSourceLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifySentenceResponseBodyDataDeltaSourceLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class VerifySentenceResponseBodyDataDeltaSource(TeaModel):
    def __init__(self, line=None, position=None):
        self.line = line  # type: VerifySentenceResponseBodyDataDeltaSourceLine
        self.position = position  # type: int

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(VerifySentenceResponseBodyDataDeltaSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaSourceLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class VerifySentenceResponseBodyDataDeltaTargetLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifySentenceResponseBodyDataDeltaTargetLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class VerifySentenceResponseBodyDataDeltaTarget(TeaModel):
    def __init__(self, line=None, position=None):
        self.line = line  # type: VerifySentenceResponseBodyDataDeltaTargetLine
        self.position = position  # type: int

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(VerifySentenceResponseBodyDataDeltaTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaTargetLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class VerifySentenceResponseBodyDataDelta(TeaModel):
    def __init__(self, source=None, target=None, type=None):
        self.source = source  # type: VerifySentenceResponseBodyDataDeltaSource
        self.target = target  # type: VerifySentenceResponseBodyDataDeltaTarget
        self.type = type  # type: str

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super(VerifySentenceResponseBodyDataDelta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class VerifySentenceResponseBodyData(TeaModel):
    def __init__(self, delta=None):
        self.delta = delta  # type: list[VerifySentenceResponseBodyDataDelta]

    def validate(self):
        if self.delta:
            for k in self.delta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifySentenceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delta'] = []
        if self.delta is not None:
            for k in self.delta:
                result['Delta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k in m.get('Delta'):
                temp_model = VerifySentenceResponseBodyDataDelta()
                self.delta.append(temp_model.from_map(k))
        return self


class VerifySentenceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, incorrect_words=None, message=None, request_id=None, source_role=None,
                 success=None, target_role=None):
        self.code = code  # type: str
        self.data = data  # type: VerifySentenceResponseBodyData
        self.incorrect_words = incorrect_words  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.source_role = source_role  # type: int
        self.success = success  # type: bool
        self.target_role = target_role  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VerifySentenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.success is not None:
            result['Success'] = self.success
        if self.target_role is not None:
            result['TargetRole'] = self.target_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VerifySentenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        return self


class VerifySentenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifySentenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifySentenceResponse, self).to_map()
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
            temp_model = VerifySentenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


