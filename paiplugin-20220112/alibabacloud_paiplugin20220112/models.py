# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateSignatureRequest(TeaModel):
    def __init__(self, description=None, name=None):
        # 申请说明。
        self.description = description  # type: str
        # 签名名称。
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSignatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSignatureResponseBodyData(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, status=None, updated_time=None):
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 签名Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSignatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: CreateSignatureResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSignatureResponse, self).to_map()
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
            temp_model = CreateSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, content=None, description=None, name=None, signature=None, signature_id=None, type=None):
        # 模板内容，请注意控制总字数在70个字以内，超出部分按长短信收费，按67个字为单位记一条短信，营销短信必须在结尾添加“回T退订”。
        self.content = content  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板名称。
        self.name = name  # type: str
        # 签名名称，同时只能指定签名名称或签名Id其中之一。
        self.signature = signature  # type: str
        # 签名Id，可通过ListSignatures获取审核状态为已通过的签名列表，获取签名Id。
        self.signature_id = signature_id  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBodyData(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名Id。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: CreateTemplateResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSignatureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSignatureResponse, self).to_map()
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
            temp_model = DeleteSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageConfigResponseBodyData(TeaModel):
    def __init__(self, sms_report_url=None, sms_up_url=None):
        # 短信发送状态回执接收服务地址。
        self.sms_report_url = sms_report_url  # type: str
        # 上行短信消息接收服务地址。
        self.sms_up_url = sms_up_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sms_report_url is not None:
            result['SmsReportUrl'] = self.sms_report_url
        if self.sms_up_url is not None:
            result['SmsUpUrl'] = self.sms_up_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SmsReportUrl') is not None:
            self.sms_report_url = m.get('SmsReportUrl')
        if m.get('SmsUpUrl') is not None:
            self.sms_up_url = m.get('SmsUpUrl')
        return self


class GetMessageConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: GetMessageConfigResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMessageConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMessageConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMessageConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMessageConfigResponse, self).to_map()
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
            temp_model = GetMessageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignatureResponseBodyData(TeaModel):
    def __init__(self, created_time=None, description=None, id=None, name=None, reason=None, status=None,
                 updated_time=None):
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 签名Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核建议。
        self.reason = reason  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSignatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: GetSignatureResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSignatureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSignatureResponse, self).to_map()
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
            temp_model = GetSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名Id。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: GetTemplateResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(self, account_status=None):
        # 账号状态。
        # - 0 : 正常使用。
        # - 1 : 因欠费等原因暂时停用。
        # - 2 : 已释放产品。
        self.account_status = account_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: GetUserResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageMetricsRequest(TeaModel):
    def __init__(self, end_date=None, group_id=None, page_number=None, page_size=None, schedule_id=None,
                 signature=None, signature_id=None, start_date=None, template_code=None, template_id=None, template_type=None):
        # 结束日期，必填，格式20220102。
        self.end_date = end_date  # type: str
        # 关联人群Id。
        self.group_id = group_id  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 关联触达计划Id。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.signature = signature  # type: str
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 开始日期，必填，格式20220102。
        self.start_date = start_date  # type: str
        # 模板号。
        self.template_code = template_code  # type: str
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 模板类型。
        # 0 : 验证码。
        # 1 : 短信通知。
        # 2 : 推广短信。
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessageMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessageMetricsResponseBodyDataMetrics(TeaModel):
    def __init__(self, date=None, fail=None, pending=None, rate=None, success=None, total=None):
        # 发送日期。
        self.date = date  # type: str
        # 发送失败。
        self.fail = fail  # type: int
        # 发送中。
        self.pending = pending  # type: int
        # 发送成功率。
        self.rate = rate  # type: float
        # 发送成功。
        self.success = success  # type: int
        # 总计短信数量。
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessageMetricsResponseBodyDataMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMessageMetricsResponseBodyData(TeaModel):
    def __init__(self, metrics=None, page_number=None, page_size=None, total_count=None):
        # 统计数据列表。
        self.metrics = metrics  # type: list[ListMessageMetricsResponseBodyDataMetrics]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总统计数量。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = ListMessageMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageMetricsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: ListMessageMetricsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessageMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessageMetricsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMessageMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponse, self).to_map()
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
            temp_model = ListMessageMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessagesRequest(TeaModel):
    def __init__(self, datetime=None, error_code=None, group_id=None, message_id=None, page_number=None,
                 page_size=None, phone_number=None, request_id=None, schedule_id=None, signature=None, signature_id=None,
                 status=None, template_code=None, template_id=None, template_type=None):
        # 发送日期，格式为20220101。
        self.datetime = datetime  # type: str
        # 短信错误码过滤。
        self.error_code = error_code  # type: str
        # 关联人群Id过滤。
        self.group_id = group_id  # type: str
        # 短信Id过滤，短信Id为SendMessage成功返回的Id。
        self.message_id = message_id  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 手机号码过滤。
        self.phone_number = phone_number  # type: str
        # 短信批处理Id过滤，短信批处理Id为SendMessage成功返回的RequestId。
        self.request_id = request_id  # type: str
        # 关联触达计划Id过滤。
        self.schedule_id = schedule_id  # type: str
        # 签名名称过滤。
        self.signature = signature  # type: str
        # 签名Id过滤，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 短信发送状态过滤。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status  # type: int
        # 模板号过滤。
        self.template_code = template_code  # type: str
        # 模板Id过滤，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 模板类型过滤。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datetime is not None:
            result['Datetime'] = self.datetime
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyDataMessages(TeaModel):
    def __init__(self, error_code=None, group_id=None, id=None, out_id=None, phone_number=None, schedule_id=None,
                 signature=None, status=None, template_code=None, template_params=None, template_type=None):
        # 短信错误码。
        self.error_code = error_code  # type: str
        # 关联人群Id，未关联则为空。
        self.group_id = group_id  # type: str
        # 短信序列号。
        self.id = id  # type: str
        # 外部拓展字段。
        self.out_id = out_id  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 关联触达计划Id，未关联则为空。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.signature = signature  # type: str
        # 短信发送状态。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status  # type: int
        # 模板号。
        self.template_code = template_code  # type: str
        # 模板参数。
        self.template_params = template_params  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessagesResponseBodyDataMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyData(TeaModel):
    def __init__(self, messages=None, page_number=None, page_size=None, total_count=None):
        # 短信列表。
        self.messages = messages  # type: list[ListMessagesResponseBodyDataMessages]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 短信数量。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMessagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ListMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessagesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: ListMessagesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListMessagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMessagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMessagesResponse, self).to_map()
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
            temp_model = ListMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSignaturesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, status=None):
        # 签名名称。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 审核状态。
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSignaturesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSignaturesResponseBodyDataSignatures(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, status=None, updated_time=None):
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 签名Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSignaturesResponseBodyDataSignatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSignaturesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, signatures=None, total_count=None):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 签名列表。
        self.signatures = signatures  # type: list[ListSignaturesResponseBodyDataSignatures]
        # 签名数量。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSignaturesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = ListSignaturesResponseBodyDataSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSignaturesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: ListSignaturesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListSignaturesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSignaturesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSignaturesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSignaturesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSignaturesResponse, self).to_map()
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
            temp_model = ListSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, content=None, name=None, page_number=None, page_size=None, status=None, type=None):
        # 内容类型过滤。
        self.content = content  # type: str
        # 模板名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 审核状态过滤。
        self.status = status  # type: int
        # 模板类型过滤。
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBodyDataTemplates(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名Id。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyDataTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListTemplatesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, templates=None, total_count=None):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 模板列表。
        self.templates = templates  # type: list[ListTemplatesResponseBodyDataTemplates]
        # 总模板数量。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: ListTemplatesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, group_id=None, out_ids=None, phone_numbers=None, schedule_id=None, sign_name=None,
                 signature_id=None, sms_up_extend_codes=None, template_code=None, template_id=None, template_params=None):
        # 人群Id，用于关联人群。
        self.group_id = group_id  # type: str
        # 外部拓展字段，示例：["1234567890"]。
        self.out_ids = out_ids  # type: list[str]
        # 手机号，每个手机号对应一个模板变量、上行拓展码和外部拓展字段，示例：["1234567890"]。
        self.phone_numbers = phone_numbers  # type: list[str]
        # 触达计划Id，用于关联触达计划。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.sign_name = sign_name  # type: str
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 短信上行拓展码，示例：["1234567890"]。
        self.sms_up_extend_codes = sms_up_extend_codes  # type: list[str]
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 短信模板变量对应的实际值，JSON格式。支持传入多个参数，示例：[{"name":"张三","number":"15038****76"}]。
        self.template_params = template_params  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.out_ids is not None:
            result['OutIds'] = self.out_ids
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.sms_up_extend_codes is not None:
            result['SmsUpExtendCodes'] = self.sms_up_extend_codes
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OutIds') is not None:
            self.out_ids = m.get('OutIds')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SmsUpExtendCodes') is not None:
            self.sms_up_extend_codes = m.get('SmsUpExtendCodes')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        return self


class SendMessageResponseBodyDataMessages(TeaModel):
    def __init__(self, id=None, phone_number=None):
        # 短信Id。
        self.id = id  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBodyDataMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(self, messages=None, request_id=None):
        # 短信列表。
        self.messages = messages  # type: list[SendMessageResponseBodyDataMessages]
        # 请求Id。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendMessageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = SendMessageResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: SendMessageResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class SmsReportRequestBody(TeaModel):
    def __init__(self, biz_id=None, err_code=None, err_msg=None, message_id=None, out_id=None, phone_number=None,
                 report_time=None, request_id=None, send_time=None, sign_name=None, sms_size=None, success=None,
                 template_code=None):
        # 发送回执ID，即发送流水号。
        self.biz_id = biz_id  # type: str
        # 状态报告编码。
        self.err_code = err_code  # type: str
        # 状态报告说明。
        self.err_msg = err_msg  # type: str
        # 短信Id。调用发送接口SendMessage发送短信时，返回值中的Id字段。可使用短信Id在接口ListMessages查询具体的发送状态。
        self.message_id = message_id  # type: str
        # 外部拓展字段。
        self.out_id = out_id  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 状态报告时间。
        self.report_time = report_time  # type: str
        # 短信批处理Id。调用发送接口SendMessage发送短信时，返回值中的RequestId字段。可使用短信批处理Id在接口ListMessages查询具体的发送状态。
        self.request_id = request_id  # type: str
        # 发送时间。
        self.send_time = send_time  # type: str
        # 签名。
        self.sign_name = sign_name  # type: str
        # 短信长度。短信长度不超过70个字，按照一条短信计费；超过70个字，即为长短信，按照67字/条拆分成多条计费。
        self.sms_size = sms_size  # type: str
        # 是否接收成功。
        # - true : 接收成功。
        # - false : 接收失败。
        self.success = success  # type: bool
        # 模板号。
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsReportRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['biz_id'] = self.biz_id
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.err_msg is not None:
            result['err_msg'] = self.err_msg
        if self.message_id is not None:
            result['message_id'] = self.message_id
        if self.out_id is not None:
            result['out_id'] = self.out_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.report_time is not None:
            result['report_time'] = self.report_time
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        if self.sms_size is not None:
            result['sms_size'] = self.sms_size
        if self.success is not None:
            result['success'] = self.success
        if self.template_code is not None:
            result['template_code'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('biz_id') is not None:
            self.biz_id = m.get('biz_id')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')
        if m.get('message_id') is not None:
            self.message_id = m.get('message_id')
        if m.get('out_id') is not None:
            self.out_id = m.get('out_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('report_time') is not None:
            self.report_time = m.get('report_time')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        if m.get('sms_size') is not None:
            self.sms_size = m.get('sms_size')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('template_code') is not None:
            self.template_code = m.get('template_code')
        return self


class SmsReportRequest(TeaModel):
    def __init__(self, body=None):
        # 请求参数的主体信息。
        self.body = body  # type: list[SmsReportRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SmsReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsReportRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsReportResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        # 应答编码。
        self.code = code  # type: int
        # 描述信息。
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SmsReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsReportResponse, self).to_map()
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
            temp_model = SmsReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsUpRequestBody(TeaModel):
    def __init__(self, content=None, dest_code=None, phone_number=None, send_time=None, sequence_id=None,
                 sign_name=None):
        # 发送内容。
        self.content = content  # type: str
        # 上行短信扩展号码，系统后台自动生成，不支持自定义传入。
        self.dest_code = dest_code  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 发送时间。
        self.send_time = send_time  # type: str
        # 序列号。
        self.sequence_id = sequence_id  # type: int
        # 签名信息。
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsUpRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.dest_code is not None:
            result['dest_code'] = self.dest_code
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sequence_id is not None:
            result['sequence_id'] = self.sequence_id
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dest_code') is not None:
            self.dest_code = m.get('dest_code')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sequence_id') is not None:
            self.sequence_id = m.get('sequence_id')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        return self


class SmsUpRequest(TeaModel):
    def __init__(self, body=None):
        # 请求参数的主体信息。
        self.body = body  # type: list[SmsUpRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SmsUpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsUpRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsUpResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        # 应答编码。
        self.code = code  # type: int
        # 描述信息。
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsUpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsUpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SmsUpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsUpResponse, self).to_map()
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
            temp_model = SmsUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReportUrlRequest(TeaModel):
    def __init__(self, url=None):
        # 可公开访问的地址。
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReportUrlRequest, self).to_map()
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


class UpdateReportUrlResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReportUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateReportUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateReportUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateReportUrlResponse, self).to_map()
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
            temp_model = UpdateReportUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUploadUrlRequest(TeaModel):
    def __init__(self, url=None):
        # 可公开访问的地址。
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUploadUrlRequest, self).to_map()
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


class UpdateUploadUrlResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUploadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUploadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUploadUrlResponse, self).to_map()
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
            temp_model = UpdateUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


