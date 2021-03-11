# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AddBusinessCategoryRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddBusinessCategoryResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBusinessCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddBusinessCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddRuleCategoryResponseBodyData(TeaModel):
    def __init__(self, select=None):
        self.select = select  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: AddRuleCategoryResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = AddRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddThesaurusForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: long
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class AddUploadDataSetRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddUploadDataSetResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: long
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUploadDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddUploadDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AddUploadDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignReviewerRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AssignReviewerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignReviewerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AssignReviewerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ConfigDataSetRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeRange(TeaModel):
    def __init__(self, from_=None, to=None):
        self.from_ = from_  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
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


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeAnchor(TeaModel):
    def __init__(self, cid=None, hit_time=None, location=None):
        self.cid = TeaConverter.to_unicode(cid)  # type: unicode
        self.hit_time = hit_time  # type: int
        self.location = TeaConverter.to_unicode(location)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.hit_time is not None:
            result['HitTime'] = self.hit_time
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRange(TeaModel):
    def __init__(self, range=None, anchor=None, role=None, role_id=None):
        self.range = range  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeRange
        self.anchor = anchor  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeAnchor
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.role_id = role_id  # type: int

    def validate(self):
        if self.range:
            self.range.validate()
        if self.anchor:
            self.anchor.validate()

    def to_map(self):
        result = dict()
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()
        if self.role is not None:
            result['Role'] = self.role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Range') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Anchor') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamKeywords(TeaModel):
    def __init__(self, keywords=None):
        self.keywords = keywords  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam(TeaModel):
    def __init__(self, keywords=None, in_sentence=None):
        self.keywords = keywords  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamKeywords
        self.in_sentence = in_sentence  # type: bool

    def validate(self):
        if self.keywords:
            self.keywords.validate()

    def to_map(self):
        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords.to_map()
        if self.in_sentence is not None:
            result['InSentence'] = self.in_sentence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keywords') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamKeywords()
            self.keywords = temp_model.from_map(m['Keywords'])
        if m.get('InSentence') is not None:
            self.in_sentence = m.get('InSentence')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfo(TeaModel):
    def __init__(self, type=None, oid=None, param=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.oid = TeaConverter.to_unicode(oid)  # type: unicode
        self.param = param  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.oid is not None:
            result['Oid'] = self.oid
        if self.param is not None:
            result['Param'] = self.param.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Oid') is not None:
            self.oid = m.get('Oid')
        if m.get('Param') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam()
            self.param = temp_model.from_map(m['Param'])
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperators(TeaModel):
    def __init__(self, operator_basic_info=None):
        self.operator_basic_info = operator_basic_info  # type: list[ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfo]

    def validate(self):
        if self.operator_basic_info:
            for k in self.operator_basic_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperatorsOperatorBasicInfo()
                self.operator_basic_info.append(temp_model.from_map(k))
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfo(TeaModel):
    def __init__(self, check_range=None, cid=None, operators=None, lambda_=None):
        self.check_range = check_range  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRange
        self.cid = TeaConverter.to_unicode(cid)  # type: unicode
        self.operators = operators  # type: ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperators
        self.lambda_ = TeaConverter.to_unicode(lambda_)  # type: unicode

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            self.operators.validate()

    def to_map(self):
        result = dict()
        if self.check_range is not None:
            result['CheckRange'] = self.check_range.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.operators is not None:
            result['Operators'] = self.operators.to_map()
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckRange') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m['CheckRange'])
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Operators') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfoOperators()
            self.operators = temp_model.from_map(m['Operators'])
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        return self


class ConfigDataSetResponseBodyDataRuleInfoConditions(TeaModel):
    def __init__(self, condition_basic_info=None):
        self.condition_basic_info = condition_basic_info  # type: list[ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfo]

    def validate(self):
        if self.condition_basic_info:
            for k in self.condition_basic_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ConfigDataSetResponseBodyDataRuleInfoConditionsConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k))
        return self


class ConfigDataSetResponseBodyDataRuleInfoRulesRuleBasicInfo(TeaModel):
    def __init__(self, external_property=None, lambda_=None, rid=None):
        self.external_property = external_property  # type: int
        self.lambda_ = TeaConverter.to_unicode(lambda_)  # type: unicode
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.external_property is not None:
            result['ExternalProperty'] = self.external_property
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalProperty') is not None:
            self.external_property = m.get('ExternalProperty')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ConfigDataSetResponseBodyDataRuleInfoRules(TeaModel):
    def __init__(self, rule_basic_info=None):
        self.rule_basic_info = rule_basic_info  # type: list[ConfigDataSetResponseBodyDataRuleInfoRulesRuleBasicInfo]

    def validate(self):
        if self.rule_basic_info:
            for k in self.rule_basic_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ConfigDataSetResponseBodyDataRuleInfoRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k))
        return self


class ConfigDataSetResponseBodyDataRuleInfo(TeaModel):
    def __init__(self, conditions=None, rules=None):
        self.conditions = conditions  # type: ConfigDataSetResponseBodyDataRuleInfoConditions
        self.rules = rules  # type: ConfigDataSetResponseBodyDataRuleInfoRules

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('Rules') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class ConfigDataSetResponseBodyData(TeaModel):
    def __init__(self, rule_info=None, channel_type=None, set_id=None, role_config_status=None, judge_type=None):
        self.rule_info = rule_info  # type: ConfigDataSetResponseBodyDataRuleInfo
        self.channel_type = channel_type  # type: int
        self.set_id = set_id  # type: long
        self.role_config_status = role_config_status  # type: int
        self.judge_type = judge_type  # type: int

    def validate(self):
        if self.rule_info:
            self.rule_info.validate()

    def to_map(self):
        result = dict()
        if self.rule_info is not None:
            result['RuleInfo'] = self.rule_info.to_map()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.role_config_status is not None:
            result['RoleConfigStatus'] = self.role_config_status
        if self.judge_type is not None:
            result['JudgeType'] = self.judge_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleInfo') is not None:
            temp_model = ConfigDataSetResponseBodyDataRuleInfo()
            self.rule_info = temp_model.from_map(m['RuleInfo'])
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RoleConfigStatus') is not None:
            self.role_config_status = m.get('RoleConfigStatus')
        if m.get('JudgeType') is not None:
            self.judge_type = m.get('JudgeType')
        return self


class ConfigDataSetResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ConfigDataSetResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ConfigDataSetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ConfigDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsrVocabRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateAsrVocabResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class CreateRuleRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: long
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSkillGroupConfigRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: long
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateWarningConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DeleteAsrVocabRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteAsrVocabResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteBusinessCategoryResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBusinessCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteBusinessCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteCustomizationConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomizationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteCustomizationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeletePrecisionTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeletePrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteSubScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteWarningConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DelRuleCategoryRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DelRuleCategoryResponseBodyData(TeaModel):
    def __init__(self, select=None):
        self.select = select  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DelRuleCategoryResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DelRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DelRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DelThesaurusForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DelThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class EditThesaurusForApiRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class EditThesaurusForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: long
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditThesaurusForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EditThesaurusForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetAsrVocabResponseBodyDataWordsWord(TeaModel):
    def __init__(self, weight=None, word=None):
        self.weight = weight  # type: int
        self.word = TeaConverter.to_unicode(word)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, words=None, name=None):
        self.words = words  # type: GetAsrVocabResponseBodyDataWords
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            temp_model = GetAsrVocabResponseBodyDataWords()
            self.words = temp_model.from_map(m['Words'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAsrVocabResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetAsrVocabResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo(TeaModel):
    def __init__(self, business_name=None, service_type=None, bid=None):
        self.business_name = TeaConverter.to_unicode(business_name)  # type: unicode
        self.service_type = service_type  # type: int
        self.bid = bid  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.bid is not None:
            result['Bid'] = self.bid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetBusinessCategoryListResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetBusinessCategoryListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBusinessCategoryListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetBusinessCategoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo(TeaModel):
    def __init__(self, task_type=None, create_time=None, model_status=None, model_name=None, model_id=None,
                 mode_customization_id=None):
        self.task_type = task_type  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.model_status = model_status  # type: int
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.model_id = model_id  # type: long
        self.mode_customization_id = TeaConverter.to_unicode(mode_customization_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetCustomizationConfigListResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetCustomizationConfigListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomizationConfigListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetCustomizationConfigListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetHitResultResponseBodyDataResultInfo(TeaModel):
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: GetHitResultResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = GetHitResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHitResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetHitResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.line = line  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, type=None, source=None, target=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.source = source  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource
        self.target = target  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Source') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
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
    def __init__(self, deltas=None, words=None, identity=None, incorrect_words=None, begin_time=None,
                 source_words=None, end=None, speech_rate=None, source_role=None, hour_min_sec=None, begin=None,
                 emotion_value=None, role=None, silence_duration=None):
        self.deltas = deltas  # type: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.incorrect_words = incorrect_words  # type: int
        self.begin_time = TeaConverter.to_unicode(begin_time)  # type: unicode
        self.source_words = TeaConverter.to_unicode(source_words)  # type: unicode
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.source_role = TeaConverter.to_unicode(source_role)  # type: unicode
        self.hour_min_sec = TeaConverter.to_unicode(hour_min_sec)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int

    def validate(self):
        if self.deltas:
            self.deltas.validate()

    def to_map(self):
        result = dict()
        if self.deltas is not None:
            result['Deltas'] = self.deltas.to_map()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.source_words is not None:
            result['SourceWords'] = self.source_words
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deltas') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas()
            self.deltas = temp_model.from_map(m['Deltas'])
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('SourceWords') is not None:
            self.source_words = m.get('SourceWords')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
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
    def __init__(self, audio_scheme=None, status=None, index=None, audio_url=None, update_time=None,
                 incorrect_words=None, verified_count=None, verified=None, file_name=None, total_count=None, precision=None,
                 file_id=None, dialogues=None, duration=None):
        self.audio_scheme = TeaConverter.to_unicode(audio_scheme)  # type: unicode
        self.status = status  # type: int
        self.index = index  # type: int
        self.audio_url = TeaConverter.to_unicode(audio_url)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.incorrect_words = incorrect_words  # type: int
        self.verified_count = verified_count  # type: int
        self.verified = verified  # type: bool
        self.file_name = TeaConverter.to_unicode(file_name)  # type: unicode
        self.total_count = total_count  # type: int
        self.precision = precision  # type: float
        self.file_id = TeaConverter.to_unicode(file_id)  # type: unicode
        self.dialogues = dialogues  # type: GetNextResultToVerifyResponseBodyDataDialogues
        self.duration = duration  # type: int

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()

    def to_map(self):
        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.status is not None:
            result['Status'] = self.status
        if self.index is not None:
            result['Index'] = self.index
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        if self.verified is not None:
            result['Verified'] = self.verified
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        if m.get('Verified') is not None:
            self.verified = m.get('Verified')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Dialogues') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class GetNextResultToVerifyResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetNextResultToVerifyResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetNextResultToVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNextResultToVerifyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetNextResultToVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetPrecisionTaskResponseBodyDataPrecisionsPrecision(TeaModel):
    def __init__(self, status=None, model_name=None, task_id=None, precision=None, model_id=None):
        self.status = status  # type: int
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.precision = precision  # type: float
        self.model_id = model_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
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
    def __init__(self, status=None, update_time=None, incorrect_words=None, data_set_id=None, verified_count=None,
                 total_count=None, source=None, precisions=None, duration=None, data_set_name=None, name=None, task_id=None):
        self.status = status  # type: int
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.incorrect_words = incorrect_words  # type: int
        self.data_set_id = data_set_id  # type: long
        self.verified_count = verified_count  # type: int
        self.total_count = total_count  # type: int
        self.source = source  # type: int
        self.precisions = precisions  # type: GetPrecisionTaskResponseBodyDataPrecisions
        self.duration = duration  # type: int
        self.data_set_name = TeaConverter.to_unicode(data_set_name)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.source is not None:
            result['Source'] = self.source
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.name is not None:
            result['Name'] = self.name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Precisions') is not None:
            temp_model = GetPrecisionTaskResponseBodyDataPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetPrecisionTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetPrecisionTaskResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultResponseBodyDataResultInfoAgent(TeaModel):
    def __init__(self, name=None, skill_group=None, id=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.skill_group = TeaConverter.to_unicode(skill_group)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetResultResponseBodyDataResultInfoAsrResultAsrResult(TeaModel):
    def __init__(self, words=None, begin=None, emotion_value=None, end=None, speech_rate=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
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


class GetResultResponseBodyDataResultInfoHitScoreHitScore(TeaModel):
    def __init__(self, score_name=None, score_number=None, score_id=None, rule_id=None):
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.score_number = TeaConverter.to_unicode(score_number)  # type: unicode
        self.score_id = TeaConverter.to_unicode(score_id)  # type: unicode
        self.rule_id = TeaConverter.to_unicode(rule_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_number is not None:
            result['ScoreNumber'] = self.score_number
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreNumber') is not None:
            self.score_number = m.get('ScoreNumber')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
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


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase(TeaModel):
    def __init__(self, words=None, begin=None, emotion_value=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord(TeaModel):
    def __init__(self, from_=None, val=None, cid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.cid = TeaConverter.to_unicode(cid)  # type: unicode
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('To') is not None:
            self.to = m.get('To')
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


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase
        self.key_words = key_words  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords
        self.cid = cid  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            self.key_words.validate()
        if self.cid:
            self.cid.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Cid') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid()
            self.cid = temp_model.from_map(m['Cid'])
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
    def __init__(self, type=None, hits=None, review_result=None, name=None, rid=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.hits = hits  # type: GetResultResponseBodyDataResultInfoHitResultHitResultHits
        self.review_result = review_result  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        if self.hits:
            self.hits.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.hits is not None:
            result['Hits'] = self.hits.to_map()
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Hits') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHits()
            self.hits = temp_model.from_map(m['Hits'])
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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


class GetResultResponseBodyDataResultInfoRecording(TeaModel):
    def __init__(self, remark_13=None, callee=None, primary_id=None, remark_12=None, remark_1=None, remark_7=None,
                 remark_8=None, remark_2=None, call_id=None, remark_9=None, name=None, remark_6=None, remark_10=None,
                 remark_3=None, business=None, url=None, remark_11=None, remark_4=None, call_type=None, caller=None,
                 duration=None, data_set_name=None, remark_5=None, id=None, call_time=None):
        self.remark_13 = TeaConverter.to_unicode(remark_13)  # type: unicode
        self.callee = TeaConverter.to_unicode(callee)  # type: unicode
        self.primary_id = TeaConverter.to_unicode(primary_id)  # type: unicode
        self.remark_12 = TeaConverter.to_unicode(remark_12)  # type: unicode
        self.remark_1 = TeaConverter.to_unicode(remark_1)  # type: unicode
        self.remark_7 = TeaConverter.to_unicode(remark_7)  # type: unicode
        self.remark_8 = TeaConverter.to_unicode(remark_8)  # type: unicode
        self.remark_2 = TeaConverter.to_unicode(remark_2)  # type: unicode
        self.call_id = TeaConverter.to_unicode(call_id)  # type: unicode
        self.remark_9 = TeaConverter.to_unicode(remark_9)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.remark_6 = TeaConverter.to_unicode(remark_6)  # type: unicode
        self.remark_10 = TeaConverter.to_unicode(remark_10)  # type: unicode
        self.remark_3 = TeaConverter.to_unicode(remark_3)  # type: unicode
        self.business = TeaConverter.to_unicode(business)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.remark_11 = TeaConverter.to_unicode(remark_11)  # type: unicode
        self.remark_4 = TeaConverter.to_unicode(remark_4)  # type: unicode
        self.call_type = call_type  # type: int
        self.caller = TeaConverter.to_unicode(caller)  # type: unicode
        self.duration = duration  # type: long
        self.data_set_name = TeaConverter.to_unicode(data_set_name)  # type: unicode
        self.remark_5 = remark_5  # type: long
        self.id = TeaConverter.to_unicode(id)  # type: unicode
        self.call_time = TeaConverter.to_unicode(call_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark_13 is not None:
            result['Remark13'] = self.remark_13
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_12 is not None:
            result['Remark12'] = self.remark_12
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.remark_7 is not None:
            result['Remark7'] = self.remark_7
        if self.remark_8 is not None:
            result['Remark8'] = self.remark_8
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.remark_9 is not None:
            result['Remark9'] = self.remark_9
        if self.name is not None:
            result['Name'] = self.name
        if self.remark_6 is not None:
            result['Remark6'] = self.remark_6
        if self.remark_10 is not None:
            result['Remark10'] = self.remark_10
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.business is not None:
            result['Business'] = self.business
        if self.url is not None:
            result['Url'] = self.url
        if self.remark_11 is not None:
            result['Remark11'] = self.remark_11
        if self.remark_4 is not None:
            result['Remark4'] = self.remark_4
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.remark_5 is not None:
            result['Remark5'] = self.remark_5
        if self.id is not None:
            result['Id'] = self.id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Remark13') is not None:
            self.remark_13 = m.get('Remark13')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark12') is not None:
            self.remark_12 = m.get('Remark12')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('Remark7') is not None:
            self.remark_7 = m.get('Remark7')
        if m.get('Remark8') is not None:
            self.remark_8 = m.get('Remark8')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Remark9') is not None:
            self.remark_9 = m.get('Remark9')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark6') is not None:
            self.remark_6 = m.get('Remark6')
        if m.get('Remark10') is not None:
            self.remark_10 = m.get('Remark10')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Remark11') is not None:
            self.remark_11 = m.get('Remark11')
        if m.get('Remark4') is not None:
            self.remark_4 = m.get('Remark4')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Remark5') is not None:
            self.remark_5 = m.get('Remark5')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class GetResultResponseBodyDataResultInfo(TeaModel):
    def __init__(self, status=None, assignment_time=None, last_data_id=None, error_message=None, review_status=None,
                 create_time=None, reviewer=None, task_name=None, review_time_long=None, score=None, review_result=None,
                 agent=None, create_time_long=None, asr_result=None, review_time=None, hit_score=None, comments=None,
                 hit_result=None, recording=None, task_id=None, review_type=None, resolver=None):
        self.status = status  # type: int
        self.assignment_time = TeaConverter.to_unicode(assignment_time)  # type: unicode
        self.last_data_id = TeaConverter.to_unicode(last_data_id)  # type: unicode
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.review_status = review_status  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.reviewer = TeaConverter.to_unicode(reviewer)  # type: unicode
        self.task_name = TeaConverter.to_unicode(task_name)  # type: unicode
        self.review_time_long = TeaConverter.to_unicode(review_time_long)  # type: unicode
        self.score = score  # type: int
        self.review_result = review_result  # type: int
        self.agent = agent  # type: GetResultResponseBodyDataResultInfoAgent
        self.create_time_long = TeaConverter.to_unicode(create_time_long)  # type: unicode
        self.asr_result = asr_result  # type: GetResultResponseBodyDataResultInfoAsrResult
        self.review_time = TeaConverter.to_unicode(review_time)  # type: unicode
        self.hit_score = hit_score  # type: GetResultResponseBodyDataResultInfoHitScore
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.hit_result = hit_result  # type: GetResultResponseBodyDataResultInfoHitResult
        self.recording = recording  # type: GetResultResponseBodyDataResultInfoRecording
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.review_type = review_type  # type: int
        self.resolver = TeaConverter.to_unicode(resolver)  # type: unicode

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            self.asr_result.validate()
        if self.hit_score:
            self.hit_score.validate()
        if self.hit_result:
            self.hit_result.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.assignment_time is not None:
            result['AssignmentTime'] = self.assignment_time
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.review_time_long is not None:
            result['ReviewTimeLong'] = self.review_time_long
        if self.score is not None:
            result['Score'] = self.score
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.asr_result is not None:
            result['AsrResult'] = self.asr_result.to_map()
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.hit_score is not None:
            result['HitScore'] = self.hit_score.to_map()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.hit_result is not None:
            result['HitResult'] = self.hit_result.to_map()
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.review_type is not None:
            result['ReviewType'] = self.review_type
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AssignmentTime') is not None:
            self.assignment_time = m.get('AssignmentTime')
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ReviewTimeLong') is not None:
            self.review_time_long = m.get('ReviewTimeLong')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Agent') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAgent()
            self.agent = temp_model.from_map(m['Agent'])
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('AsrResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAsrResult()
            self.asr_result = temp_model.from_map(m['AsrResult'])
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('HitScore') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitScore()
            self.hit_score = temp_model.from_map(m['HitScore'])
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('HitResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResult()
            self.hit_result = temp_model.from_map(m['HitResult'])
        if m.get('Recording') is not None:
            temp_model = GetResultResponseBodyDataResultInfoRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ReviewType') is not None:
            self.review_type = m.get('ReviewType')
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None, result_count_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: GetResultResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool
        self.result_count_id = TeaConverter.to_unicode(result_count_id)  # type: unicode

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = GetResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        return self


class GetResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultCallbackResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetResultCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory(TeaModel):
    def __init__(self, type=None, operator_name=None, time_str=None, score=None, review_result=None,
                 complain_result=None, old_score=None):
        self.type = type  # type: int
        self.operator_name = TeaConverter.to_unicode(operator_name)  # type: unicode
        self.time_str = TeaConverter.to_unicode(time_str)  # type: unicode
        self.score = score  # type: int
        self.review_result = review_result  # type: int
        self.complain_result = complain_result  # type: int
        self.old_score = old_score  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.time_str is not None:
            result['TimeStr'] = self.time_str
        if self.score is not None:
            result['Score'] = self.score
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.complain_result is not None:
            result['ComplainResult'] = self.complain_result
        if self.old_score is not None:
            result['OldScore'] = self.old_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('TimeStr') is not None:
            self.time_str = m.get('TimeStr')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ComplainResult') is not None:
            self.complain_result = m.get('ComplainResult')
        if m.get('OldScore') is not None:
            self.old_score = m.get('OldScore')
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


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(self, words=None, begin=None, identity=None, pid=None, emotion_value=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.pid = pid  # type: int
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(self, from_=None, val=None, pid=None, tid=None, cid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.pid = pid  # type: int
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.cid = TeaConverter.to_unicode(cid)  # type: unicode
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('To') is not None:
            self.to = m.get('To')
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


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase
        self.key_words = key_words  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords
        self.cid = cid  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            self.key_words.validate()
        if self.cid:
            self.cid.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Cid') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
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
    def __init__(self, review_time=None, reviewer=None, review_result=None, hit_id=None, rid=None):
        self.review_time = TeaConverter.to_unicode(review_time)  # type: unicode
        self.reviewer = TeaConverter.to_unicode(reviewer)  # type: unicode
        self.review_result = review_result  # type: int
        self.hit_id = TeaConverter.to_unicode(hit_id)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.hit_id is not None:
            result['HitId'] = self.hit_id
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories(TeaModel):
    def __init__(self, operator_name=None, comments=None, operator=None, operation_time=None, operation_type=None):
        self.operator_name = TeaConverter.to_unicode(operator_name)  # type: unicode
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.operator = operator  # type: long
        self.operation_time = TeaConverter.to_unicode(operation_time)  # type: unicode
        self.operation_type = operation_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
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


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(self, condition_hit_info_list=None, score_sub_id=None, review_info=None, rule_name=None, rid=None,
                 score_sub_name=None, score_num=None, auto_review=None, complain_histories=None, complainable=None, score_id=None):
        self.condition_hit_info_list = condition_hit_info_list  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList
        self.score_sub_id = score_sub_id  # type: long
        self.review_info = review_info  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_num = score_num  # type: int
        self.auto_review = auto_review  # type: int
        self.complain_histories = complain_histories  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories
        self.complainable = complainable  # type: bool
        self.score_id = score_id  # type: long

    def validate(self):
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()
        if self.complain_histories:
            self.complain_histories.validate()

    def to_map(self):
        result = dict()
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionHitInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ReviewInfo') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m['ReviewInfo'])
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
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
    def __init__(self, operator_name=None, comments=None, operator=None, operation_time=None, operation_type=None):
        self.operator_name = TeaConverter.to_unicode(operator_name)  # type: unicode
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.operator = operator  # type: long
        self.operation_time = TeaConverter.to_unicode(operation_time)  # type: unicode
        self.operation_type = operation_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
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
    def __init__(self, score_sub_name=None, score_num=None, score_sub_id=None, complain_histories=None,
                 complainable=None, score_id=None):
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.complain_histories = complain_histories  # type: GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories
        self.complainable = complainable  # type: bool
        self.score_id = score_id  # type: long

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()

    def to_map(self):
        result = dict()
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
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


class GetResultToReviewResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(self, words=None, identity=None, begin=None, begin_time=None, emotion_value=None, end=None,
                 speech_rate=None, role=None, silence_duration=None, hour_min_sec=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.begin = begin  # type: long
        self.begin_time = TeaConverter.to_unicode(begin_time)  # type: unicode
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int
        self.hour_min_sec = TeaConverter.to_unicode(hour_min_sec)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
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


class GetResultToReviewResponseBodyData(TeaModel):
    def __init__(self, audio_scheme=None, audio_url=None, review_history_list=None, hit_rule_review_info_list=None,
                 total_score=None, file_id=None, manual_score_info_list=None, file_merge_name=None, comments=None,
                 dialogues=None, vid=None):
        self.audio_scheme = TeaConverter.to_unicode(audio_scheme)  # type: unicode
        self.audio_url = TeaConverter.to_unicode(audio_url)  # type: unicode
        self.review_history_list = review_history_list  # type: GetResultToReviewResponseBodyDataReviewHistoryList
        self.hit_rule_review_info_list = hit_rule_review_info_list  # type: GetResultToReviewResponseBodyDataHitRuleReviewInfoList
        self.total_score = total_score  # type: int
        self.file_id = TeaConverter.to_unicode(file_id)  # type: unicode
        self.manual_score_info_list = manual_score_info_list  # type: GetResultToReviewResponseBodyDataManualScoreInfoList
        self.file_merge_name = TeaConverter.to_unicode(file_merge_name)  # type: unicode
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.dialogues = dialogues  # type: GetResultToReviewResponseBodyDataDialogues
        self.vid = TeaConverter.to_unicode(vid)  # type: unicode

    def validate(self):
        if self.review_history_list:
            self.review_history_list.validate()
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_info_list:
            self.manual_score_info_list.validate()
        if self.dialogues:
            self.dialogues.validate()

    def to_map(self):
        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.manual_score_info_list is not None:
            result['ManualScoreInfoList'] = self.manual_score_info_list.to_map()
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('ReviewHistoryList') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewHistoryList()
            self.review_history_list = temp_model.from_map(m['ReviewHistoryList'])
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ManualScoreInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoList()
            self.manual_score_info_list = temp_model.from_map(m['ManualScoreInfoList'])
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Dialogues') is not None:
            temp_model = GetResultToReviewResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetResultToReviewResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetResultToReviewResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetResultToReviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultToReviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetResultToReviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class GetReviewInfoRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(self, words=None, begin=None, identity=None, pid=None, emotion_value=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.pid = pid  # type: int
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(self, from_=None, val=None, tid=None, pid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.pid = pid  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(TeaModel):
    def __init__(self, key_word=None):
        self.key_word = key_word  # type: list[GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord]

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase
        self.key_words = key_words  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords
        self.cid = cid  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            self.key_words.validate()
        if self.cid:
            self.cid.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('KeyWords') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Cid') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(TeaModel):
    def __init__(self, condition_hit_info=None):
        self.condition_hit_info = condition_hit_info  # type: list[GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo]

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo(TeaModel):
    def __init__(self, hit_id=None, rid=None):
        self.hit_id = TeaConverter.to_unicode(hit_id)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hit_id is not None:
            result['HitId'] = self.hit_id
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(self, rule_score_type=None, condition_hit_info_list=None, rule_type=None, auto_review=None,
                 score_sub_id=None, review_info=None, total_number=None, score_id=None, rid=None, rule_name=None):
        self.rule_score_type = rule_score_type  # type: int
        self.condition_hit_info_list = condition_hit_info_list  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList
        self.rule_type = rule_type  # type: int
        self.auto_review = auto_review  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.review_info = review_info  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo
        self.total_number = total_number  # type: int
        self.score_id = score_id  # type: long
        self.rid = rid  # type: long
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode

    def validate(self):
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()

    def to_map(self):
        result = dict()
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('ConditionHitInfoList') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ReviewInfo') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m['ReviewInfo'])
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetReviewInfoResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(self, hit_rule_review_info=None):
        self.hit_rule_review_info = hit_rule_review_info  # type: list[GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo]

    def validate(self):
        if self.hit_rule_review_info:
            for k in self.hit_rule_review_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyDataManualScoreMappingList(TeaModel):
    def __init__(self, manual_score_mapping_list=None):
        self.manual_score_mapping_list = manual_score_mapping_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.manual_score_mapping_list is not None:
            result['ManualScoreMappingList'] = self.manual_score_mapping_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ManualScoreMappingList') is not None:
            self.manual_score_mapping_list = m.get('ManualScoreMappingList')
        return self


class GetReviewInfoResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(self, words=None, identity=None, begin=None, begin_time=None, emotion_value=None, end=None,
                 speech_rate=None, role=None, silence_duration=None, hour_min_sec=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.begin = begin  # type: long
        self.begin_time = TeaConverter.to_unicode(begin_time)  # type: unicode
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int
        self.hour_min_sec = TeaConverter.to_unicode(hour_min_sec)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        return self


class GetReviewInfoResponseBodyDataDialogues(TeaModel):
    def __init__(self, dialogue=None):
        self.dialogue = dialogue  # type: list[GetReviewInfoResponseBodyDataDialoguesDialogue]

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam(TeaModel):
    def __init__(self, score_sub_name=None, score_num=None, score_sub_id=None, score_type=None, hit=None):
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.score_type = score_type  # type: int
        self.hit = hit  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.hit is not None:
            result['Hit'] = self.hit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        return self


class GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfos(TeaModel):
    def __init__(self, score_param=None):
        self.score_param = score_param  # type: list[GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam]

    def validate(self):
        if self.score_param:
            for k in self.score_param:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam()
                self.score_param.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyDataHandScoreInfoListScorePo(TeaModel):
    def __init__(self, score_infos=None, score_name=None, score_id=None):
        self.score_infos = score_infos  # type: GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfos
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.score_id = score_id  # type: long

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        result = dict()
        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreInfos') is not None:
            temp_model = GetReviewInfoResponseBodyDataHandScoreInfoListScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m['ScoreInfos'])
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        return self


class GetReviewInfoResponseBodyDataHandScoreInfoList(TeaModel):
    def __init__(self, score_po=None):
        self.score_po = score_po  # type: list[GetReviewInfoResponseBodyDataHandScoreInfoListScorePo]

    def validate(self):
        if self.score_po:
            for k in self.score_po:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetReviewInfoResponseBodyDataHandScoreInfoListScorePo()
                self.score_po.append(temp_model.from_map(k))
        return self


class GetReviewInfoResponseBodyData(TeaModel):
    def __init__(self, audio_url=None, hit_number=None, next_vid=None, pre_vid=None, is_audio=None,
                 hit_rule_review_info_list=None, audio=None, asr_words_count=None, total_score=None, business_type=None,
                 manual_score_mapping_list=None, file_merge_name=None, is_deleted=None, dialogues=None, deleted=None,
                 hand_score_info_list=None, vid=None, review_number=None):
        self.audio_url = TeaConverter.to_unicode(audio_url)  # type: unicode
        self.hit_number = hit_number  # type: int
        self.next_vid = TeaConverter.to_unicode(next_vid)  # type: unicode
        self.pre_vid = TeaConverter.to_unicode(pre_vid)  # type: unicode
        self.is_audio = is_audio  # type: bool
        self.hit_rule_review_info_list = hit_rule_review_info_list  # type: GetReviewInfoResponseBodyDataHitRuleReviewInfoList
        self.audio = audio  # type: bool
        self.asr_words_count = asr_words_count  # type: int
        self.total_score = total_score  # type: int
        self.business_type = business_type  # type: int
        self.manual_score_mapping_list = manual_score_mapping_list  # type: GetReviewInfoResponseBodyDataManualScoreMappingList
        self.file_merge_name = TeaConverter.to_unicode(file_merge_name)  # type: unicode
        self.is_deleted = is_deleted  # type: bool
        self.dialogues = dialogues  # type: GetReviewInfoResponseBodyDataDialogues
        self.deleted = deleted  # type: bool
        self.hand_score_info_list = hand_score_info_list  # type: GetReviewInfoResponseBodyDataHandScoreInfoList
        self.vid = TeaConverter.to_unicode(vid)  # type: unicode
        self.review_number = review_number  # type: int

    def validate(self):
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_mapping_list:
            self.manual_score_mapping_list.validate()
        if self.dialogues:
            self.dialogues.validate()
        if self.hand_score_info_list:
            self.hand_score_info_list.validate()

    def to_map(self):
        result = dict()
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.next_vid is not None:
            result['NextVid'] = self.next_vid
        if self.pre_vid is not None:
            result['PreVid'] = self.pre_vid
        if self.is_audio is not None:
            result['IsAudio'] = self.is_audio
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.asr_words_count is not None:
            result['AsrWordsCount'] = self.asr_words_count
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.manual_score_mapping_list is not None:
            result['ManualScoreMappingList'] = self.manual_score_mapping_list.to_map()
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.hand_score_info_list is not None:
            result['HandScoreInfoList'] = self.hand_score_info_list.to_map()
        if self.vid is not None:
            result['Vid'] = self.vid
        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('NextVid') is not None:
            self.next_vid = m.get('NextVid')
        if m.get('PreVid') is not None:
            self.pre_vid = m.get('PreVid')
        if m.get('IsAudio') is not None:
            self.is_audio = m.get('IsAudio')
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = GetReviewInfoResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('AsrWordsCount') is not None:
            self.asr_words_count = m.get('AsrWordsCount')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('ManualScoreMappingList') is not None:
            temp_model = GetReviewInfoResponseBodyDataManualScoreMappingList()
            self.manual_score_mapping_list = temp_model.from_map(m['ManualScoreMappingList'])
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Dialogues') is not None:
            temp_model = GetReviewInfoResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('HandScoreInfoList') is not None:
            temp_model = GetReviewInfoResponseBodyDataHandScoreInfoList()
            self.hand_score_info_list = temp_model.from_map(m['HandScoreInfoList'])
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')
        return self


class GetReviewInfoResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetReviewInfoResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetReviewInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetReviewInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetReviewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetReviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList(TeaModel):
    def __init__(self, business_category_name_list=None):
        self.business_category_name_list = business_category_name_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, type=None, status=None, business_category_name_list=None, is_online=None, score_sub_id=None,
                 create_empid=None, create_time=None, last_update_empid=None, is_delete=None, rid=None, end_time=None,
                 rule_score_type=None, weight=None, start_time=None, rule_lambda=None, score_sub_name=None, auto_review=None,
                 comments=None, last_update_time=None, score_name=None, name=None, score_id=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.business_category_name_list = business_category_name_list  # type: GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList
        self.is_online = is_online  # type: int
        self.score_sub_id = score_sub_id  # type: int
        self.create_empid = TeaConverter.to_unicode(create_empid)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.last_update_empid = TeaConverter.to_unicode(last_update_empid)  # type: unicode
        self.is_delete = is_delete  # type: int
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.rule_score_type = rule_score_type  # type: int
        self.weight = TeaConverter.to_unicode(weight)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.rule_lambda = TeaConverter.to_unicode(rule_lambda)  # type: unicode
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.auto_review = auto_review  # type: int
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.last_update_time = TeaConverter.to_unicode(last_update_time)  # type: unicode
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.score_id = score_id  # type: int

    def validate(self):
        if self.business_category_name_list:
            self.business_category_name_list.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list.to_map()
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.name is not None:
            result['Name'] = self.name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessCategoryNameList') is not None:
            temp_model = GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList()
            self.business_category_name_list = temp_model.from_map(m['BusinessCategoryNameList'])
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetRuleResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleCategoryResponseBodyDataRuleCountInfo(TeaModel):
    def __init__(self, type=None, select=None, type_name=None):
        self.type = type  # type: int
        self.select = select  # type: bool
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.select is not None:
            result['Select'] = self.select
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Select') is not None:
            self.select = m.get('Select')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetRuleCategoryResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetRuleCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords(TeaModel):
    def __init__(self, oper_key_word=None):
        self.oper_key_word = oper_key_word  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.oper_key_word is not None:
            result['OperKeyWord'] = self.oper_key_word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperKeyWord') is not None:
            self.oper_key_word = m.get('OperKeyWord')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences(TeaModel):
    def __init__(self, reference=None):
        self.reference = reference  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.similarly_sentence = similarly_sentence  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.similarly_sentence is not None:
            result['SimilarlySentence'] = self.similarly_sentence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SimilarlySentence') is not None:
            self.similarly_sentence = m.get('SimilarlySentence')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes(TeaModel):
    def __init__(self, excludes=None):
        self.excludes = excludes  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam(TeaModel):
    def __init__(self, regex=None, phrase=None, interval=None, threshold=None, in_sentence=None, target=None,
                 from_end=None, different_role=None, target_role=None, score=None, context_chat_match=None,
                 keyword_match_size=None, average=None, velocity_in_mint=None, min_word_size=None, keyword_extension=None,
                 hit_time=None, from_=None, begin_type=None, compare_operator=None, check_type=None,
                 max_emotion_change_value=None, oper_key_words=None, references=None, similarly_sentences=None, excludes=None):
        self.regex = TeaConverter.to_unicode(regex)  # type: unicode
        self.phrase = TeaConverter.to_unicode(phrase)  # type: unicode
        self.interval = interval  # type: int
        self.threshold = threshold  # type: float
        self.in_sentence = in_sentence  # type: bool
        self.target = target  # type: int
        self.from_end = from_end  # type: bool
        self.different_role = different_role  # type: bool
        self.target_role = TeaConverter.to_unicode(target_role)  # type: unicode
        self.score = score  # type: int
        self.context_chat_match = context_chat_match  # type: bool
        self.keyword_match_size = keyword_match_size  # type: int
        self.average = average  # type: bool
        self.velocity_in_mint = velocity_in_mint  # type: int
        self.min_word_size = min_word_size  # type: int
        self.keyword_extension = keyword_extension  # type: bool
        self.hit_time = hit_time  # type: int
        self.from_ = from_  # type: int
        self.begin_type = TeaConverter.to_unicode(begin_type)  # type: unicode
        self.compare_operator = TeaConverter.to_unicode(compare_operator)  # type: unicode
        self.check_type = check_type  # type: int
        self.max_emotion_change_value = max_emotion_change_value  # type: int
        self.oper_key_words = oper_key_words  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords
        self.references = references  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences
        self.similarly_sentences = similarly_sentences  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences
        self.excludes = excludes  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes

    def validate(self):
        if self.oper_key_words:
            self.oper_key_words.validate()
        if self.references:
            self.references.validate()
        if self.similarly_sentences:
            self.similarly_sentences.validate()
        if self.excludes:
            self.excludes.validate()

    def to_map(self):
        result = dict()
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.phrase is not None:
            result['Phrase'] = self.phrase
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.in_sentence is not None:
            result['InSentence'] = self.in_sentence
        if self.target is not None:
            result['Target'] = self.target
        if self.from_end is not None:
            result['FromEnd'] = self.from_end
        if self.different_role is not None:
            result['DifferentRole'] = self.different_role
        if self.target_role is not None:
            result['TargetRole'] = self.target_role
        if self.score is not None:
            result['Score'] = self.score
        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match
        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size
        if self.average is not None:
            result['Average'] = self.average
        if self.velocity_in_mint is not None:
            result['VelocityInMint'] = self.velocity_in_mint
        if self.min_word_size is not None:
            result['MinWordSize'] = self.min_word_size
        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension
        if self.hit_time is not None:
            result['HitTime'] = self.hit_time
        if self.from_ is not None:
            result['From'] = self.from_
        if self.begin_type is not None:
            result['BeginType'] = self.begin_type
        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.max_emotion_change_value is not None:
            result['MaxEmotionChangeValue'] = self.max_emotion_change_value
        if self.oper_key_words is not None:
            result['OperKeyWords'] = self.oper_key_words.to_map()
        if self.references is not None:
            result['References'] = self.references.to_map()
        if self.similarly_sentences is not None:
            result['SimilarlySentences'] = self.similarly_sentences.to_map()
        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('InSentence') is not None:
            self.in_sentence = m.get('InSentence')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('FromEnd') is not None:
            self.from_end = m.get('FromEnd')
        if m.get('DifferentRole') is not None:
            self.different_role = m.get('DifferentRole')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')
        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('VelocityInMint') is not None:
            self.velocity_in_mint = m.get('VelocityInMint')
        if m.get('MinWordSize') is not None:
            self.min_word_size = m.get('MinWordSize')
        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')
        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')
        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('MaxEmotionChangeValue') is not None:
            self.max_emotion_change_value = m.get('MaxEmotionChangeValue')
        if m.get('OperKeyWords') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords()
            self.oper_key_words = temp_model.from_map(m['OperKeyWords'])
        if m.get('References') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences()
            self.references = temp_model.from_map(m['References'])
        if m.get('SimilarlySentences') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences()
            self.similarly_sentences = temp_model.from_map(m['SimilarlySentences'])
        if m.get('Excludes') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes()
            self.excludes = temp_model.from_map(m['Excludes'])
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo(TeaModel):
    def __init__(self, oid=None, type=None, oper_name=None, param=None):
        self.oid = TeaConverter.to_unicode(oid)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.oper_name = TeaConverter.to_unicode(oper_name)  # type: unicode
        self.param = param  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        if self.oid is not None:
            result['Oid'] = self.oid
        if self.type is not None:
            result['Type'] = self.type
        if self.oper_name is not None:
            result['OperName'] = self.oper_name
        if self.param is not None:
            result['Param'] = self.param.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Oid') is not None:
            self.oid = m.get('Oid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperName') is not None:
            self.oper_name = m.get('OperName')
        if m.get('Param') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam()
            self.param = temp_model.from_map(m['Param'])
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


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor(TeaModel):
    def __init__(self, anchor_cid=None, location=None, hit_time=None):
        self.anchor_cid = TeaConverter.to_unicode(anchor_cid)  # type: unicode
        self.location = TeaConverter.to_unicode(location)  # type: unicode
        self.hit_time = hit_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.anchor_cid is not None:
            result['AnchorCid'] = self.anchor_cid
        if self.location is not None:
            result['Location'] = self.location
        if self.hit_time is not None:
            result['HitTime'] = self.hit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorCid') is not None:
            self.anchor_cid = m.get('AnchorCid')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange(TeaModel):
    def __init__(self, from_=None, to=None):
        self.from_ = from_  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, role=None, absolute=None, anchor=None, range=None):
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.absolute = absolute  # type: bool
        self.anchor = anchor  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor
        self.range = range  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.absolute is not None:
            result['Absolute'] = self.absolute
        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()
        if self.range is not None:
            result['Range'] = self.range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')
        if m.get('Anchor') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Range') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfo(TeaModel):
    def __init__(self, condition_info_cid=None, oper_lambda=None, operators=None, check_range=None):
        self.condition_info_cid = TeaConverter.to_unicode(condition_info_cid)  # type: unicode
        self.oper_lambda = TeaConverter.to_unicode(oper_lambda)  # type: unicode
        self.operators = operators  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators
        self.check_range = check_range  # type: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange

    def validate(self):
        if self.operators:
            self.operators.validate()
        if self.check_range:
            self.check_range.validate()

    def to_map(self):
        result = dict()
        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid
        if self.oper_lambda is not None:
            result['OperLambda'] = self.oper_lambda
        if self.operators is not None:
            result['Operators'] = self.operators.to_map()
        if self.check_range is not None:
            result['CheckRange'] = self.check_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')
        if m.get('OperLambda') is not None:
            self.oper_lambda = m.get('OperLambda')
        if m.get('Operators') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators()
            self.operators = temp_model.from_map(m['Operators'])
        if m.get('CheckRange') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m['CheckRange'])
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


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers(TeaModel):
    def __init__(self, trigger=None):
        self.trigger = trigger  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo(TeaModel):
    def __init__(self, bid=None, service_type=None, business_name=None):
        self.bid = bid  # type: int
        self.service_type = service_type  # type: int
        self.business_name = TeaConverter.to_unicode(business_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
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


class GetRuleDetailResponseBodyDataRulesRuleBasicInfo(TeaModel):
    def __init__(self, rid=None, rule_lambda=None, triggers=None, business_categories=None):
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.rule_lambda = TeaConverter.to_unicode(rule_lambda)  # type: unicode
        self.triggers = triggers  # type: GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers
        self.business_categories = business_categories  # type: GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories

    def validate(self):
        if self.triggers:
            self.triggers.validate()
        if self.business_categories:
            self.business_categories.validate()

    def to_map(self):
        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda
        if self.triggers is not None:
            result['Triggers'] = self.triggers.to_map()
        if self.business_categories is not None:
            result['BusinessCategories'] = self.business_categories.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('Triggers') is not None:
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers()
            self.triggers = temp_model.from_map(m['Triggers'])
        if m.get('BusinessCategories') is not None:
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories()
            self.business_categories = temp_model.from_map(m['BusinessCategories'])
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
    def __init__(self, conditions=None, rules=None):
        self.conditions = conditions  # type: GetRuleDetailResponseBodyDataConditions
        self.rules = rules  # type: GetRuleDetailResponseBodyDataRules

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('Rules') is not None:
            temp_model = GetRuleDetailResponseBodyDataRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class GetRuleDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.data = data  # type: GetRuleDetailResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetRuleDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetRuleDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class GetRuleDimensionRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleDimensionResponseBodyDataRuleCountInfo(TeaModel):
    def __init__(self, status=None, type=None, pre_review_number=None, hit_number=None, select=None,
                 create_empid=None, create_time=None, last_update_empid=None, real_violation_number=None, is_delete=None,
                 hit_rate=None, rid=None, check_number=None, type_name=None, last_update_time=None, name=None,
                 hit_real_violation_rate=None, review_number=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.pre_review_number = pre_review_number  # type: int
        self.hit_number = hit_number  # type: int
        self.select = select  # type: bool
        self.create_empid = TeaConverter.to_unicode(create_empid)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.last_update_empid = TeaConverter.to_unicode(last_update_empid)  # type: unicode
        self.real_violation_number = real_violation_number  # type: int
        self.is_delete = is_delete  # type: int
        self.hit_rate = hit_rate  # type: float
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.check_number = check_number  # type: int
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode
        self.last_update_time = TeaConverter.to_unicode(last_update_time)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.hit_real_violation_rate = hit_real_violation_rate  # type: float
        self.review_number = review_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.pre_review_number is not None:
            result['PreReviewNumber'] = self.pre_review_number
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.select is not None:
            result['Select'] = self.select
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.real_violation_number is not None:
            result['RealViolationNumber'] = self.real_violation_number
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.hit_rate is not None:
            result['HitRate'] = self.hit_rate
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.hit_real_violation_rate is not None:
            result['HitRealViolationRate'] = self.hit_real_violation_rate
        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PreReviewNumber') is not None:
            self.pre_review_number = m.get('PreReviewNumber')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('RealViolationNumber') is not None:
            self.real_violation_number = m.get('RealViolationNumber')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('HitRate') is not None:
            self.hit_rate = m.get('HitRate')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('HitRealViolationRate') is not None:
            self.hit_real_violation_rate = m.get('HitRealViolationRate')
        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')
        return self


class GetRuleDimensionResponseBodyData(TeaModel):
    def __init__(self, rule_count_info=None):
        self.rule_count_info = rule_count_info  # type: list[GetRuleDimensionResponseBodyDataRuleCountInfo]

    def validate(self):
        if self.rule_count_info:
            for k in self.rule_count_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetRuleDimensionResponseBodyDataRuleCountInfo()
                self.rule_count_info.append(temp_model.from_map(k))
        return self


class GetRuleDimensionResponseBody(TeaModel):
    def __init__(self, comp_sub_task_count=None, total_count=None, request_id=None, message=None, page_size=None,
                 current_page=None, review_status=None, data_size=None, data=None, code=None, success=None,
                 total_sub_task_count=None):
        self.comp_sub_task_count = comp_sub_task_count  # type: int
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.review_status = review_status  # type: int
        self.data_size = data_size  # type: int
        self.data = data  # type: GetRuleDimensionResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool
        self.total_sub_task_count = total_sub_task_count  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.comp_sub_task_count is not None:
            result['CompSubTaskCount'] = self.comp_sub_task_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.total_sub_task_count is not None:
            result['TotalSubTaskCount'] = self.total_sub_task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompSubTaskCount') is not None:
            self.comp_sub_task_count = m.get('CompSubTaskCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Data') is not None:
            temp_model = GetRuleDimensionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSubTaskCount') is not None:
            self.total_sub_task_count = m.get('TotalSubTaskCount')
        return self


class GetRuleDimensionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetRuleDimensionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetRuleDimensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScoreInfoRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam(TeaModel):
    def __init__(self, score_sub_name=None, score_num=None, score_sub_id=None, score_type=None):
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: int
        self.score_type = score_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
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
    def __init__(self, score_infos=None, score_name=None, score_id=None):
        self.score_infos = score_infos  # type: GetScoreInfoResponseBodyDataScorePoScoreInfos
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.score_id = score_id  # type: int

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        result = dict()
        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreInfos') is not None:
            temp_model = GetScoreInfoResponseBodyDataScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m['ScoreInfos'])
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetScoreInfoResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetScoreInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScoreInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetScoreInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo(TeaModel):
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, status=None, type=None, all_rule_list=None, update_time=None, all_content_quality_check=None,
                 create_time=None, skill_group_id=None, instance_id=None, vocab_id=None, skill_group_from=None, rid=None,
                 skill_group_name=None, rule_list=None, model_name=None, all_rids=None, name=None, model_id=None, id=None,
                 quality_check_type=None, vocab_name=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.all_rule_list = all_rule_list  # type: GetSkillGroupConfigResponseBodyDataAllRuleList
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.all_content_quality_check = all_content_quality_check  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.skill_group_id = TeaConverter.to_unicode(skill_group_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.vocab_id = vocab_id  # type: long
        self.skill_group_from = skill_group_from  # type: int
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.skill_group_name = TeaConverter.to_unicode(skill_group_name)  # type: unicode
        self.rule_list = rule_list  # type: GetSkillGroupConfigResponseBodyDataRuleList
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.all_rids = TeaConverter.to_unicode(all_rids)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.model_id = model_id  # type: long
        self.id = id  # type: long
        self.quality_check_type = quality_check_type  # type: int
        self.vocab_name = TeaConverter.to_unicode(vocab_name)  # type: unicode

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.name is not None:
            result['Name'] = self.name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.id is not None:
            result['Id'] = self.id
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AllRuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('RuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class GetSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetSkillGroupConfigResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, name=None, skill_group=None, id=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.skill_group = TeaConverter.to_unicode(skill_group)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetSyncResultResponseBodyDataAsrResult(TeaModel):
    def __init__(self, words=None, begin=None, emotion_value=None, end=None, speech_rate=None, role=None,
                 silence_duration=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class GetSyncResultResponseBodyDataHitResultHitsPhrase(TeaModel):
    def __init__(self, words=None, begin=None, emotion_value=None, end=None, speech_rate=None, role=None,
                 silence_duration=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: int
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class GetSyncResultResponseBodyDataHitResultHitsKeyWords(TeaModel):
    def __init__(self, from_=None, val=None, cid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.cid = TeaConverter.to_unicode(cid)  # type: unicode
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetSyncResultResponseBodyDataHitResultHits(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: GetSyncResultResponseBodyDataHitResultHitsPhrase
        self.key_words = key_words  # type: list[GetSyncResultResponseBodyDataHitResultHitsKeyWords]
        self.cid = cid  # type: list[unicode]

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            for k in self.key_words:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        result['KeyWords'] = []
        if self.key_words is not None:
            for k in self.key_words:
                result['KeyWords'].append(k.to_map() if k else None)
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = GetSyncResultResponseBodyDataHitResultHitsPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        self.key_words = []
        if m.get('KeyWords') is not None:
            for k in m.get('KeyWords'):
                temp_model = GetSyncResultResponseBodyDataHitResultHitsKeyWords()
                self.key_words.append(temp_model.from_map(k))
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetSyncResultResponseBodyDataHitResult(TeaModel):
    def __init__(self, type=None, hits=None, review_result=None, name=None, rid=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.hits = hits  # type: list[GetSyncResultResponseBodyDataHitResultHits]
        self.review_result = review_result  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['Hits'] = []
        if self.hits is not None:
            for k in self.hits:
                result['Hits'].append(k.to_map() if k else None)
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.hits = []
        if m.get('Hits') is not None:
            for k in m.get('Hits'):
                temp_model = GetSyncResultResponseBodyDataHitResultHits()
                self.hits.append(temp_model.from_map(k))
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetSyncResultResponseBodyDataRecording(TeaModel):
    def __init__(self, callee=None, business=None, remark_3=None, url=None, primary_id=None, remark_1=None,
                 call_type=None, remark_2=None, caller=None, call_id=None, duration=None, data_set_name=None, name=None,
                 id=None, call_time=None):
        self.callee = TeaConverter.to_unicode(callee)  # type: unicode
        self.business = TeaConverter.to_unicode(business)  # type: unicode
        self.remark_3 = TeaConverter.to_unicode(remark_3)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.primary_id = TeaConverter.to_unicode(primary_id)  # type: unicode
        self.remark_1 = TeaConverter.to_unicode(remark_1)  # type: unicode
        self.call_type = call_type  # type: int
        self.remark_2 = TeaConverter.to_unicode(remark_2)  # type: unicode
        self.caller = TeaConverter.to_unicode(caller)  # type: unicode
        self.call_id = TeaConverter.to_unicode(call_id)  # type: unicode
        self.duration = duration  # type: long
        self.data_set_name = TeaConverter.to_unicode(data_set_name)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode
        self.call_time = TeaConverter.to_unicode(call_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.business is not None:
            result['Business'] = self.business
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.url is not None:
            result['Url'] = self.url
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class GetSyncResultResponseBodyData(TeaModel):
    def __init__(self, status=None, error_message=None, reviewer=None, create_time=None, review_status=None,
                 task_name=None, review_result=None, score=None, agent=None, asr_result=None, hit_result=None, comments=None,
                 recording=None, task_id=None, resolver=None):
        self.status = status  # type: int
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.reviewer = TeaConverter.to_unicode(reviewer)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.review_status = review_status  # type: int
        self.task_name = TeaConverter.to_unicode(task_name)  # type: unicode
        self.review_result = review_result  # type: int
        self.score = score  # type: int
        self.agent = agent  # type: GetSyncResultResponseBodyDataAgent
        self.asr_result = asr_result  # type: list[GetSyncResultResponseBodyDataAsrResult]
        self.hit_result = hit_result  # type: list[GetSyncResultResponseBodyDataHitResult]
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.recording = recording  # type: GetSyncResultResponseBodyDataRecording
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.resolver = TeaConverter.to_unicode(resolver)  # type: unicode

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
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.score is not None:
            result['Score'] = self.score
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['AsrResult'].append(k.to_map() if k else None)
        result['HitResult'] = []
        if self.hit_result is not None:
            for k in self.hit_result:
                result['HitResult'].append(k.to_map() if k else None)
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Agent') is not None:
            temp_model = GetSyncResultResponseBodyDataAgent()
            self.agent = temp_model.from_map(m['Agent'])
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k in m.get('AsrResult'):
                temp_model = GetSyncResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k in m.get('HitResult'):
                temp_model = GetSyncResultResponseBodyDataHitResult()
                self.hit_result.append(temp_model.from_map(k))
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Recording') is not None:
            temp_model = GetSyncResultResponseBodyDataRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
        return self


class GetSyncResultResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None, result_count_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[GetSyncResultResponseBodyData]
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool
        self.result_count_id = TeaConverter.to_unicode(result_count_id)  # type: unicode

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSyncResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        return self


class GetSyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetSyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class GetTaskFileResultListRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetTaskFileResultListResponseBodyDataTaskResultReviewInfoHitRuleSet(TeaModel):
    def __init__(self, hit_rule_set=None):
        self.hit_rule_set = hit_rule_set  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hit_rule_set is not None:
            result['HitRuleSet'] = self.hit_rule_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitRuleSet') is not None:
            self.hit_rule_set = m.get('HitRuleSet')
        return self


class GetTaskFileResultListResponseBodyDataTaskResultReviewInfo(TeaModel):
    def __init__(self, status=None, hit_number=None, data_type=None, next_vid=None, hit_rule=None, pre_vid=None,
                 is_hit_rule=None, real_violation_number=None, review_accuracy_rate=None, file_name=None, total_score=None,
                 check_number=None, file_merge_name=None, bucket_name=None, hand_task_file=None, hit_rule_set=None, task_id=None,
                 vid=None):
        self.status = status  # type: int
        self.hit_number = hit_number  # type: int
        self.data_type = data_type  # type: int
        self.next_vid = TeaConverter.to_unicode(next_vid)  # type: unicode
        self.hit_rule = hit_rule  # type: bool
        self.pre_vid = TeaConverter.to_unicode(pre_vid)  # type: unicode
        self.is_hit_rule = is_hit_rule  # type: bool
        self.real_violation_number = real_violation_number  # type: int
        self.review_accuracy_rate = review_accuracy_rate  # type: float
        self.file_name = TeaConverter.to_unicode(file_name)  # type: unicode
        self.total_score = total_score  # type: int
        self.check_number = check_number  # type: int
        self.file_merge_name = TeaConverter.to_unicode(file_merge_name)  # type: unicode
        self.bucket_name = TeaConverter.to_unicode(bucket_name)  # type: unicode
        self.hand_task_file = hand_task_file  # type: bool
        self.hit_rule_set = hit_rule_set  # type: GetTaskFileResultListResponseBodyDataTaskResultReviewInfoHitRuleSet
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.vid = TeaConverter.to_unicode(vid)  # type: unicode

    def validate(self):
        if self.hit_rule_set:
            self.hit_rule_set.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.next_vid is not None:
            result['NextVid'] = self.next_vid
        if self.hit_rule is not None:
            result['HitRule'] = self.hit_rule
        if self.pre_vid is not None:
            result['PreVid'] = self.pre_vid
        if self.is_hit_rule is not None:
            result['IsHitRule'] = self.is_hit_rule
        if self.real_violation_number is not None:
            result['RealViolationNumber'] = self.real_violation_number
        if self.review_accuracy_rate is not None:
            result['ReviewAccuracyRate'] = self.review_accuracy_rate
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.hand_task_file is not None:
            result['HandTaskFile'] = self.hand_task_file
        if self.hit_rule_set is not None:
            result['HitRuleSet'] = self.hit_rule_set.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('NextVid') is not None:
            self.next_vid = m.get('NextVid')
        if m.get('HitRule') is not None:
            self.hit_rule = m.get('HitRule')
        if m.get('PreVid') is not None:
            self.pre_vid = m.get('PreVid')
        if m.get('IsHitRule') is not None:
            self.is_hit_rule = m.get('IsHitRule')
        if m.get('RealViolationNumber') is not None:
            self.real_violation_number = m.get('RealViolationNumber')
        if m.get('ReviewAccuracyRate') is not None:
            self.review_accuracy_rate = m.get('ReviewAccuracyRate')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('HandTaskFile') is not None:
            self.hand_task_file = m.get('HandTaskFile')
        if m.get('HitRuleSet') is not None:
            temp_model = GetTaskFileResultListResponseBodyDataTaskResultReviewInfoHitRuleSet()
            self.hit_rule_set = temp_model.from_map(m['HitRuleSet'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetTaskFileResultListResponseBodyData(TeaModel):
    def __init__(self, task_result_review_info=None):
        self.task_result_review_info = task_result_review_info  # type: list[GetTaskFileResultListResponseBodyDataTaskResultReviewInfo]

    def validate(self):
        if self.task_result_review_info:
            for k in self.task_result_review_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TaskResultReviewInfo'] = []
        if self.task_result_review_info is not None:
            for k in self.task_result_review_info:
                result['TaskResultReviewInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_result_review_info = []
        if m.get('TaskResultReviewInfo') is not None:
            for k in m.get('TaskResultReviewInfo'):
                temp_model = GetTaskFileResultListResponseBodyDataTaskResultReviewInfo()
                self.task_result_review_info.append(temp_model.from_map(k))
        return self


class GetTaskFileResultListResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, message=None, page_size=None, data_size=None, data=None,
                 code=None, success=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.data_size = data_size  # type: int
        self.data = data  # type: GetTaskFileResultListResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Data') is not None:
            temp_model = GetTaskFileResultListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTaskFileResultListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTaskFileResultListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetTaskFileResultListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRuleListRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetTaskRuleListResponseBodyDataRuleCountInfo(TeaModel):
    def __init__(self, status=None, type=None, pre_review_number=None, hit_number=None, select=None,
                 create_empid=None, create_time=None, last_update_empid=None, real_violation_number=None, is_delete=None,
                 hit_rate=None, rid=None, check_number=None, type_name=None, last_update_time=None, name=None,
                 hit_real_violation_rate=None, review_number=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.pre_review_number = pre_review_number  # type: int
        self.hit_number = hit_number  # type: int
        self.select = select  # type: bool
        self.create_empid = TeaConverter.to_unicode(create_empid)  # type: unicode
        self.create_time = create_time  # type: long
        self.last_update_empid = TeaConverter.to_unicode(last_update_empid)  # type: unicode
        self.real_violation_number = real_violation_number  # type: int
        self.is_delete = is_delete  # type: int
        self.hit_rate = hit_rate  # type: float
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.check_number = check_number  # type: int
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode
        self.last_update_time = last_update_time  # type: long
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.hit_real_violation_rate = hit_real_violation_rate  # type: float
        self.review_number = review_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.pre_review_number is not None:
            result['PreReviewNumber'] = self.pre_review_number
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.select is not None:
            result['Select'] = self.select
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.real_violation_number is not None:
            result['RealViolationNumber'] = self.real_violation_number
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.hit_rate is not None:
            result['HitRate'] = self.hit_rate
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.hit_real_violation_rate is not None:
            result['HitRealViolationRate'] = self.hit_real_violation_rate
        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PreReviewNumber') is not None:
            self.pre_review_number = m.get('PreReviewNumber')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('RealViolationNumber') is not None:
            self.real_violation_number = m.get('RealViolationNumber')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('HitRate') is not None:
            self.hit_rate = m.get('HitRate')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('HitRealViolationRate') is not None:
            self.hit_real_violation_rate = m.get('HitRealViolationRate')
        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')
        return self


class GetTaskRuleListResponseBodyData(TeaModel):
    def __init__(self, rule_count_info=None):
        self.rule_count_info = rule_count_info  # type: list[GetTaskRuleListResponseBodyDataRuleCountInfo]

    def validate(self):
        if self.rule_count_info:
            for k in self.rule_count_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = GetTaskRuleListResponseBodyDataRuleCountInfo()
                self.rule_count_info.append(temp_model.from_map(k))
        return self


class GetTaskRuleListResponseBody(TeaModel):
    def __init__(self, comp_sub_task_count=None, total_count=None, request_id=None, message=None, page_size=None,
                 current_page=None, review_status=None, data_size=None, data=None, code=None, success=None,
                 total_sub_task_count=None):
        self.comp_sub_task_count = comp_sub_task_count  # type: int
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.review_status = review_status  # type: int
        self.data_size = data_size  # type: int
        self.data = data  # type: GetTaskRuleListResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool
        self.total_sub_task_count = total_sub_task_count  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.comp_sub_task_count is not None:
            result['CompSubTaskCount'] = self.comp_sub_task_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.total_sub_task_count is not None:
            result['TotalSubTaskCount'] = self.total_sub_task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompSubTaskCount') is not None:
            self.comp_sub_task_count = m.get('CompSubTaskCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Data') is not None:
            temp_model = GetTaskRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSubTaskCount') is not None:
            self.total_sub_task_count = m.get('TotalSubTaskCount')
        return self


class GetTaskRuleListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTaskRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetTaskRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThesaurusBySynonymForApiRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList(TeaModel):
    def __init__(self, synonym_list=None):
        self.synonym_list = synonym_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, business=None, synonym_list=None, id=None):
        self.business = TeaConverter.to_unicode(business)  # type: unicode
        self.synonym_list = synonym_list  # type: GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList
        self.id = id  # type: long

    def validate(self):
        if self.synonym_list:
            self.synonym_list.validate()

    def to_map(self):
        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.synonym_list is not None:
            result['SynonymList'] = self.synonym_list.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('SynonymList') is not None:
            temp_model = GetThesaurusBySynonymForApiResponseBodyDataThesaurusPoSynonymList()
            self.synonym_list = temp_model.from_map(m['SynonymList'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetThesaurusBySynonymForApiResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetThesaurusBySynonymForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetThesaurusBySynonymForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetThesaurusBySynonymForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class HandleComplaintResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HandleComplaintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: HandleComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InsertScoreForApiResponseBodyData(TeaModel):
    def __init__(self, score_name=None, score_id=None):
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.score_id = score_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        return self


class InsertScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: InsertScoreForApiResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = InsertScoreForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: InsertScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InsertSubScoreForApiResponseBodyData(TeaModel):
    def __init__(self, score_sub_name=None, score_sub_id=None):
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_sub_id = score_sub_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        return self


class InsertSubScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: InsertSubScoreForApiResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = InsertSubScoreForApiResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: InsertSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InvalidRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: bool
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvalidRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: InvalidRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListAsrVocabResponseBodyDataAsrVocab(TeaModel):
    def __init__(self, vocabulary_id=None, update_time=None, create_time=None, name=None, id=None):
        self.vocabulary_id = TeaConverter.to_unicode(vocabulary_id)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ListAsrVocabResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ListDataSetTaskRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoListRuleNameInfo(TeaModel):
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoList(TeaModel):
    def __init__(self, rule_name_info=None):
        self.rule_name_info = rule_name_info  # type: list[ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoListRuleNameInfo]

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class ListDataSetTaskResponseBodyDataPageTaskInfoDataSets(TeaModel):
    def __init__(self, data_sets=None):
        self.data_sets = data_sets  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_sets is not None:
            result['dataSets'] = self.data_sets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSets') is not None:
            self.data_sets = m.get('dataSets')
        return self


class ListDataSetTaskResponseBodyDataPageTaskInfo(TeaModel):
    def __init__(self, status=None, is_task_complete=None, rule_name_info_list=None, schedule_ratio=None,
                 task_complete=None, data_sets=None, data_set_size=None, rule_size=None, job_name=None, task_id=None):
        self.status = status  # type: int
        self.is_task_complete = is_task_complete  # type: bool
        self.rule_name_info_list = rule_name_info_list  # type: ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoList
        self.schedule_ratio = schedule_ratio  # type: float
        self.task_complete = task_complete  # type: bool
        self.data_sets = data_sets  # type: ListDataSetTaskResponseBodyDataPageTaskInfoDataSets
        self.data_set_size = data_set_size  # type: int
        self.rule_size = rule_size  # type: int
        self.job_name = TeaConverter.to_unicode(job_name)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        if self.rule_name_info_list:
            self.rule_name_info_list.validate()
        if self.data_sets:
            self.data_sets.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.is_task_complete is not None:
            result['IsTaskComplete'] = self.is_task_complete
        if self.rule_name_info_list is not None:
            result['RuleNameInfoList'] = self.rule_name_info_list.to_map()
        if self.schedule_ratio is not None:
            result['ScheduleRatio'] = self.schedule_ratio
        if self.task_complete is not None:
            result['TaskComplete'] = self.task_complete
        if self.data_sets is not None:
            result['DataSets'] = self.data_sets.to_map()
        if self.data_set_size is not None:
            result['DataSetSize'] = self.data_set_size
        if self.rule_size is not None:
            result['RuleSize'] = self.rule_size
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsTaskComplete') is not None:
            self.is_task_complete = m.get('IsTaskComplete')
        if m.get('RuleNameInfoList') is not None:
            temp_model = ListDataSetTaskResponseBodyDataPageTaskInfoRuleNameInfoList()
            self.rule_name_info_list = temp_model.from_map(m['RuleNameInfoList'])
        if m.get('ScheduleRatio') is not None:
            self.schedule_ratio = m.get('ScheduleRatio')
        if m.get('TaskComplete') is not None:
            self.task_complete = m.get('TaskComplete')
        if m.get('DataSets') is not None:
            temp_model = ListDataSetTaskResponseBodyDataPageTaskInfoDataSets()
            self.data_sets = temp_model.from_map(m['DataSets'])
        if m.get('DataSetSize') is not None:
            self.data_set_size = m.get('DataSetSize')
        if m.get('RuleSize') is not None:
            self.rule_size = m.get('RuleSize')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListDataSetTaskResponseBodyData(TeaModel):
    def __init__(self, page_task_info=None):
        self.page_task_info = page_task_info  # type: list[ListDataSetTaskResponseBodyDataPageTaskInfo]

    def validate(self):
        if self.page_task_info:
            for k in self.page_task_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PageTaskInfo'] = []
        if self.page_task_info is not None:
            for k in self.page_task_info:
                result['PageTaskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_task_info = []
        if m.get('PageTaskInfo') is not None:
            for k in m.get('PageTaskInfo'):
                temp_model = ListDataSetTaskResponseBodyDataPageTaskInfo()
                self.page_task_info.append(temp_model.from_map(k))
        return self


class ListDataSetTaskResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, message=None, page_size=None, current_page=None,
                 data_size=None, data=None, is_allcomplete=None, code=None, success=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.data_size = data_size  # type: int
        self.data = data  # type: ListDataSetTaskResponseBodyData
        self.is_allcomplete = is_allcomplete  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.is_allcomplete is not None:
            result['IsAllcomplete'] = self.is_allcomplete
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Data') is not None:
            temp_model = ListDataSetTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('IsAllcomplete') is not None:
            self.is_allcomplete = m.get('IsAllcomplete')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSetTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListDataSetTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListDataSetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotWordsTasksRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam(TeaModel):
    def __init__(self, excludes=None, includes=None, extra_config_id=None):
        self.excludes = TeaConverter.to_unicode(excludes)  # type: unicode
        self.includes = TeaConverter.to_unicode(includes)  # type: unicode
        self.extra_config_id = extra_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes
        if self.includes is not None:
            result['Includes'] = self.includes
        if self.extra_config_id is not None:
            result['ExtraConfigId'] = self.extra_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')
        if m.get('Includes') is not None:
            self.includes = m.get('Includes')
        if m.get('ExtraConfigId') is not None:
            self.extra_config_id = m.get('ExtraConfigId')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam(TeaModel):
    def __init__(self, end_time=None, dialogue_id=None, end_index=None, start_time=None, source_type=None,
                 start_index=None, role=None, data_set_ids=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dialogue_id = dialogue_id  # type: long
        self.end_index = end_index  # type: int
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.source_type = source_type  # type: int
        self.start_index = start_index  # type: int
        self.role = role  # type: int
        self.data_set_ids = TeaConverter.to_unicode(data_set_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        if self.role is not None:
            result['Role'] = self.role
        if self.data_set_ids is not None:
            result['DataSetIds'] = self.data_set_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('DataSetIds') is not None:
            self.data_set_ids = m.get('DataSetIds')
        return self


class ListHotWordsTasksResponseBodyDataHotWordsTaskPo(TeaModel):
    def __init__(self, type=None, status=None, task_config_id=None, message=None, last_execution_time=None,
                 time_unit=None, words_param=None, end_time=None, time_interval=None, start_time=None, instance_status=None,
                 name=None, dialogue_param=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.task_config_id = task_config_id  # type: long
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.last_execution_time = TeaConverter.to_unicode(last_execution_time)  # type: unicode
        self.time_unit = time_unit  # type: int
        self.words_param = words_param  # type: ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.time_interval = time_interval  # type: int
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.instance_status = instance_status  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.dialogue_param = dialogue_param  # type: ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam

    def validate(self):
        if self.words_param:
            self.words_param.validate()
        if self.dialogue_param:
            self.dialogue_param.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id
        if self.message is not None:
            result['Message'] = self.message
        if self.last_execution_time is not None:
            result['LastExecutionTime'] = self.last_execution_time
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.words_param is not None:
            result['WordsParam'] = self.words_param.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.name is not None:
            result['Name'] = self.name
        if self.dialogue_param is not None:
            result['DialogueParam'] = self.dialogue_param.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LastExecutionTime') is not None:
            self.last_execution_time = m.get('LastExecutionTime')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('WordsParam') is not None:
            temp_model = ListHotWordsTasksResponseBodyDataHotWordsTaskPoWordsParam()
            self.words_param = temp_model.from_map(m['WordsParam'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DialogueParam') is not None:
            temp_model = ListHotWordsTasksResponseBodyDataHotWordsTaskPoDialogueParam()
            self.dialogue_param = temp_model.from_map(m['DialogueParam'])
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: ListHotWordsTasksResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = ListHotWordsTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotWordsTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListHotWordsTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision(TeaModel):
    def __init__(self, status=None, create_time=None, model_name=None, task_id=None, model_id=None, precision=None):
        self.status = status  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.model_id = model_id  # type: long
        self.precision = precision  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.precision is not None:
            result['Precision'] = self.precision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
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
    def __init__(self, status=None, update_time=None, create_time=None, incorrect_words=None, data_set_id=None,
                 verified_count=None, total_count=None, source=None, precisions=None, duration=None, data_set_name=None, name=None,
                 task_id=None):
        self.status = status  # type: int
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.incorrect_words = incorrect_words  # type: int
        self.data_set_id = data_set_id  # type: long
        self.verified_count = verified_count  # type: int
        self.total_count = total_count  # type: int
        self.source = source  # type: int
        self.precisions = precisions  # type: ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions
        self.duration = duration  # type: int
        self.data_set_name = TeaConverter.to_unicode(data_set_name)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.source is not None:
            result['Source'] = self.source
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.name is not None:
            result['Name'] = self.name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Precisions') is not None:
            temp_model = ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: ListPrecisionTaskResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = ListPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListRolesResponseBodyDataRole(TeaModel):
    def __init__(self, display_name=None, update_time=None, create_time=None, name=None, id=None, level=None):
        self.display_name = TeaConverter.to_unicode(display_name)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.id = id  # type: long
        self.level = level  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ListRolesResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListRolesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRolesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(self, type=None, rule_type=None, business_category_name_list=None, create_time=None, comments=None,
                 type_name=None, name=None, rid=None):
        self.type = type  # type: int
        self.rule_type = rule_type  # type: int
        self.business_category_name_list = business_category_name_list  # type: list[unicode]
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListRulesResponseBodyData]
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo(TeaModel):
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, value=None, data_type=None, symbol=None, name=None):
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.data_type = data_type  # type: int
        self.symbol = symbol  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, status=None, type=None, all_rule_list=None, update_time=None, all_content_quality_check=None,
                 create_time=None, skill_group_id=None, screen_switch=None, instance_id=None, vocab_id=None,
                 skill_group_from=None, rid=None, skill_group_name=None, rule_list=None, model_name=None, all_rids=None, name=None,
                 model_id=None, id=None, skill_group_screens=None, quality_check_type=None, vocab_name=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.all_rule_list = all_rule_list  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.all_content_quality_check = all_content_quality_check  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.skill_group_id = TeaConverter.to_unicode(skill_group_id)  # type: unicode
        self.screen_switch = screen_switch  # type: bool
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.vocab_id = vocab_id  # type: long
        self.skill_group_from = skill_group_from  # type: int
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode
        self.skill_group_name = TeaConverter.to_unicode(skill_group_name)  # type: unicode
        self.rule_list = rule_list  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.all_rids = TeaConverter.to_unicode(all_rids)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.model_id = model_id  # type: long
        self.id = id  # type: long
        self.skill_group_screens = skill_group_screens  # type: ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens
        self.quality_check_type = quality_check_type  # type: int
        self.vocab_name = TeaConverter.to_unicode(vocab_name)  # type: unicode

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()
        if self.skill_group_screens:
            self.skill_group_screens.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.screen_switch is not None:
            result['ScreenSwitch'] = self.screen_switch
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.name is not None:
            result['Name'] = self.name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.id is not None:
            result['Id'] = self.id
        if self.skill_group_screens is not None:
            result['SkillGroupScreens'] = self.skill_group_screens.to_map()
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AllRuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('ScreenSwitch') is not None:
            self.screen_switch = m.get('ScreenSwitch')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('RuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SkillGroupScreens') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens()
            self.skill_group_screens = temp_model.from_map(m['SkillGroupScreens'])
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ListSkillGroupConfigResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo(TeaModel):
    def __init__(self, name=None, rid=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup(TeaModel):
    def __init__(self, skill_id=None, skill_name=None):
        self.skill_id = TeaConverter.to_unicode(skill_id)  # type: unicode
        self.skill_name = TeaConverter.to_unicode(skill_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent(TeaModel):
    def __init__(self, agent_id=None, agent_name=None):
        self.agent_id = TeaConverter.to_unicode(agent_id)  # type: unicode
        self.agent_name = TeaConverter.to_unicode(agent_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, reviewer_name=None, reviewer_id=None):
        self.reviewer_name = TeaConverter.to_unicode(reviewer_name)  # type: unicode
        self.reviewer_id = TeaConverter.to_unicode(reviewer_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reviewer_name is not None:
            result['ReviewerName'] = self.reviewer_name
        if self.reviewer_id is not None:
            result['ReviewerId'] = self.reviewer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewerName') is not None:
            self.reviewer_name = m.get('ReviewerName')
        if m.get('ReviewerId') is not None:
            self.reviewer_id = m.get('ReviewerId')
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


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo(TeaModel):
    def __init__(self, skill_groups_str=None, update_time=None, duration_max=None, create_time=None, priority=None,
                 agents_str=None, duration_min=None, rules=None, rule_id=None, skill_groups=None, agents=None, call_type=None,
                 enabled=None, reviewers=None):
        self.skill_groups_str = TeaConverter.to_unicode(skill_groups_str)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.duration_max = duration_max  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.priority = priority  # type: int
        self.agents_str = TeaConverter.to_unicode(agents_str)  # type: unicode
        self.duration_min = duration_min  # type: int
        self.rules = rules  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules
        self.rule_id = rule_id  # type: long
        self.skill_groups = skill_groups  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups
        self.agents = agents  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents
        self.call_type = call_type  # type: int
        self.enabled = enabled  # type: int
        self.reviewers = reviewers  # type: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers

    def validate(self):
        if self.rules:
            self.rules.validate()
        if self.skill_groups:
            self.skill_groups.validate()
        if self.agents:
            self.agents.validate()
        if self.reviewers:
            self.reviewers.validate()

    def to_map(self):
        result = dict()
        if self.skill_groups_str is not None:
            result['SkillGroupsStr'] = self.skill_groups_str
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.duration_max is not None:
            result['DurationMax'] = self.duration_max
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.agents_str is not None:
            result['AgentsStr'] = self.agents_str
        if self.duration_min is not None:
            result['DurationMin'] = self.duration_min
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.skill_groups is not None:
            result['SkillGroups'] = self.skill_groups.to_map()
        if self.agents is not None:
            result['Agents'] = self.agents.to_map()
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SkillGroupsStr') is not None:
            self.skill_groups_str = m.get('SkillGroupsStr')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DurationMax') is not None:
            self.duration_max = m.get('DurationMax')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('AgentsStr') is not None:
            self.agents_str = m.get('AgentsStr')
        if m.get('DurationMin') is not None:
            self.duration_min = m.get('DurationMin')
        if m.get('Rules') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SkillGroups') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups()
            self.skill_groups = temp_model.from_map(m['SkillGroups'])
        if m.get('Agents') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents()
            self.agents = temp_model.from_map(m['Agents'])
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Reviewers') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers()
            self.reviewers = temp_model.from_map(m['Reviewers'])
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: ListTaskAssignRulesResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = ListTaskAssignRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTaskAssignRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTaskAssignRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListUsersResponseBodyDataUser(TeaModel):
    def __init__(self, display_name=None, update_time=None, description=None, create_time=None,
                 login_user_type=None, ali_uid=None, role_name=None, user_name=None, id=None):
        self.display_name = TeaConverter.to_unicode(display_name)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.login_user_type = login_user_type  # type: int
        self.ali_uid = TeaConverter.to_unicode(ali_uid)  # type: unicode
        self.role_name = TeaConverter.to_unicode(role_name)  # type: unicode
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.login_user_type is not None:
            result['LoginUserType'] = self.login_user_type
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LoginUserType') is not None:
            self.login_user_type = m.get('LoginUserType')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
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
    def __init__(self, request_id=None, message=None, page_size=None, page_number=None, data=None, count=None,
                 code=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: ListUsersResponseBodyData
        self.count = count  # type: int
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRidList(TeaModel):
    def __init__(self, rid_list=None):
        self.rid_list = rid_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rid_list is not None:
            result['RidList'] = self.rid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RidList') is not None:
            self.rid_list = m.get('RidList')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel(TeaModel):
    def __init__(self, type=None, url=None):
        self.type = type  # type: int
        self.url = TeaConverter.to_unicode(url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule(TeaModel):
    def __init__(self, rule_name=None, rid=None):
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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
    def __init__(self, status=None, config_name=None, update_time=None, config_id=None, rid_list=None,
                 create_time=None, channels=None, rule_list=None):
        self.status = status  # type: int
        self.config_name = TeaConverter.to_unicode(config_name)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.config_id = config_id  # type: long
        self.rid_list = rid_list  # type: ListWarningConfigResponseBodyDataWarningConfigInfoRidList
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.channels = channels  # type: ListWarningConfigResponseBodyDataWarningConfigInfoChannels
        self.rule_list = rule_list  # type: ListWarningConfigResponseBodyDataWarningConfigInfoRuleList

    def validate(self):
        if self.rid_list:
            self.rid_list.validate()
        if self.channels:
            self.channels.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.rid_list is not None:
            result['RidList'] = self.rid_list.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('RidList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRidList()
            self.rid_list = temp_model.from_map(m['RidList'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Channels') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('RuleList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ListWarningConfigResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListWarningConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class RemoveAndGetTaskRulesRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class RemoveAndGetTaskRulesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveAndGetTaskRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RemoveAndGetTaskRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RemoveAndGetTaskRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartAsrTaskRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class RestartAsrTaskResponseBodyDataRestartResult(TeaModel):
    def __init__(self, data=None, success=None, message=None):
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.success = success  # type: bool
        self.message = TeaConverter.to_unicode(message)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: RestartAsrTaskResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = RestartAsrTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartAsrTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RestartAsrTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ReviewSingleResultByIdRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(self, words=None, begin=None, identity=None, pid=None, emotion_value=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.pid = pid  # type: int
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(self, from_=None, val=None, tid=None, pid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.pid = pid  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(TeaModel):
    def __init__(self, key_word=None):
        self.key_word = key_word  # type: list[ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord]

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase
        self.key_words = key_words  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords
        self.cid = cid  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            self.key_words.validate()
        if self.cid:
            self.cid.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('KeyWords') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Cid') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(TeaModel):
    def __init__(self, condition_hit_info=None):
        self.condition_hit_info = condition_hit_info  # type: list[ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo]

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo(TeaModel):
    def __init__(self, hit_id=None, rid=None):
        self.hit_id = TeaConverter.to_unicode(hit_id)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hit_id is not None:
            result['HitId'] = self.hit_id
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(self, rule_score_type=None, condition_hit_info_list=None, rule_type=None, auto_review=None,
                 score_sub_id=None, comments=None, review_info=None, total_number=None, score_id=None, rule_name=None, rid=None):
        self.rule_score_type = rule_score_type  # type: int
        self.condition_hit_info_list = condition_hit_info_list  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList
        self.rule_type = rule_type  # type: int
        self.auto_review = auto_review  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.comments = TeaConverter.to_unicode(comments)  # type: unicode
        self.review_info = review_info  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo
        self.total_number = total_number  # type: int
        self.score_id = score_id  # type: long
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = rid  # type: long

    def validate(self):
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()

    def to_map(self):
        result = dict()
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('ConditionHitInfoList') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ReviewInfo') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m['ReviewInfo'])
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(self, hit_rule_review_info=None):
        self.hit_rule_review_info = hit_rule_review_info  # type: list[ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo]

    def validate(self):
        if self.hit_rule_review_info:
            for k in self.hit_rule_review_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyDataManualScoreMappingList(TeaModel):
    def __init__(self, manual_score_mapping_list=None):
        self.manual_score_mapping_list = manual_score_mapping_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.manual_score_mapping_list is not None:
            result['ManualScoreMappingList'] = self.manual_score_mapping_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ManualScoreMappingList') is not None:
            self.manual_score_mapping_list = m.get('ManualScoreMappingList')
        return self


class ReviewSingleResultByIdResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(self, words=None, identity=None, begin=None, begin_time=None, emotion_value=None, end=None,
                 speech_rate=None, role=None, silence_duration=None, hour_min_sec=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.begin = begin  # type: long
        self.begin_time = begin_time  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int
        self.hour_min_sec = TeaConverter.to_unicode(hour_min_sec)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        return self


class ReviewSingleResultByIdResponseBodyDataDialogues(TeaModel):
    def __init__(self, dialogue=None):
        self.dialogue = dialogue  # type: list[ReviewSingleResultByIdResponseBodyDataDialoguesDialogue]

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam(TeaModel):
    def __init__(self, score_sub_name=None, score_num=None, score_sub_id=None, score_type=None, hit=None):
        self.score_sub_name = TeaConverter.to_unicode(score_sub_name)  # type: unicode
        self.score_num = score_num  # type: int
        self.score_sub_id = score_sub_id  # type: long
        self.score_type = score_type  # type: int
        self.hit = hit  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.hit is not None:
            result['Hit'] = self.hit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        return self


class ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfos(TeaModel):
    def __init__(self, score_param=None):
        self.score_param = score_param  # type: list[ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam]

    def validate(self):
        if self.score_param:
            for k in self.score_param:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfosScoreParam()
                self.score_param.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePo(TeaModel):
    def __init__(self, score_infos=None, score_name=None, score_id=None):
        self.score_infos = score_infos  # type: ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfos
        self.score_name = TeaConverter.to_unicode(score_name)  # type: unicode
        self.score_id = score_id  # type: long

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        result = dict()
        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScoreInfos') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m['ScoreInfos'])
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        return self


class ReviewSingleResultByIdResponseBodyDataHandScoreInfoList(TeaModel):
    def __init__(self, score_po=None):
        self.score_po = score_po  # type: list[ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePo]

    def validate(self):
        if self.score_po:
            for k in self.score_po:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ReviewSingleResultByIdResponseBodyDataHandScoreInfoListScorePo()
                self.score_po.append(temp_model.from_map(k))
        return self


class ReviewSingleResultByIdResponseBodyData(TeaModel):
    def __init__(self, audio_url=None, hit_number=None, next_vid=None, pre_vid=None, is_audio=None,
                 hit_rule_review_info_list=None, audio=None, asr_words_count=None, total_score=None, business_type=None,
                 manual_score_mapping_list=None, file_merge_name=None, is_deleted=None, dialogues=None, deleted=None,
                 hand_score_info_list=None, vid=None, review_number=None):
        self.audio_url = TeaConverter.to_unicode(audio_url)  # type: unicode
        self.hit_number = hit_number  # type: int
        self.next_vid = TeaConverter.to_unicode(next_vid)  # type: unicode
        self.pre_vid = TeaConverter.to_unicode(pre_vid)  # type: unicode
        self.is_audio = is_audio  # type: bool
        self.hit_rule_review_info_list = hit_rule_review_info_list  # type: ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoList
        self.audio = audio  # type: bool
        self.asr_words_count = asr_words_count  # type: int
        self.total_score = total_score  # type: int
        self.business_type = business_type  # type: int
        self.manual_score_mapping_list = manual_score_mapping_list  # type: ReviewSingleResultByIdResponseBodyDataManualScoreMappingList
        self.file_merge_name = TeaConverter.to_unicode(file_merge_name)  # type: unicode
        self.is_deleted = is_deleted  # type: bool
        self.dialogues = dialogues  # type: ReviewSingleResultByIdResponseBodyDataDialogues
        self.deleted = deleted  # type: bool
        self.hand_score_info_list = hand_score_info_list  # type: ReviewSingleResultByIdResponseBodyDataHandScoreInfoList
        self.vid = vid  # type: int
        self.review_number = review_number  # type: int

    def validate(self):
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_mapping_list:
            self.manual_score_mapping_list.validate()
        if self.dialogues:
            self.dialogues.validate()
        if self.hand_score_info_list:
            self.hand_score_info_list.validate()

    def to_map(self):
        result = dict()
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.next_vid is not None:
            result['NextVid'] = self.next_vid
        if self.pre_vid is not None:
            result['PreVid'] = self.pre_vid
        if self.is_audio is not None:
            result['IsAudio'] = self.is_audio
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.asr_words_count is not None:
            result['AsrWordsCount'] = self.asr_words_count
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.manual_score_mapping_list is not None:
            result['ManualScoreMappingList'] = self.manual_score_mapping_list.to_map()
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.hand_score_info_list is not None:
            result['HandScoreInfoList'] = self.hand_score_info_list.to_map()
        if self.vid is not None:
            result['Vid'] = self.vid
        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('NextVid') is not None:
            self.next_vid = m.get('NextVid')
        if m.get('PreVid') is not None:
            self.pre_vid = m.get('PreVid')
        if m.get('IsAudio') is not None:
            self.is_audio = m.get('IsAudio')
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('AsrWordsCount') is not None:
            self.asr_words_count = m.get('AsrWordsCount')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('ManualScoreMappingList') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataManualScoreMappingList()
            self.manual_score_mapping_list = temp_model.from_map(m['ManualScoreMappingList'])
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Dialogues') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('HandScoreInfoList') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyDataHandScoreInfoList()
            self.hand_score_info_list = temp_model.from_map(m['HandScoreInfoList'])
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')
        return self


class ReviewSingleResultByIdResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ReviewSingleResultByIdResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ReviewSingleResultByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReviewSingleResultByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReviewSingleResultByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ReviewSingleResultByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveConfigDataSetRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SaveConfigDataSetResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveConfigDataSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SaveConfigDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitComplaintResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitComplaintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class SubmitCustomizationConfigRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitCustomizationConfigResponseBodyData(TeaModel):
    def __init__(self, model_status=None, model_name=None, model_id=None, mode_customization_id=None):
        self.model_status = model_status  # type: int
        self.model_name = TeaConverter.to_unicode(model_name)  # type: unicode
        self.model_id = model_id  # type: long
        self.mode_customization_id = TeaConverter.to_unicode(mode_customization_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')
        return self


class SubmitCustomizationConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: SubmitCustomizationConfigResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SubmitCustomizationConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitCustomizationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitCustomizationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SubmitCustomizationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPrecisionTaskRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitPrecisionTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitPrecisionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitPrecisionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitQualityCheckTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitQualityCheckTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitQualityCheckTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitReviewInfoResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitReviewInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitReviewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SyncQualityCheckResponseBodyDataRulesHitPhrase(TeaModel):
    def __init__(self, words=None, identity=None, begin=None, emotion_value=None, end=None, speech_rate=None,
                 role=None, silence_duration=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.begin = begin  # type: long
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.speech_rate = speech_rate  # type: int
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.silence_duration = silence_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class SyncQualityCheckResponseBodyDataRulesHitHitKeyWords(TeaModel):
    def __init__(self, from_=None, val=None, cid=None, pid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.cid = cid  # type: int
        self.pid = pid  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SyncQualityCheckResponseBodyDataRulesHit(TeaModel):
    def __init__(self, phrase=None, hit_key_words=None):
        self.phrase = phrase  # type: SyncQualityCheckResponseBodyDataRulesHitPhrase
        self.hit_key_words = hit_key_words  # type: list[SyncQualityCheckResponseBodyDataRulesHitHitKeyWords]

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.hit_key_words:
            for k in self.hit_key_words:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        result['HitKeyWords'] = []
        if self.hit_key_words is not None:
            for k in self.hit_key_words:
                result['HitKeyWords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = SyncQualityCheckResponseBodyDataRulesHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        self.hit_key_words = []
        if m.get('HitKeyWords') is not None:
            for k in m.get('HitKeyWords'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHitHitKeyWords()
                self.hit_key_words.append(temp_model.from_map(k))
        return self


class SyncQualityCheckResponseBodyDataRules(TeaModel):
    def __init__(self, hit=None, rule_name=None, rid=None):
        self.hit = hit  # type: list[SyncQualityCheckResponseBodyDataRulesHit]
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Hit'] = []
        if self.hit is not None:
            for k in self.hit:
                result['Hit'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k in m.get('Hit'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHit()
                self.hit.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class SyncQualityCheckResponseBodyData(TeaModel):
    def __init__(self, tid=None, begin_time=None, score=None, task_id=None, rules=None):
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.begin_time = begin_time  # type: long
        self.score = score  # type: int
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.rules = rules  # type: list[SyncQualityCheckResponseBodyDataRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.score is not None:
            result['Score'] = self.score
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SyncQualityCheckResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class SyncQualityCheckResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: SyncQualityCheckResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SyncQualityCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncQualityCheckResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SyncQualityCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class TestRuleRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(self, words=None, begin=None, identity=None, pid=None, emotion_value=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.begin = begin  # type: long
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.pid = pid  # type: int
        self.emotion_value = emotion_value  # type: int
        self.end = end  # type: long
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(self, from_=None, val=None, tid=None, pid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.pid = pid  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(TeaModel):
    def __init__(self, key_word=None):
        self.key_word = key_word  # type: list[TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord]

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(self, cid=None):
        self.cid = cid  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cid is not None:
            result['cid'] = self.cid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cid') is not None:
            self.cid = m.get('cid')
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(self, phrase=None, key_words=None, cid=None):
        self.phrase = phrase  # type: TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase
        self.key_words = key_words  # type: TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords
        self.cid = cid  # type: TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.key_words:
            self.key_words.validate()
        if self.cid:
            self.cid.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('KeyWords') is not None:
            temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Cid') is not None:
            temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(TeaModel):
    def __init__(self, condition_hit_info=None):
        self.condition_hit_info = condition_hit_info  # type: list[TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo]

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(self, condition_hit_info_list=None, rid=None):
        self.condition_hit_info_list = condition_hit_info_list  # type: TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList
        self.rid = rid  # type: long

    def validate(self):
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()

    def to_map(self):
        result = dict()
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionHitInfoList') is not None:
            temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class TestRuleResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(self, hit_rule_review_info=None):
        self.hit_rule_review_info = hit_rule_review_info  # type: list[TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo]

    def validate(self):
        if self.hit_rule_review_info:
            for k in self.hit_rule_review_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = TestRuleResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k))
        return self


class TestRuleResponseBodyData(TeaModel):
    def __init__(self, hit_rule_review_info_list=None, poc=None):
        self.hit_rule_review_info_list = hit_rule_review_info_list  # type: TestRuleResponseBodyDataHitRuleReviewInfoList
        self.poc = poc  # type: bool

    def validate(self):
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()

    def to_map(self):
        result = dict()
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.poc is not None:
            result['Poc'] = self.poc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = TestRuleResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('Poc') is not None:
            self.poc = m.get('Poc')
        return self


class TestRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: TestRuleResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = TestRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TestRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TestRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TestRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAsrVocabRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateAsrVocabResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAsrVocabResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAsrVocabResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class UpdateOnPurchaseSuccessRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateOnPurchaseSuccessResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateOnPurchaseSuccessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateOnPurchaseSuccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateOnPurchaseSuccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSkillGroupConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSkillGroupConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateSkillGroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSubScoreForApiResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSubScoreForApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateSubScoreForApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSyncQualityCheckDataResponseBodyData(TeaModel):
    def __init__(self, tid=None, task_id=None):
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateSyncQualityCheckDataResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: UpdateSyncQualityCheckDataResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = UpdateSyncQualityCheckDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSyncQualityCheckDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateSyncQualityCheckDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateTaskAssignRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskAssignRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateTaskAssignRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateUserConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateUserConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateWarningConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWarningConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateWarningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadAudioDataResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadAudioDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadAudioDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase(TeaModel):
    def __init__(self, words=None, identity=None, begin=None, begin_time=None, end=None, role=None):
        self.words = TeaConverter.to_unicode(words)  # type: unicode
        self.identity = TeaConverter.to_unicode(identity)  # type: unicode
        self.begin = begin  # type: long
        self.begin_time = TeaConverter.to_unicode(begin_time)  # type: unicode
        self.end = end  # type: long
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids(TeaModel):
    def __init__(self, cid_item=None):
        self.cid_item = cid_item  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, from_=None, val=None, tid=None, pid=None, to=None):
        self.from_ = from_  # type: int
        self.val = TeaConverter.to_unicode(val)  # type: unicode
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.pid = pid  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.val is not None:
            result['Val'] = self.val
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('To') is not None:
            self.to = m.get('To')
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


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo(TeaModel):
    def __init__(self, phrase=None, hit_cids=None, hit_key_words=None):
        self.phrase = phrase  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase
        self.hit_cids = hit_cids  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids
        self.hit_key_words = hit_key_words  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords

    def validate(self):
        if self.phrase:
            self.phrase.validate()
        if self.hit_cids:
            self.hit_cids.validate()
        if self.hit_key_words:
            self.hit_key_words.validate()

    def to_map(self):
        result = dict()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        if self.hit_cids is not None:
            result['HitCids'] = self.hit_cids.to_map()
        if self.hit_key_words is not None:
            result['HitKeyWords'] = self.hit_key_words.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phrase') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        if m.get('HitCids') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids()
            self.hit_cids = temp_model.from_map(m['HitCids'])
        if m.get('HitKeyWords') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords()
            self.hit_key_words = temp_model.from_map(m['HitKeyWords'])
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


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo(TeaModel):
    def __init__(self, condition_info_cid=None):
        self.condition_info_cid = TeaConverter.to_unicode(condition_info_cid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo(TeaModel):
    def __init__(self, tid=None, hit=None, condition_info=None, rid=None):
        self.tid = TeaConverter.to_unicode(tid)  # type: unicode
        self.hit = hit  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit
        self.condition_info = condition_info  # type: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo
        self.rid = TeaConverter.to_unicode(rid)  # type: unicode

    def validate(self):
        if self.hit:
            self.hit.validate()
        if self.condition_info:
            self.condition_info.validate()

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.hit is not None:
            result['Hit'] = self.hit.to_map()
        if self.condition_info is not None:
            result['ConditionInfo'] = self.condition_info.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Hit') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit()
            self.hit = temp_model.from_map(m['Hit'])
        if m.get('ConditionInfo') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo()
            self.condition_info = temp_model.from_map(m['ConditionInfo'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
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


class UploadDataSyncResponseBodyDataResultInfoHandScoreIdList(TeaModel):
    def __init__(self, hand_score_id_list=None):
        self.hand_score_id_list = hand_score_id_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            self.hand_score_id_list = m.get('HandScoreIdList')
        return self


class UploadDataSyncResponseBodyDataResultInfo(TeaModel):
    def __init__(self, score=None, rules=None, hand_score_id_list=None):
        self.score = score  # type: int
        self.rules = rules  # type: UploadDataSyncResponseBodyDataResultInfoRules
        self.hand_score_id_list = hand_score_id_list  # type: UploadDataSyncResponseBodyDataResultInfoHandScoreIdList

    def validate(self):
        if self.rules:
            self.rules.validate()
        if self.hand_score_id_list:
            self.hand_score_id_list.validate()

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Rules') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('HandScoreIdList') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoHandScoreIdList()
            self.hand_score_id_list = temp_model.from_map(m['HandScoreIdList'])
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: UploadDataSyncResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = UploadDataSyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataSyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadDataSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadRuleResponseBodyData(TeaModel):
    def __init__(self, rid_info=None):
        self.rid_info = rid_info  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: UploadRuleResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = UploadRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifyFileResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: float
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: VerifyFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
    def __init__(self, resource_owner_id=None, json_str=None):
        self.resource_owner_id = resource_owner_id  # type: long
        self.json_str = TeaConverter.to_unicode(json_str)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifySentenceResponseBodyDataDeltaSourceLine(TeaModel):
    def __init__(self, line=None):
        self.line = line  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.line = line  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, type=None, source=None, target=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.source = source  # type: VerifySentenceResponseBodyDataDeltaSource
        self.target = target  # type: VerifySentenceResponseBodyDataDeltaTarget

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Source') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
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
    def __init__(self, source_role=None, incorrect_words=None, request_id=None, message=None, target_role=None,
                 data=None, code=None, success=None):
        self.source_role = source_role  # type: int
        self.incorrect_words = incorrect_words  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.target_role = target_role  # type: int
        self.data = data  # type: VerifySentenceResponseBodyData
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.target_role is not None:
            result['TargetRole'] = self.target_role
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        if m.get('Data') is not None:
            temp_model = VerifySentenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifySentenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: VerifySentenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


