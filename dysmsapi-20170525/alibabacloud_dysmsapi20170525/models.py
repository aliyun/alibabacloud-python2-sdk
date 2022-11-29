# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddShortUrlRequest(TeaModel):
    def __init__(self, effective_days=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 short_url_name=None, source_url=None):
        self.effective_days = effective_days  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.short_url_name = short_url_name  # type: str
        self.source_url = source_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShortUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_days is not None:
            result['EffectiveDays'] = self.effective_days
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.short_url_name is not None:
            result['ShortUrlName'] = self.short_url_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectiveDays') is not None:
            self.effective_days = m.get('EffectiveDays')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShortUrlName') is not None:
            self.short_url_name = m.get('ShortUrlName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class AddShortUrlResponseBodyData(TeaModel):
    def __init__(self, expire_date=None, short_url=None, source_url=None):
        self.expire_date = expire_date  # type: str
        self.short_url = short_url  # type: str
        self.source_url = source_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShortUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class AddShortUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AddShortUrlResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddShortUrlResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddShortUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddShortUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddShortUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddShortUrlResponse, self).to_map()
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
            temp_model = AddShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSmsSignRequestSignFileList(TeaModel):
    def __init__(self, file_contents=None, file_suffix=None):
        self.file_contents = file_contents  # type: str
        self.file_suffix = file_suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSmsSignRequestSignFileList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_contents is not None:
            result['FileContents'] = self.file_contents
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        return self


class AddSmsSignRequest(TeaModel):
    def __init__(self, owner_id=None, remark=None, resource_owner_account=None, resource_owner_id=None,
                 sign_file_list=None, sign_name=None, sign_source=None, sign_type=None):
        self.owner_id = owner_id  # type: long
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_file_list = sign_file_list  # type: list[AddSmsSignRequestSignFileList]
        self.sign_name = sign_name  # type: str
        self.sign_source = sign_source  # type: int
        self.sign_type = sign_type  # type: int

    def validate(self):
        if self.sign_file_list:
            for k in self.sign_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddSmsSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = AddSmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        return self


class AddSmsSignResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sign_name=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSmsSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class AddSmsSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSmsSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSmsSignResponse, self).to_map()
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
            temp_model = AddSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSmsTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, remark=None, resource_owner_account=None, resource_owner_id=None,
                 template_content=None, template_name=None, template_type=None):
        self.owner_id = owner_id  # type: long
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_content = template_content  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddSmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, template_code=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class AddSmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSmsTemplateResponse, self).to_map()
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
            temp_model = AddSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMobilesCardSupportRequest(TeaModel):
    def __init__(self, mobiles=None, template_code=None):
        self.mobiles = mobiles  # type: list[dict[str, any]]
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMobilesCardSupportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class CheckMobilesCardSupportResponseBodyDataQueryResult(TeaModel):
    def __init__(self, mobile=None, support=None):
        self.mobile = mobile  # type: str
        self.support = support  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMobilesCardSupportResponseBodyDataQueryResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.support is not None:
            result['support'] = self.support
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('support') is not None:
            self.support = m.get('support')
        return self


class CheckMobilesCardSupportResponseBodyData(TeaModel):
    def __init__(self, query_result=None):
        self.query_result = query_result  # type: list[CheckMobilesCardSupportResponseBodyDataQueryResult]

    def validate(self):
        if self.query_result:
            for k in self.query_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckMobilesCardSupportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['queryResult'] = []
        if self.query_result is not None:
            for k in self.query_result:
                result['queryResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.query_result = []
        if m.get('queryResult') is not None:
            for k in m.get('queryResult'):
                temp_model = CheckMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k))
        return self


class CheckMobilesCardSupportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CheckMobilesCardSupportResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckMobilesCardSupportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CheckMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckMobilesCardSupportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckMobilesCardSupportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckMobilesCardSupportResponse, self).to_map()
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
            temp_model = CheckMobilesCardSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCardSmsTemplateRequest(TeaModel):
    def __init__(self, factorys=None, memo=None, template=None, template_name=None):
        self.factorys = factorys  # type: str
        self.memo = memo  # type: str
        self.template = template  # type: dict[str, any]
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCardSmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factorys is not None:
            result['Factorys'] = self.factorys
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.template is not None:
            result['Template'] = self.template
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Factorys') is not None:
            self.factorys = m.get('Factorys')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateCardSmsTemplateShrinkRequest(TeaModel):
    def __init__(self, factorys=None, memo=None, template_shrink=None, template_name=None):
        self.factorys = factorys  # type: str
        self.memo = memo  # type: str
        self.template_shrink = template_shrink  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCardSmsTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factorys is not None:
            result['Factorys'] = self.factorys
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.template_shrink is not None:
            result['Template'] = self.template_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Factorys') is not None:
            self.factorys = m.get('Factorys')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Template') is not None:
            self.template_shrink = m.get('Template')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateCardSmsTemplateResponseBodyData(TeaModel):
    def __init__(self, template_code=None):
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCardSmsTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class CreateCardSmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateCardSmsTemplateResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateCardSmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CreateCardSmsTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCardSmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCardSmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCardSmsTemplateResponse, self).to_map()
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
            temp_model = CreateCardSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShortUrlRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, source_url=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.source_url = source_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteShortUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class DeleteShortUrlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteShortUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteShortUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteShortUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteShortUrlResponse, self).to_map()
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
            temp_model = DeleteShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsSignRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, sign_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmsSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteSmsSignResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sign_name=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmsSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteSmsSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSmsSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSmsSignResponse, self).to_map()
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
            temp_model = DeleteSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, template_code=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteSmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, template_code=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteSmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSmsTemplateResponse, self).to_map()
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
            temp_model = DeleteSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardSmsLinkRequest(TeaModel):
    def __init__(self, card_code_type=None, card_link_type=None, card_template_code=None,
                 card_template_param_json=None, custom_short_code_json=None, domain=None, out_id=None, phone_number_json=None,
                 sign_name_json=None):
        self.card_code_type = card_code_type  # type: int
        self.card_link_type = card_link_type  # type: int
        self.card_template_code = card_template_code  # type: str
        self.card_template_param_json = card_template_param_json  # type: str
        self.custom_short_code_json = custom_short_code_json  # type: str
        self.domain = domain  # type: str
        self.out_id = out_id  # type: str
        self.phone_number_json = phone_number_json  # type: str
        self.sign_name_json = sign_name_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardSmsLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_code_type is not None:
            result['CardCodeType'] = self.card_code_type
        if self.card_link_type is not None:
            result['CardLinkType'] = self.card_link_type
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json
        if self.custom_short_code_json is not None:
            result['CustomShortCodeJson'] = self.custom_short_code_json
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardCodeType') is not None:
            self.card_code_type = m.get('CardCodeType')
        if m.get('CardLinkType') is not None:
            self.card_link_type = m.get('CardLinkType')
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')
        if m.get('CustomShortCodeJson') is not None:
            self.custom_short_code_json = m.get('CustomShortCodeJson')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        return self


class GetCardSmsLinkResponseBodyData(TeaModel):
    def __init__(self, card_phone_numbers=None, card_sign_names=None, card_sms_links=None, card_tmp_state=None,
                 not_media_mobiles=None):
        self.card_phone_numbers = card_phone_numbers  # type: str
        self.card_sign_names = card_sign_names  # type: str
        self.card_sms_links = card_sms_links  # type: str
        self.card_tmp_state = card_tmp_state  # type: int
        self.not_media_mobiles = not_media_mobiles  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardSmsLinkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_phone_numbers is not None:
            result['CardPhoneNumbers'] = self.card_phone_numbers
        if self.card_sign_names is not None:
            result['CardSignNames'] = self.card_sign_names
        if self.card_sms_links is not None:
            result['CardSmsLinks'] = self.card_sms_links
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardPhoneNumbers') is not None:
            self.card_phone_numbers = m.get('CardPhoneNumbers')
        if m.get('CardSignNames') is not None:
            self.card_sign_names = m.get('CardSignNames')
        if m.get('CardSmsLinks') is not None:
            self.card_sms_links = m.get('CardSmsLinks')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class GetCardSmsLinkResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCardSmsLinkResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCardSmsLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetCardSmsLinkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardSmsLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCardSmsLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardSmsLinkResponse, self).to_map()
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
            temp_model = GetCardSmsLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaResourceIdRequest(TeaModel):
    def __init__(self, extend_info=None, file_size=None, memo=None, oss_key=None, resource_type=None):
        self.extend_info = extend_info  # type: str
        self.file_size = file_size  # type: long
        self.memo = memo  # type: str
        self.oss_key = oss_key  # type: str
        self.resource_type = resource_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaResourceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetMediaResourceIdResponseBodyData(TeaModel):
    def __init__(self, res_url_download=None, resource_id=None):
        self.res_url_download = res_url_download  # type: str
        self.resource_id = resource_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaResourceIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_url_download is not None:
            result['ResUrlDownload'] = self.res_url_download
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResUrlDownload') is not None:
            self.res_url_download = m.get('ResUrlDownload')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetMediaResourceIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetMediaResourceIdResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMediaResourceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetMediaResourceIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMediaResourceIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaResourceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaResourceIdResponse, self).to_map()
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
            temp_model = GetMediaResourceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSInfoForCardTemplateResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, ali_uid=None, bucket=None, expire_time=None, host=None, policy=None,
                 signature=None, start_path=None):
        self.access_key_id = access_key_id  # type: str
        self.ali_uid = ali_uid  # type: str
        self.bucket = bucket  # type: str
        self.expire_time = expire_time  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str
        self.start_path = start_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOSSInfoForCardTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.start_path is not None:
            result['StartPath'] = self.start_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartPath') is not None:
            self.start_path = m.get('StartPath')
        return self


class GetOSSInfoForCardTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetOSSInfoForCardTemplateResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOSSInfoForCardTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetOSSInfoForCardTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOSSInfoForCardTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOSSInfoForCardTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOSSInfoForCardTemplateResponse, self).to_map()
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
            temp_model = GetOSSInfoForCardTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, owner_id=None, page_size=None, prod_code=None, region_id=None,
                 resource_id=None, resource_owner_account=None, resource_owner_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.owner_id = owner_id  # type: long
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, next_token=None, request_id=None, tag_resources=None):
        self.code = code  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmsSignRequestSignFileList(TeaModel):
    def __init__(self, file_contents=None, file_suffix=None):
        self.file_contents = file_contents  # type: str
        self.file_suffix = file_suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmsSignRequestSignFileList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_contents is not None:
            result['FileContents'] = self.file_contents
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        return self


class ModifySmsSignRequest(TeaModel):
    def __init__(self, owner_id=None, remark=None, resource_owner_account=None, resource_owner_id=None,
                 sign_file_list=None, sign_name=None, sign_source=None, sign_type=None):
        self.owner_id = owner_id  # type: long
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_file_list = sign_file_list  # type: list[ModifySmsSignRequestSignFileList]
        self.sign_name = sign_name  # type: str
        self.sign_source = sign_source  # type: int
        self.sign_type = sign_type  # type: int

    def validate(self):
        if self.sign_file_list:
            for k in self.sign_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifySmsSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = ModifySmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        return self


class ModifySmsSignResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sign_name=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmsSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class ModifySmsSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySmsSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySmsSignResponse, self).to_map()
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
            temp_model = ModifySmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmsTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, remark=None, resource_owner_account=None, resource_owner_id=None,
                 template_code=None, template_content=None, template_name=None, template_type=None):
        self.owner_id = owner_id  # type: long
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_code = template_code  # type: str
        self.template_content = template_content  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifySmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, template_code=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class ModifySmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySmsTemplateResponse, self).to_map()
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
            temp_model = ModifySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardSmsTemplateRequest(TeaModel):
    def __init__(self, template_code=None):
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCardSmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryCardSmsTemplateResponseBodyData(TeaModel):
    def __init__(self, templates=None):
        self.templates = templates  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCardSmsTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class QueryCardSmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCardSmsTemplateResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCardSmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCardSmsTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCardSmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCardSmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCardSmsTemplateResponse, self).to_map()
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
            temp_model = QueryCardSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardSmsTemplateReportRequest(TeaModel):
    def __init__(self, end_date=None, start_date=None, template_codes=None):
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.template_codes = template_codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCardSmsTemplateReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_codes is not None:
            result['TemplateCodes'] = self.template_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateCodes') is not None:
            self.template_codes = m.get('TemplateCodes')
        return self


class QueryCardSmsTemplateReportResponseBodyData(TeaModel):
    def __init__(self, model=None):
        self.model = model  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCardSmsTemplateReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['model'] = self.model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')
        return self


class QueryCardSmsTemplateReportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCardSmsTemplateReportResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCardSmsTemplateReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCardSmsTemplateReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCardSmsTemplateReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCardSmsTemplateReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCardSmsTemplateReportResponse, self).to_map()
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
            temp_model = QueryCardSmsTemplateReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMobilesCardSupportRequest(TeaModel):
    def __init__(self, mobiles=None, template_code=None):
        self.mobiles = mobiles  # type: list[dict[str, any]]
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMobilesCardSupportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryMobilesCardSupportShrinkRequest(TeaModel):
    def __init__(self, mobiles_shrink=None, template_code=None):
        self.mobiles_shrink = mobiles_shrink  # type: str
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMobilesCardSupportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryMobilesCardSupportResponseBodyDataQueryResult(TeaModel):
    def __init__(self, mobile=None, support=None):
        self.mobile = mobile  # type: str
        self.support = support  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMobilesCardSupportResponseBodyDataQueryResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.support is not None:
            result['Support'] = self.support
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        return self


class QueryMobilesCardSupportResponseBodyData(TeaModel):
    def __init__(self, query_result=None):
        self.query_result = query_result  # type: list[QueryMobilesCardSupportResponseBodyDataQueryResult]

    def validate(self):
        if self.query_result:
            for k in self.query_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMobilesCardSupportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueryResult'] = []
        if self.query_result is not None:
            for k in self.query_result:
                result['QueryResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.query_result = []
        if m.get('QueryResult') is not None:
            for k in m.get('QueryResult'):
                temp_model = QueryMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k))
        return self


class QueryMobilesCardSupportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryMobilesCardSupportResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMobilesCardSupportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMobilesCardSupportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMobilesCardSupportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMobilesCardSupportResponse, self).to_map()
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
            temp_model = QueryMobilesCardSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendDetailsRequest(TeaModel):
    def __init__(self, biz_id=None, current_page=None, owner_id=None, page_size=None, phone_number=None,
                 resource_owner_account=None, resource_owner_id=None, send_date=None):
        self.biz_id = biz_id  # type: str
        self.current_page = current_page  # type: long
        self.owner_id = owner_id  # type: long
        self.page_size = page_size  # type: long
        self.phone_number = phone_number  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.send_date = send_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySendDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        return self


class QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO(TeaModel):
    def __init__(self, content=None, err_code=None, out_id=None, phone_num=None, receive_date=None, send_date=None,
                 send_status=None, template_code=None):
        self.content = content  # type: str
        self.err_code = err_code  # type: str
        self.out_id = out_id  # type: str
        self.phone_num = phone_num  # type: str
        self.receive_date = receive_date  # type: str
        self.send_date = send_date  # type: str
        self.send_status = send_status  # type: long
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QuerySendDetailsResponseBodySmsSendDetailDTOs(TeaModel):
    def __init__(self, sms_send_detail_dto=None):
        self.sms_send_detail_dto = sms_send_detail_dto  # type: list[QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO]

    def validate(self):
        if self.sms_send_detail_dto:
            for k in self.sms_send_detail_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySendDetailsResponseBodySmsSendDetailDTOs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SmsSendDetailDTO'] = []
        if self.sms_send_detail_dto is not None:
            for k in self.sms_send_detail_dto:
                result['SmsSendDetailDTO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sms_send_detail_dto = []
        if m.get('SmsSendDetailDTO') is not None:
            for k in m.get('SmsSendDetailDTO'):
                temp_model = QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO()
                self.sms_send_detail_dto.append(temp_model.from_map(k))
        return self


class QuerySendDetailsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sms_send_detail_dtos=None, total_count=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.sms_send_detail_dtos = sms_send_detail_dtos  # type: QuerySendDetailsResponseBodySmsSendDetailDTOs
        self.total_count = total_count  # type: str

    def validate(self):
        if self.sms_send_detail_dtos:
            self.sms_send_detail_dtos.validate()

    def to_map(self):
        _map = super(QuerySendDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sms_send_detail_dtos is not None:
            result['SmsSendDetailDTOs'] = self.sms_send_detail_dtos.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmsSendDetailDTOs') is not None:
            temp_model = QuerySendDetailsResponseBodySmsSendDetailDTOs()
            self.sms_send_detail_dtos = temp_model.from_map(m['SmsSendDetailDTOs'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySendDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySendDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySendDetailsResponse, self).to_map()
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
            temp_model = QuerySendDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendStatisticsRequest(TeaModel):
    def __init__(self, end_date=None, is_globe=None, owner_id=None, page_index=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, sign_name=None, start_date=None, template_type=None):
        self.end_date = end_date  # type: str
        self.is_globe = is_globe  # type: int
        self.owner_id = owner_id  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_name = sign_name  # type: str
        self.start_date = start_date  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySendStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.is_globe is not None:
            result['IsGlobe'] = self.is_globe
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IsGlobe') is not None:
            self.is_globe = m.get('IsGlobe')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySendStatisticsResponseBodyDataTargetList(TeaModel):
    def __init__(self, no_responded_count=None, responded_fail_count=None, responded_success_count=None,
                 send_date=None, total_count=None):
        self.no_responded_count = no_responded_count  # type: long
        self.responded_fail_count = responded_fail_count  # type: long
        self.responded_success_count = responded_success_count  # type: long
        self.send_date = send_date  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySendStatisticsResponseBodyDataTargetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no_responded_count is not None:
            result['NoRespondedCount'] = self.no_responded_count
        if self.responded_fail_count is not None:
            result['RespondedFailCount'] = self.responded_fail_count
        if self.responded_success_count is not None:
            result['RespondedSuccessCount'] = self.responded_success_count
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NoRespondedCount') is not None:
            self.no_responded_count = m.get('NoRespondedCount')
        if m.get('RespondedFailCount') is not None:
            self.responded_fail_count = m.get('RespondedFailCount')
        if m.get('RespondedSuccessCount') is not None:
            self.responded_success_count = m.get('RespondedSuccessCount')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySendStatisticsResponseBodyData(TeaModel):
    def __init__(self, target_list=None, total_size=None):
        self.target_list = target_list  # type: list[QuerySendStatisticsResponseBodyDataTargetList]
        self.total_size = total_size  # type: long

    def validate(self):
        if self.target_list:
            for k in self.target_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySendStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetList'] = []
        if self.target_list is not None:
            for k in self.target_list:
                result['TargetList'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.target_list = []
        if m.get('TargetList') is not None:
            for k in m.get('TargetList'):
                temp_model = QuerySendStatisticsResponseBodyDataTargetList()
                self.target_list.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class QuerySendStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QuerySendStatisticsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QuerySendStatisticsResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QuerySendStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySendStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySendStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySendStatisticsResponse, self).to_map()
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
            temp_model = QuerySendStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShortUrlRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, short_url=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.short_url = short_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryShortUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class QueryShortUrlResponseBodyData(TeaModel):
    def __init__(self, create_date=None, expire_date=None, page_view_count=None, short_url=None,
                 short_url_name=None, short_url_status=None, source_url=None, unique_visitor_count=None):
        self.create_date = create_date  # type: str
        self.expire_date = expire_date  # type: str
        self.page_view_count = page_view_count  # type: str
        self.short_url = short_url  # type: str
        self.short_url_name = short_url_name  # type: str
        self.short_url_status = short_url_status  # type: str
        self.source_url = source_url  # type: str
        self.unique_visitor_count = unique_visitor_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryShortUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.page_view_count is not None:
            result['PageViewCount'] = self.page_view_count
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.short_url_name is not None:
            result['ShortUrlName'] = self.short_url_name
        if self.short_url_status is not None:
            result['ShortUrlStatus'] = self.short_url_status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.unique_visitor_count is not None:
            result['UniqueVisitorCount'] = self.unique_visitor_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('PageViewCount') is not None:
            self.page_view_count = m.get('PageViewCount')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('ShortUrlName') is not None:
            self.short_url_name = m.get('ShortUrlName')
        if m.get('ShortUrlStatus') is not None:
            self.short_url_status = m.get('ShortUrlStatus')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('UniqueVisitorCount') is not None:
            self.unique_visitor_count = m.get('UniqueVisitorCount')
        return self


class QueryShortUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryShortUrlResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryShortUrlResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryShortUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryShortUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryShortUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryShortUrlResponse, self).to_map()
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
            temp_model = QueryShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsSignRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, sign_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QuerySmsSignResponseBody(TeaModel):
    def __init__(self, code=None, create_date=None, message=None, reason=None, request_id=None, sign_name=None,
                 sign_status=None):
        self.code = code  # type: str
        self.create_date = create_date  # type: str
        self.message = message  # type: str
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str
        self.sign_name = sign_name  # type: str
        self.sign_status = sign_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')
        return self


class QuerySmsSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySmsSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySmsSignResponse, self).to_map()
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
            temp_model = QuerySmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsSignListRequest(TeaModel):
    def __init__(self, owner_id=None, page_index=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsSignListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySmsSignListResponseBodySmsSignListReason(TeaModel):
    def __init__(self, reject_date=None, reject_info=None, reject_sub_info=None):
        self.reject_date = reject_date  # type: str
        self.reject_info = reject_info  # type: str
        self.reject_sub_info = reject_sub_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsSignListResponseBodySmsSignListReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')
        return self


class QuerySmsSignListResponseBodySmsSignList(TeaModel):
    def __init__(self, audit_status=None, business_type=None, create_date=None, order_id=None, reason=None,
                 sign_name=None):
        self.audit_status = audit_status  # type: str
        self.business_type = business_type  # type: str
        self.create_date = create_date  # type: str
        self.order_id = order_id  # type: str
        self.reason = reason  # type: QuerySmsSignListResponseBodySmsSignListReason
        self.sign_name = sign_name  # type: str

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super(QuerySmsSignListResponseBodySmsSignList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Reason') is not None:
            temp_model = QuerySmsSignListResponseBodySmsSignListReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QuerySmsSignListResponseBody(TeaModel):
    def __init__(self, code=None, current_page=None, message=None, page_size=None, request_id=None,
                 sms_sign_list=None, total_count=None):
        self.code = code  # type: str
        self.current_page = current_page  # type: int
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.sms_sign_list = sms_sign_list  # type: list[QuerySmsSignListResponseBodySmsSignList]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.sms_sign_list:
            for k in self.sms_sign_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySmsSignListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsSignList'] = []
        if self.sms_sign_list is not None:
            for k in self.sms_sign_list:
                result['SmsSignList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_sign_list = []
        if m.get('SmsSignList') is not None:
            for k in m.get('SmsSignList'):
                temp_model = QuerySmsSignListResponseBodySmsSignList()
                self.sms_sign_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySmsSignListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySmsSignListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySmsSignListResponse, self).to_map()
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
            temp_model = QuerySmsSignListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, template_code=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QuerySmsTemplateResponseBody(TeaModel):
    def __init__(self, code=None, create_date=None, message=None, reason=None, request_id=None, template_code=None,
                 template_content=None, template_name=None, template_status=None, template_type=None):
        self.code = code  # type: str
        self.create_date = create_date  # type: str
        self.message = message  # type: str
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str
        self.template_code = template_code  # type: str
        self.template_content = template_content  # type: str
        self.template_name = template_name  # type: str
        self.template_status = template_status  # type: int
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySmsTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySmsTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySmsTemplateResponse, self).to_map()
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
            temp_model = QuerySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsTemplateListRequest(TeaModel):
    def __init__(self, owner_id=None, page_index=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySmsTemplateListResponseBodySmsTemplateListReason(TeaModel):
    def __init__(self, reject_date=None, reject_info=None, reject_sub_info=None):
        self.reject_date = reject_date  # type: str
        self.reject_info = reject_info  # type: str
        self.reject_sub_info = reject_sub_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySmsTemplateListResponseBodySmsTemplateListReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')
        return self


class QuerySmsTemplateListResponseBodySmsTemplateList(TeaModel):
    def __init__(self, audit_status=None, create_date=None, order_id=None, outer_template_type=None, reason=None,
                 template_code=None, template_content=None, template_name=None, template_type=None):
        self.audit_status = audit_status  # type: str
        self.create_date = create_date  # type: str
        self.order_id = order_id  # type: str
        self.outer_template_type = outer_template_type  # type: int
        self.reason = reason  # type: QuerySmsTemplateListResponseBodySmsTemplateListReason
        self.template_code = template_code  # type: str
        self.template_content = template_content  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super(QuerySmsTemplateListResponseBodySmsTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.outer_template_type is not None:
            result['OuterTemplateType'] = self.outer_template_type
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OuterTemplateType') is not None:
            self.outer_template_type = m.get('OuterTemplateType')
        if m.get('Reason') is not None:
            temp_model = QuerySmsTemplateListResponseBodySmsTemplateListReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySmsTemplateListResponseBody(TeaModel):
    def __init__(self, code=None, current_page=None, message=None, page_size=None, request_id=None,
                 sms_template_list=None, total_count=None):
        self.code = code  # type: str
        self.current_page = current_page  # type: int
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.sms_template_list = sms_template_list  # type: list[QuerySmsTemplateListResponseBodySmsTemplateList]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.sms_template_list:
            for k in self.sms_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySmsTemplateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsTemplateList'] = []
        if self.sms_template_list is not None:
            for k in self.sms_template_list:
                result['SmsTemplateList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_template_list = []
        if m.get('SmsTemplateList') is not None:
            for k in m.get('SmsTemplateList'):
                temp_model = QuerySmsTemplateListResponseBodySmsTemplateList()
                self.sms_template_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySmsTemplateListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySmsTemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySmsTemplateListResponse, self).to_map()
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
            temp_model = QuerySmsTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchCardSmsRequest(TeaModel):
    def __init__(self, card_template_code=None, card_template_param_json=None, digital_template_code=None,
                 digital_template_param_json=None, fallback_type=None, out_id=None, phone_number_json=None, sign_name_json=None,
                 sms_template_code=None, sms_template_param_json=None, sms_up_extend_code_json=None, template_code=None,
                 template_param_json=None):
        self.card_template_code = card_template_code  # type: str
        self.card_template_param_json = card_template_param_json  # type: str
        self.digital_template_code = digital_template_code  # type: str
        self.digital_template_param_json = digital_template_param_json  # type: str
        self.fallback_type = fallback_type  # type: str
        self.out_id = out_id  # type: str
        self.phone_number_json = phone_number_json  # type: str
        self.sign_name_json = sign_name_json  # type: str
        self.sms_template_code = sms_template_code  # type: str
        self.sms_template_param_json = sms_template_param_json  # type: str
        self.sms_up_extend_code_json = sms_up_extend_code_json  # type: str
        self.template_code = template_code  # type: str
        self.template_param_json = template_param_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendBatchCardSmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json
        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code
        if self.digital_template_param_json is not None:
            result['DigitalTemplateParamJson'] = self.digital_template_param_json
        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param_json is not None:
            result['SmsTemplateParamJson'] = self.sms_template_param_json
        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')
        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')
        if m.get('DigitalTemplateParamJson') is not None:
            self.digital_template_param_json = m.get('DigitalTemplateParamJson')
        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParamJson') is not None:
            self.sms_template_param_json = m.get('SmsTemplateParamJson')
        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        return self


class SendBatchCardSmsResponseBodyData(TeaModel):
    def __init__(self, biz_card_id=None, biz_digital_id=None, biz_sms_id=None, card_tmp_state=None,
                 media_mobiles=None, not_media_mobiles=None):
        self.biz_card_id = biz_card_id  # type: str
        self.biz_digital_id = biz_digital_id  # type: str
        self.biz_sms_id = biz_sms_id  # type: str
        self.card_tmp_state = card_tmp_state  # type: int
        self.media_mobiles = media_mobiles  # type: str
        self.not_media_mobiles = not_media_mobiles  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendBatchCardSmsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id
        if self.biz_digital_id is not None:
            result['BizDigitalId'] = self.biz_digital_id
        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.media_mobiles is not None:
            result['MediaMobiles'] = self.media_mobiles
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')
        if m.get('BizDigitalId') is not None:
            self.biz_digital_id = m.get('BizDigitalId')
        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('MediaMobiles') is not None:
            self.media_mobiles = m.get('MediaMobiles')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class SendBatchCardSmsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendBatchCardSmsResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendBatchCardSmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SendBatchCardSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendBatchCardSmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendBatchCardSmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendBatchCardSmsResponse, self).to_map()
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
            temp_model = SendBatchCardSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchSmsRequest(TeaModel):
    def __init__(self, out_id=None, owner_id=None, phone_number_json=None, resource_owner_account=None,
                 resource_owner_id=None, sign_name_json=None, sms_up_extend_code_json=None, template_code=None,
                 template_param_json=None):
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_number_json = phone_number_json  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_name_json = sign_name_json  # type: str
        self.sms_up_extend_code_json = sms_up_extend_code_json  # type: str
        self.template_code = template_code  # type: str
        self.template_param_json = template_param_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendBatchSmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        return self


class SendBatchSmsResponseBody(TeaModel):
    def __init__(self, biz_id=None, code=None, message=None, request_id=None):
        self.biz_id = biz_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendBatchSmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendBatchSmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendBatchSmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendBatchSmsResponse, self).to_map()
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
            temp_model = SendBatchSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCardSmsRequestCardObjects(TeaModel):
    def __init__(self, custom_url=None, dync_params=None, mobile=None):
        self.custom_url = custom_url  # type: str
        self.dync_params = dync_params  # type: str
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCardSmsRequestCardObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_url is not None:
            result['customUrl'] = self.custom_url
        if self.dync_params is not None:
            result['dyncParams'] = self.dync_params
        if self.mobile is not None:
            result['mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('customUrl') is not None:
            self.custom_url = m.get('customUrl')
        if m.get('dyncParams') is not None:
            self.dync_params = m.get('dyncParams')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        return self


class SendCardSmsRequest(TeaModel):
    def __init__(self, card_objects=None, card_template_code=None, digital_template_code=None,
                 digital_template_param=None, fallback_type=None, out_id=None, sign_name=None, sms_template_code=None,
                 sms_template_param=None, sms_up_extend_code=None, template_code=None, template_param=None):
        self.card_objects = card_objects  # type: list[SendCardSmsRequestCardObjects]
        self.card_template_code = card_template_code  # type: str
        self.digital_template_code = digital_template_code  # type: str
        self.digital_template_param = digital_template_param  # type: str
        self.fallback_type = fallback_type  # type: str
        self.out_id = out_id  # type: str
        self.sign_name = sign_name  # type: str
        self.sms_template_code = sms_template_code  # type: str
        self.sms_template_param = sms_template_param  # type: str
        self.sms_up_extend_code = sms_up_extend_code  # type: str
        self.template_code = template_code  # type: str
        self.template_param = template_param  # type: str

    def validate(self):
        if self.card_objects:
            for k in self.card_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendCardSmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardObjects'] = []
        if self.card_objects is not None:
            for k in self.card_objects:
                result['CardObjects'].append(k.to_map() if k else None)
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code
        if self.digital_template_param is not None:
            result['DigitalTemplateParam'] = self.digital_template_param
        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.card_objects = []
        if m.get('CardObjects') is not None:
            for k in m.get('CardObjects'):
                temp_model = SendCardSmsRequestCardObjects()
                self.card_objects.append(temp_model.from_map(k))
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')
        if m.get('DigitalTemplateParam') is not None:
            self.digital_template_param = m.get('DigitalTemplateParam')
        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendCardSmsResponseBodyData(TeaModel):
    def __init__(self, biz_card_id=None, biz_digital_id=None, biz_sms_id=None, card_tmp_state=None,
                 media_mobiles=None, not_media_mobiles=None):
        self.biz_card_id = biz_card_id  # type: str
        self.biz_digital_id = biz_digital_id  # type: str
        self.biz_sms_id = biz_sms_id  # type: str
        self.card_tmp_state = card_tmp_state  # type: int
        self.media_mobiles = media_mobiles  # type: str
        self.not_media_mobiles = not_media_mobiles  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCardSmsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id
        if self.biz_digital_id is not None:
            result['BizDigitalId'] = self.biz_digital_id
        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.media_mobiles is not None:
            result['MediaMobiles'] = self.media_mobiles
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')
        if m.get('BizDigitalId') is not None:
            self.biz_digital_id = m.get('BizDigitalId')
        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('MediaMobiles') is not None:
            self.media_mobiles = m.get('MediaMobiles')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class SendCardSmsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendCardSmsResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendCardSmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SendCardSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendCardSmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCardSmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCardSmsResponse, self).to_map()
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
            temp_model = SendCardSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSmsRequest(TeaModel):
    def __init__(self, out_id=None, owner_id=None, phone_numbers=None, resource_owner_account=None,
                 resource_owner_id=None, sign_name=None, sms_up_extend_code=None, template_code=None, template_param=None):
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_numbers = phone_numbers  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sign_name = sign_name  # type: str
        self.sms_up_extend_code = sms_up_extend_code  # type: str
        self.template_code = template_code  # type: str
        self.template_param = template_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendSmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendSmsResponseBody(TeaModel):
    def __init__(self, biz_id=None, code=None, message=None, request_id=None):
        self.biz_id = biz_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendSmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendSmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendSmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendSmsResponse, self).to_map()
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
            temp_model = SendSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, region_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_id=None, prod_code=None, region_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


