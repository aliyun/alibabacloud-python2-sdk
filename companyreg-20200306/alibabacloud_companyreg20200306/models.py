# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BindProduceAuthorizationRequest(TeaModel):
    def __init__(self, authorized_user_ids=None, biz_id=None, biz_type=None):
        self.authorized_user_ids = authorized_user_ids  # type: str
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindProduceAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class BindProduceAuthorizationResponseBodyDataAuthorizedUserList(TeaModel):
    def __init__(self, account_valid_type=None, user_id=None, user_name=None):
        self.account_valid_type = account_valid_type  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindProduceAuthorizationResponseBodyDataAuthorizedUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_valid_type is not None:
            result['AccountValidType'] = self.account_valid_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountValidType') is not None:
            self.account_valid_type = m.get('AccountValidType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindProduceAuthorizationResponseBodyData(TeaModel):
    def __init__(self, authorized_user_list=None, message=None, success=None):
        self.authorized_user_list = authorized_user_list  # type: list[BindProduceAuthorizationResponseBodyDataAuthorizedUserList]
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.authorized_user_list:
            for k in self.authorized_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BindProduceAuthorizationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k in self.authorized_user_list:
                result['AuthorizedUserList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k in m.get('AuthorizedUserList'):
                temp_model = BindProduceAuthorizationResponseBodyDataAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindProduceAuthorizationResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_msg=None, request_id=None):
        self.data = data  # type: BindProduceAuthorizationResponseBodyData
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BindProduceAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BindProduceAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindProduceAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindProduceAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindProduceAuthorizationResponse, self).to_map()
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
            temp_model = BindProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseIntentionForPartnerRequest(TeaModel):
    def __init__(self, biz_type=None, intention_biz_id=None, note=None):
        self.biz_type = biz_type  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseIntentionForPartnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class CloseIntentionForPartnerResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseIntentionForPartnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseIntentionForPartnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseIntentionForPartnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseIntentionForPartnerResponse, self).to_map()
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
            temp_model = CloseIntentionForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseUserIntentionRequest(TeaModel):
    def __init__(self, biz_type=None, intention_biz_id=None, note=None):
        self.biz_type = biz_type  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseUserIntentionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class CloseUserIntentionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseUserIntentionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseUserIntentionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseUserIntentionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseUserIntentionResponse, self).to_map()
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
            temp_model = CloseUserIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBusinessOpportunityRequest(TeaModel):
    def __init__(self, biz_type=None, contact_name=None, mobile=None, source=None, vcode=None):
        self.biz_type = biz_type  # type: str
        self.contact_name = contact_name  # type: str
        self.mobile = mobile  # type: str
        self.source = source  # type: int
        self.vcode = vcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBusinessOpportunityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.source is not None:
            result['Source'] = self.source
        if self.vcode is not None:
            result['VCode'] = self.vcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VCode') is not None:
            self.vcode = m.get('VCode')
        return self


class CreateBusinessOpportunityResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBusinessOpportunityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBusinessOpportunityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBusinessOpportunityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBusinessOpportunityResponse, self).to_map()
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
            temp_model = CreateBusinessOpportunityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProduceForPartnerRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, ext_info=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProduceForPartnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class CreateProduceForPartnerResponseBody(TeaModel):
    def __init__(self, biz_id=None, error_code=None, error_msg=None, request_id=None, success=None):
        self.biz_id = biz_id  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProduceForPartnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProduceForPartnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProduceForPartnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProduceForPartnerResponse, self).to_map()
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
            temp_model = CreateProduceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePartnerConfigRequest(TeaModel):
    def __init__(self, biz_type=None, partner_code=None):
        self.biz_type = biz_type  # type: str
        self.partner_code = partner_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePartnerConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        return self


class DescribePartnerConfigResponseBody(TeaModel):
    def __init__(self, contact=None, partner_code=None, partner_name=None, request_id=None):
        self.contact = contact  # type: str
        self.partner_code = partner_code  # type: str
        self.partner_name = partner_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePartnerConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePartnerConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePartnerConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePartnerConfigResponse, self).to_map()
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
            temp_model = DescribePartnerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(self, biz_type=None, file_name=None, file_type=None):
        self.biz_type = biz_type  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(self, access_id=None, encoded_policy=None, expire_time=None, file_dir=None, file_url=None,
                 host=None, request_id=None, signature=None):
        # OSSAccessKeyId
        self.access_id = access_id  # type: str
        self.encoded_policy = encoded_policy  # type: str
        self.expire_time = expire_time  # type: str
        self.file_dir = file_dir  # type: str
        self.file_url = file_url  # type: str
        # OSS Endpoint。
        self.host = host  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GenerateUploadFilePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateUploadFilePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponse, self).to_map()
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
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlipayUrlRequest(TeaModel):
    def __init__(self, biz_type=None, order_id=None, return_url=None, type=None):
        self.biz_type = biz_type  # type: str
        self.order_id = order_id  # type: long
        self.return_url = return_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlipayUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAlipayUrlResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlipayUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlipayUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlipayUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlipayUrlResponse, self).to_map()
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
            temp_model = GetAlipayUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntentionNoteRequest(TeaModel):
    def __init__(self, begin_time=None, end_time=None, intention_biz_id=None, page_number=None, page_size=None):
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntentionNoteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIntentionNoteResponseBodyData(TeaModel):
    def __init__(self, create_time=None, intention_biz_id=None, note=None, source=None, type=None):
        self.create_time = create_time  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.note = note  # type: str
        self.source = source  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntentionNoteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListIntentionNoteResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListIntentionNoteResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntentionNoteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListIntentionNoteResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListIntentionNoteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIntentionNoteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntentionNoteResponse, self).to_map()
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
            temp_model = ListIntentionNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProduceAuthorizationRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, page_num=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProduceAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListProduceAuthorizationResponseBodyData(TeaModel):
    def __init__(self, authorized_user_id=None, authorized_user_name=None):
        self.authorized_user_id = authorized_user_id  # type: str
        self.authorized_user_name = authorized_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProduceAuthorizationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.authorized_user_name is not None:
            result['AuthorizedUserName'] = self.authorized_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('AuthorizedUserName') is not None:
            self.authorized_user_name = m.get('AuthorizedUserName')
        return self


class ListProduceAuthorizationResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, success=None,
                 total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListProduceAuthorizationResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProduceAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProduceAuthorizationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListProduceAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProduceAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProduceAuthorizationResponse, self).to_map()
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
            temp_model = ListProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDetailSolutionsRequest(TeaModel):
    def __init__(self, biz_type=None, intention_biz_id=None, page_num=None, page_size=None):
        self.biz_type = biz_type  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDetailSolutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDetailSolutionsResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, create_time=None, delivery_order_biz_id=None, ext_info=None,
                 intention_assign_biz_id=None, intention_biz_id=None, partner_code=None, reason=None, status=None, update_time=None,
                 user_id=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.create_time = create_time  # type: long
        self.delivery_order_biz_id = delivery_order_biz_id  # type: str
        self.ext_info = ext_info  # type: str
        self.intention_assign_biz_id = intention_assign_biz_id  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.partner_code = partner_code  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDetailSolutionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_order_biz_id is not None:
            result['DeliveryOrderBizId'] = self.delivery_order_biz_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intention_assign_biz_id is not None:
            result['IntentionAssignBizId'] = self.intention_assign_biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryOrderBizId') is not None:
            self.delivery_order_biz_id = m.get('DeliveryOrderBizId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('IntentionAssignBizId') is not None:
            self.intention_assign_biz_id = m.get('IntentionAssignBizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserDetailSolutionsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListUserDetailSolutionsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserDetailSolutionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserDetailSolutionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserDetailSolutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserDetailSolutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserDetailSolutionsResponse, self).to_map()
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
            temp_model = ListUserDetailSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserIntentionNotesRequest(TeaModel):
    def __init__(self, biz_type=None, intention_biz_id=None, page_num=None, page_size=None):
        self.biz_type = biz_type  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserIntentionNotesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserIntentionNotesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, note=None):
        self.create_time = create_time  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserIntentionNotesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ListUserIntentionNotesResponseBody(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, request_id=None, success=None, total_item_num=None,
                 total_page_num=None):
        self.data = data  # type: list[ListUserIntentionNotesResponseBodyData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserIntentionNotesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserIntentionNotesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserIntentionNotesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserIntentionNotesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserIntentionNotesResponse, self).to_map()
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
            temp_model = ListUserIntentionNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserIntentionsRequest(TeaModel):
    def __init__(self, area=None, biz_type=None, biz_types=None, intention_biz_id=None, page_num=None,
                 page_size=None, sort_filed=None, sort_order=None, status=None, with_ext_info=None):
        self.area = area  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_types = biz_types  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str
        self.status = status  # type: int
        self.with_ext_info = with_ext_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserIntentionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        if self.with_ext_info is not None:
            result['WithExtInfo'] = self.with_ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WithExtInfo') is not None:
            self.with_ext_info = m.get('WithExtInfo')
        return self


class ListUserIntentionsResponseBodyData(TeaModel):
    def __init__(self, area=None, biz_id=None, biz_type=None, contact_name=None, create_time=None, description=None,
                 ext=None, mobile=None, reason=None, status=None, update_time=None, user_id=None):
        self.area = area  # type: str
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.contact_name = contact_name  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.ext = ext  # type: str
        self.mobile = mobile  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserIntentionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserIntentionsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListUserIntentionsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserIntentionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserIntentionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserIntentionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserIntentionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserIntentionsResponse, self).to_map()
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
            temp_model = ListUserIntentionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserProduceOperateLogsRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, page_num=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserProduceOperateLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserProduceOperateLogsResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, biz_status=None, biz_type=None, note=None, operate_name=None, operate_time=None,
                 operate_user_type=None, to_biz_status=None):
        self.biz_id = biz_id  # type: str
        self.biz_status = biz_status  # type: int
        self.biz_type = biz_type  # type: str
        self.note = note  # type: str
        self.operate_name = operate_name  # type: str
        self.operate_time = operate_time  # type: long
        self.operate_user_type = operate_user_type  # type: str
        self.to_biz_status = to_biz_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserProduceOperateLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_name is not None:
            result['OperateName'] = self.operate_name
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_user_type is not None:
            result['OperateUserType'] = self.operate_user_type
        if self.to_biz_status is not None:
            result['ToBizStatus'] = self.to_biz_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateName') is not None:
            self.operate_name = m.get('OperateName')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateUserType') is not None:
            self.operate_user_type = m.get('OperateUserType')
        if m.get('ToBizStatus') is not None:
            self.to_biz_status = m.get('ToBizStatus')
        return self


class ListUserProduceOperateLogsResponseBody(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, request_id=None, success=None, total_item_num=None,
                 total_page_num=None):
        self.data = data  # type: list[ListUserProduceOperateLogsResponseBodyData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserProduceOperateLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserProduceOperateLogsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserProduceOperateLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserProduceOperateLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserProduceOperateLogsResponse, self).to_map()
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
            temp_model = ListUserProduceOperateLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSolutionsRequest(TeaModel):
    def __init__(self, exist_status=None, intention_biz_id=None, page_num=None, page_size=None):
        self.exist_status = exist_status  # type: list[long]
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSolutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSolutionsShrinkRequest(TeaModel):
    def __init__(self, exist_status_shrink=None, intention_biz_id=None, page_num=None, page_size=None):
        self.exist_status_shrink = exist_status_shrink  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSolutionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status_shrink is not None:
            result['ExistStatus'] = self.exist_status_shrink
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status_shrink = m.get('ExistStatus')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSolutionsResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, create_time=None, delivery_order_biz_id=None,
                 intention_assign_biz_id=None, intention_biz_id=None, partner_code=None, reason=None, status=None, update_time=None,
                 user_id=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.create_time = create_time  # type: long
        self.delivery_order_biz_id = delivery_order_biz_id  # type: str
        self.intention_assign_biz_id = intention_assign_biz_id  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.partner_code = partner_code  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSolutionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_order_biz_id is not None:
            result['DeliveryOrderBizId'] = self.delivery_order_biz_id
        if self.intention_assign_biz_id is not None:
            result['IntentionAssignBizId'] = self.intention_assign_biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryOrderBizId') is not None:
            self.delivery_order_biz_id = m.get('DeliveryOrderBizId')
        if m.get('IntentionAssignBizId') is not None:
            self.intention_assign_biz_id = m.get('IntentionAssignBizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserSolutionsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListUserSolutionsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserSolutionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserSolutionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserSolutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserSolutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserSolutionsResponse, self).to_map()
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
            temp_model = ListUserSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateProduceForPartnerRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, ext_info=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.ext_info = ext_info  # type: str
        self.operate_type = operate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateProduceForPartnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class OperateProduceForPartnerResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateProduceForPartnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateProduceForPartnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OperateProduceForPartnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateProduceForPartnerResponse, self).to_map()
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
            temp_model = OperateProduceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureDataRequest(TeaModel):
    def __init__(self, biz_type=None, data=None, data_type=None, end_time=None, start_time=None):
        self.biz_type = biz_type  # type: str
        self.data = data  # type: str
        self.data_type = data_type  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutMeasureDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PutMeasureDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutMeasureDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutMeasureDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutMeasureDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutMeasureDataResponse, self).to_map()
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
            temp_model = PutMeasureDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureReadyFlagRequest(TeaModel):
    def __init__(self, biz_type=None, data_type=None, end_time=None, ready_flag=None, start_time=None):
        self.biz_type = biz_type  # type: str
        self.data_type = data_type  # type: str
        self.end_time = end_time  # type: str
        self.ready_flag = ready_flag  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutMeasureReadyFlagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ready_flag is not None:
            result['ReadyFlag'] = self.ready_flag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReadyFlag') is not None:
            self.ready_flag = m.get('ReadyFlag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PutMeasureReadyFlagResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutMeasureReadyFlagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutMeasureReadyFlagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutMeasureReadyFlagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutMeasureReadyFlagResponse, self).to_map()
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
            temp_model = PutMeasureReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvailableNumbersRequest(TeaModel):
    def __init__(self, biz_type=None):
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvailableNumbersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryAvailableNumbersResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: list[str]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvailableNumbersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvailableNumbersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAvailableNumbersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAvailableNumbersResponse, self).to_map()
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
            temp_model = QueryAvailableNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBagRemainingRequest(TeaModel):
    def __init__(self, biz_type=None):
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBagRemainingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryBagRemainingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBagRemainingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryBagRemainingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBagRemainingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBagRemainingResponse, self).to_map()
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
            temp_model = QueryBagRemainingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommodityConfigRequest(TeaModel):
    def __init__(self, biz_type=None, commodity_code=None, query_module=None):
        self.biz_type = biz_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.query_module = query_module  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommodityConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.query_module is not None:
            result['QueryModule'] = self.query_module
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('QueryModule') is not None:
            self.query_module = m.get('QueryModule')
        return self


class QueryCommodityConfigResponseBodyDataCommodityModules(TeaModel):
    def __init__(self, lx_module_code=None, module_code=None, module_description=None, module_name=None,
                 module_tip=None, module_type=None, module_url=None, module_value=None, sort_number=None):
        self.lx_module_code = lx_module_code  # type: str
        self.module_code = module_code  # type: str
        self.module_description = module_description  # type: str
        self.module_name = module_name  # type: str
        self.module_tip = module_tip  # type: str
        self.module_type = module_type  # type: str
        self.module_url = module_url  # type: str
        self.module_value = module_value  # type: str
        self.sort_number = sort_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommodityConfigResponseBodyDataCommodityModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lx_module_code is not None:
            result['LxModuleCode'] = self.lx_module_code
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_description is not None:
            result['ModuleDescription'] = self.module_description
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_tip is not None:
            result['ModuleTip'] = self.module_tip
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.module_url is not None:
            result['ModuleUrl'] = self.module_url
        if self.module_value is not None:
            result['ModuleValue'] = self.module_value
        if self.sort_number is not None:
            result['SortNumber'] = self.sort_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LxModuleCode') is not None:
            self.lx_module_code = m.get('LxModuleCode')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleDescription') is not None:
            self.module_description = m.get('ModuleDescription')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleTip') is not None:
            self.module_tip = m.get('ModuleTip')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('ModuleUrl') is not None:
            self.module_url = m.get('ModuleUrl')
        if m.get('ModuleValue') is not None:
            self.module_value = m.get('ModuleValue')
        if m.get('SortNumber') is not None:
            self.sort_number = m.get('SortNumber')
        return self


class QueryCommodityConfigResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, commodity_modules=None, description=None, icon_url=None,
                 product_line=None, protocol_url=None, starting_price=None, type=None):
        self.commodity_code = commodity_code  # type: str
        self.commodity_modules = commodity_modules  # type: list[QueryCommodityConfigResponseBodyDataCommodityModules]
        self.description = description  # type: str
        self.icon_url = icon_url  # type: str
        self.product_line = product_line  # type: str
        self.protocol_url = protocol_url  # type: str
        self.starting_price = starting_price  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.commodity_modules:
            for k in self.commodity_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCommodityConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['CommodityModules'] = []
        if self.commodity_modules is not None:
            for k in self.commodity_modules:
                result['CommodityModules'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.product_line is not None:
            result['ProductLine'] = self.product_line
        if self.protocol_url is not None:
            result['ProtocolUrl'] = self.protocol_url
        if self.starting_price is not None:
            result['StartingPrice'] = self.starting_price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.commodity_modules = []
        if m.get('CommodityModules') is not None:
            for k in m.get('CommodityModules'):
                temp_model = QueryCommodityConfigResponseBodyDataCommodityModules()
                self.commodity_modules.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('ProductLine') is not None:
            self.product_line = m.get('ProductLine')
        if m.get('ProtocolUrl') is not None:
            self.protocol_url = m.get('ProtocolUrl')
        if m.get('StartingPrice') is not None:
            self.starting_price = m.get('StartingPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCommodityConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryCommodityConfigResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCommodityConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryCommodityConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCommodityConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCommodityConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCommodityConfigResponse, self).to_map()
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
            temp_model = QueryCommodityConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceRequest(TeaModel):
    def __init__(self, biz_type=None, instance_id=None):
        self.biz_type = biz_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryInstanceResponse, self).to_map()
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
            temp_model = QueryInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPartnerIntentionListRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, page_num=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPartnerIntentionListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPartnerIntentionListResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, mobile=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPartnerIntentionListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class QueryPartnerIntentionListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: long
        self.data = data  # type: list[QueryPartnerIntentionListResponseBodyData]
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: long
        self.total_page_num = total_page_num  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPartnerIntentionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryPartnerIntentionListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryPartnerIntentionListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPartnerIntentionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPartnerIntentionListResponse, self).to_map()
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
            temp_model = QueryPartnerIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPartnerProduceListRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, page_num=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPartnerProduceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPartnerProduceListResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, mobile=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPartnerProduceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.mobile is not None:
            result['mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        return self


class QueryPartnerProduceListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: long
        self.data = data  # type: list[QueryPartnerProduceListResponseBodyData]
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: long
        self.total_page_num = total_page_num  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPartnerProduceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryPartnerProduceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryPartnerProduceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPartnerProduceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPartnerProduceListResponse, self).to_map()
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
            temp_model = QueryPartnerProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserNeedAuthResponseBody(TeaModel):
    def __init__(self, need_auth=None, request_id=None, success=None):
        self.need_auth = need_auth  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserNeedAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_auth is not None:
            result['NeedAuth'] = self.need_auth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedAuth') is not None:
            self.need_auth = m.get('NeedAuth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserNeedAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUserNeedAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserNeedAuthResponse, self).to_map()
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
            temp_model = QueryUserNeedAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordPostBackRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, contactor=None, content=None, entity_key=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.contactor = contactor  # type: str
        self.content = content  # type: str
        self.entity_key = entity_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordPostBackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.contactor is not None:
            result['contactor'] = self.contactor
        if self.content is not None:
            result['content'] = self.content
        if self.entity_key is not None:
            result['entityKey'] = self.entity_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('contactor') is not None:
            self.contactor = m.get('contactor')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('entityKey') is not None:
            self.entity_key = m.get('entityKey')
        return self


class RecordPostBackResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, dynamic_code=None, dynamic_message=None, error_args=None,
                 error_code=None, error_msg=None, http_status_code=None, module=None, request_id=None, success=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_args = error_args  # type: list[any]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordPostBackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecordPostBackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecordPostBackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecordPostBackResponse, self).to_map()
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
            temp_model = RecordPostBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectSolutionRequest(TeaModel):
    def __init__(self, note=None, solution_biz_id=None):
        self.note = note  # type: str
        self.solution_biz_id = solution_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        return self


class RejectSolutionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RejectSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectSolutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectSolutionResponse, self).to_map()
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
            temp_model = RejectSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectUserSolutionRequest(TeaModel):
    def __init__(self, biz_type=None, note=None, solution_biz_id=None):
        self.biz_type = biz_type  # type: str
        self.note = note  # type: str
        self.solution_biz_id = solution_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectUserSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.note is not None:
            result['Note'] = self.note
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        return self


class RejectUserSolutionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectUserSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RejectUserSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectUserSolutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectUserSolutionResponse, self).to_map()
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
            temp_model = RejectUserSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseProduceAuthorizationRequest(TeaModel):
    def __init__(self, authorized_user_id=None, biz_id=None, biz_type=None):
        self.authorized_user_id = authorized_user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseProduceAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class ReleaseProduceAuthorizationResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseProduceAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseProduceAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseProduceAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseProduceAuthorizationResponse, self).to_map()
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
            temp_model = ReleaseProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBackToBackCallRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, call_center_number=None, caller=None, mobile_key=None,
                 skill_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.call_center_number = call_center_number  # type: str
        self.caller = caller  # type: str
        self.mobile_key = mobile_key  # type: str
        self.skill_type = skill_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartBackToBackCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.call_center_number is not None:
            result['CallCenterNumber'] = self.call_center_number
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.mobile_key is not None:
            result['MobileKey'] = self.mobile_key
        if self.skill_type is not None:
            result['SkillType'] = self.skill_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallCenterNumber') is not None:
            self.call_center_number = m.get('CallCenterNumber')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('MobileKey') is not None:
            self.mobile_key = m.get('MobileKey')
        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')
        return self


class StartBackToBackCallResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartBackToBackCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartBackToBackCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartBackToBackCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartBackToBackCallResponse, self).to_map()
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
            temp_model = StartBackToBackCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIntentionNoteRequest(TeaModel):
    def __init__(self, intention_biz_id=None, note=None):
        self.intention_biz_id = intention_biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIntentionNoteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class SubmitIntentionNoteResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIntentionNoteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitIntentionNoteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitIntentionNoteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitIntentionNoteResponse, self).to_map()
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
            temp_model = SubmitIntentionNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSolutionRequest(TeaModel):
    def __init__(self, biz_type=None, intention_biz_id=None, solution=None, user_id=None):
        self.biz_type = biz_type  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.solution = solution  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SubmitSolutionResponseBody(TeaModel):
    def __init__(self, confirm_url=None, error_code=None, error_msg=None, request_id=None, solution_biz_id=None,
                 success=None):
        self.confirm_url = confirm_url  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.solution_biz_id = solution_biz_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm_url is not None:
            result['ConfirmUrl'] = self.confirm_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfirmUrl') is not None:
            self.confirm_url = m.get('ConfirmUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitSolutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSolutionResponse, self).to_map()
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
            temp_model = SubmitSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferIntentionOwnerRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, person_id=None, remark=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.person_id = person_id  # type: int
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferIntentionOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class TransferIntentionOwnerResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferIntentionOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferIntentionOwnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferIntentionOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferIntentionOwnerResponse, self).to_map()
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
            temp_model = TransferIntentionOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferProduceOwnerRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, person_id=None, remark=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.person_id = person_id  # type: int
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferProduceOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class TransferProduceOwnerResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferProduceOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferProduceOwnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferProduceOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferProduceOwnerResponse, self).to_map()
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
            temp_model = TransferProduceOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


