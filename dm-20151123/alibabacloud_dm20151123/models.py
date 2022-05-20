# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddIpfilterRequest(TeaModel):
    def __init__(self, ip_address=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.ip_address = ip_address  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpfilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AddIpfilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpfilterResponseBody, self).to_map()
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


class AddIpfilterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIpfilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIpfilterResponse, self).to_map()
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
            temp_model = AddIpfilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveReplyMailAddressRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, ticket=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveReplyMailAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class ApproveReplyMailAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveReplyMailAddressResponseBody, self).to_map()
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


class ApproveReplyMailAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApproveReplyMailAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApproveReplyMailAddressResponse, self).to_map()
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
            temp_model = ApproveReplyMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendMailRequest(TeaModel):
    def __init__(self, account_name=None, address_type=None, click_trace=None, owner_id=None, receivers_name=None,
                 reply_address=None, reply_address_alias=None, resource_owner_account=None, resource_owner_id=None,
                 tag_name=None, template_name=None):
        self.account_name = account_name  # type: str
        self.address_type = address_type  # type: int
        self.click_trace = click_trace  # type: str
        self.owner_id = owner_id  # type: long
        self.receivers_name = receivers_name  # type: str
        self.reply_address = reply_address  # type: str
        self.reply_address_alias = reply_address_alias  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_name = tag_name  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSendMailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class BatchSendMailResponseBody(TeaModel):
    def __init__(self, env_id=None, request_id=None):
        self.env_id = env_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSendMailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSendMailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchSendMailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSendMailResponse, self).to_map()
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
            temp_model = BatchSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(self, domain_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.domain_id = domain_id  # type: int
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(self, domain_status=None, request_id=None):
        self.domain_status = domain_status  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDomainResponse, self).to_map()
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
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckReplyToMailAddressRequest(TeaModel):
    def __init__(self, lang=None, mail_address_id=None, owner_id=None, region=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.lang = lang  # type: str
        self.mail_address_id = mail_address_id  # type: int
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckReplyToMailAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckReplyToMailAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckReplyToMailAddressResponseBody, self).to_map()
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


class CheckReplyToMailAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckReplyToMailAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckReplyToMailAddressResponse, self).to_map()
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
            temp_model = CheckReplyToMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(self, domain_id=None, request_id=None):
        self.domain_id = domain_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainResponse, self).to_map()
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMailAddressRequest(TeaModel):
    def __init__(self, account_name=None, owner_id=None, reply_address=None, resource_owner_account=None,
                 resource_owner_id=None, sendtype=None):
        self.account_name = account_name  # type: str
        self.owner_id = owner_id  # type: long
        self.reply_address = reply_address  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sendtype = sendtype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMailAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class CreateMailAddressResponseBody(TeaModel):
    def __init__(self, mail_address_id=None, request_id=None):
        self.mail_address_id = mail_address_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMailAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMailAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMailAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMailAddressResponse, self).to_map()
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
            temp_model = CreateMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReceiverRequest(TeaModel):
    def __init__(self, desc=None, owner_id=None, receivers_alias=None, receivers_name=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.desc = desc  # type: str
        self.owner_id = owner_id  # type: long
        self.receivers_alias = receivers_alias  # type: str
        self.receivers_name = receivers_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReceiverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateReceiverResponseBody(TeaModel):
    def __init__(self, receiver_id=None, request_id=None):
        self.receiver_id = receiver_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReceiverResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateReceiverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateReceiverResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReceiverResponse, self).to_map()
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
            temp_model = CreateReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, tag_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_id=None):
        self.request_id = request_id  # type: str
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class CreateTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagResponse, self).to_map()
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, domain_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.domain_id = domain_id  # type: int
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResponseBody, self).to_map()
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


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainResponse, self).to_map()
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpfilterByEdmIdRequest(TeaModel):
    def __init__(self, from_type=None, id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.from_type = from_type  # type: int
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpfilterByEdmIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpfilterByEdmIdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpfilterByEdmIdResponseBody, self).to_map()
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


class DeleteIpfilterByEdmIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIpfilterByEdmIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpfilterByEdmIdResponse, self).to_map()
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
            temp_model = DeleteIpfilterByEdmIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMailAddressRequest(TeaModel):
    def __init__(self, mail_address_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.mail_address_id = mail_address_id  # type: int
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMailAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteMailAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMailAddressResponseBody, self).to_map()
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


class DeleteMailAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMailAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMailAddressResponse, self).to_map()
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
            temp_model = DeleteMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverRequest(TeaModel):
    def __init__(self, owner_id=None, receiver_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.receiver_id = receiver_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReceiverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteReceiverResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReceiverResponseBody, self).to_map()
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


class DeleteReceiverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteReceiverResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteReceiverResponse, self).to_map()
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
            temp_model = DeleteReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverDetailRequest(TeaModel):
    def __init__(self, email=None, owner_id=None, receiver_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.email = email  # type: str
        self.owner_id = owner_id  # type: long
        self.receiver_id = receiver_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReceiverDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteReceiverDetailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReceiverDetailResponseBody, self).to_map()
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


class DeleteReceiverDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteReceiverDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteReceiverDetailResponse, self).to_map()
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
            temp_model = DeleteReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, tag_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_id = tag_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeleteTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagResponseBody, self).to_map()
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


class DeleteTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagResponse, self).to_map()
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescAccountSummaryRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescAccountSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescAccountSummaryResponseBody(TeaModel):
    def __init__(self, daily_quota=None, dayu_status=None, domains=None, enable_times=None, mail_addresses=None,
                 max_quota_level=None, month_quota=None, quota_level=None, receivers=None, request_id=None, sms_record=None,
                 sms_sign=None, sms_templates=None, tags=None, templates=None, user_status=None):
        self.daily_quota = daily_quota  # type: int
        self.dayu_status = dayu_status  # type: int
        self.domains = domains  # type: int
        self.enable_times = enable_times  # type: int
        self.mail_addresses = mail_addresses  # type: int
        self.max_quota_level = max_quota_level  # type: int
        self.month_quota = month_quota  # type: int
        self.quota_level = quota_level  # type: int
        self.receivers = receivers  # type: int
        self.request_id = request_id  # type: str
        self.sms_record = sms_record  # type: int
        self.sms_sign = sms_sign  # type: int
        self.sms_templates = sms_templates  # type: int
        self.tags = tags  # type: int
        self.templates = templates  # type: int
        self.user_status = user_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescAccountSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_quota is not None:
            result['DailyQuota'] = self.daily_quota
        if self.dayu_status is not None:
            result['DayuStatus'] = self.dayu_status
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.enable_times is not None:
            result['EnableTimes'] = self.enable_times
        if self.mail_addresses is not None:
            result['MailAddresses'] = self.mail_addresses
        if self.max_quota_level is not None:
            result['MaxQuotaLevel'] = self.max_quota_level
        if self.month_quota is not None:
            result['MonthQuota'] = self.month_quota
        if self.quota_level is not None:
            result['QuotaLevel'] = self.quota_level
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sms_record is not None:
            result['SmsRecord'] = self.sms_record
        if self.sms_sign is not None:
            result['SmsSign'] = self.sms_sign
        if self.sms_templates is not None:
            result['SmsTemplates'] = self.sms_templates
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.templates is not None:
            result['Templates'] = self.templates
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DailyQuota') is not None:
            self.daily_quota = m.get('DailyQuota')
        if m.get('DayuStatus') is not None:
            self.dayu_status = m.get('DayuStatus')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('EnableTimes') is not None:
            self.enable_times = m.get('EnableTimes')
        if m.get('MailAddresses') is not None:
            self.mail_addresses = m.get('MailAddresses')
        if m.get('MaxQuotaLevel') is not None:
            self.max_quota_level = m.get('MaxQuotaLevel')
        if m.get('MonthQuota') is not None:
            self.month_quota = m.get('MonthQuota')
        if m.get('QuotaLevel') is not None:
            self.quota_level = m.get('QuotaLevel')
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmsRecord') is not None:
            self.sms_record = m.get('SmsRecord')
        if m.get('SmsSign') is not None:
            self.sms_sign = m.get('SmsSign')
        if m.get('SmsTemplates') is not None:
            self.sms_templates = m.get('SmsTemplates')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class DescAccountSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescAccountSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescAccountSummaryResponse, self).to_map()
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
            temp_model = DescAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescDomainRequest(TeaModel):
    def __init__(self, domain_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.domain_id = domain_id  # type: int
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescDomainResponseBody(TeaModel):
    def __init__(self, cname_auth_status=None, cname_confirm_status=None, cname_record=None, create_time=None,
                 default_domain=None, dns_mx=None, dns_spf=None, dns_txt=None, domain_id=None, domain_name=None, domain_status=None,
                 domain_type=None, icp_status=None, mx_auth_status=None, mx_record=None, request_id=None, spf_auth_status=None,
                 spf_record=None, tl_domain_name=None, tracef_record=None):
        self.cname_auth_status = cname_auth_status  # type: str
        self.cname_confirm_status = cname_confirm_status  # type: str
        self.cname_record = cname_record  # type: str
        self.create_time = create_time  # type: str
        self.default_domain = default_domain  # type: str
        self.dns_mx = dns_mx  # type: str
        self.dns_spf = dns_spf  # type: str
        self.dns_txt = dns_txt  # type: str
        self.domain_id = domain_id  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.domain_type = domain_type  # type: str
        self.icp_status = icp_status  # type: str
        self.mx_auth_status = mx_auth_status  # type: str
        self.mx_record = mx_record  # type: str
        self.request_id = request_id  # type: str
        self.spf_auth_status = spf_auth_status  # type: str
        self.spf_record = spf_record  # type: str
        self.tl_domain_name = tl_domain_name  # type: str
        self.tracef_record = tracef_record  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.cname_confirm_status is not None:
            result['CnameConfirmStatus'] = self.cname_confirm_status
        if self.cname_record is not None:
            result['CnameRecord'] = self.cname_record
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.dns_mx is not None:
            result['DnsMx'] = self.dns_mx
        if self.dns_spf is not None:
            result['DnsSpf'] = self.dns_spf
        if self.dns_txt is not None:
            result['DnsTxt'] = self.dns_txt
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.mx_record is not None:
            result['MxRecord'] = self.mx_record
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.spf_record is not None:
            result['SpfRecord'] = self.spf_record
        if self.tl_domain_name is not None:
            result['TlDomainName'] = self.tl_domain_name
        if self.tracef_record is not None:
            result['TracefRecord'] = self.tracef_record
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('CnameConfirmStatus') is not None:
            self.cname_confirm_status = m.get('CnameConfirmStatus')
        if m.get('CnameRecord') is not None:
            self.cname_record = m.get('CnameRecord')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('DnsMx') is not None:
            self.dns_mx = m.get('DnsMx')
        if m.get('DnsSpf') is not None:
            self.dns_spf = m.get('DnsSpf')
        if m.get('DnsTxt') is not None:
            self.dns_txt = m.get('DnsTxt')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('MxRecord') is not None:
            self.mx_record = m.get('MxRecord')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('SpfRecord') is not None:
            self.spf_record = m.get('SpfRecord')
        if m.get('TlDomainName') is not None:
            self.tl_domain_name = m.get('TlDomainName')
        if m.get('TracefRecord') is not None:
            self.tracef_record = m.get('TracefRecord')
        return self


class DescDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescDomainResponse, self).to_map()
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
            temp_model = DescDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpProtectionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetIpProtectionResponseBody(TeaModel):
    def __init__(self, ip_protection=None, request_id=None):
        self.ip_protection = ip_protection  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpProtectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIpProtectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIpProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIpProtectionResponse, self).to_map()
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
            temp_model = GetIpProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpfilterListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpfilterListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetIpfilterListResponseBodyDataIpfilters(TeaModel):
    def __init__(self, create_time=None, id=None, ip_address=None):
        self.create_time = create_time  # type: str
        self.id = id  # type: str
        self.ip_address = ip_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpfilterListResponseBodyDataIpfilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class GetIpfilterListResponseBodyData(TeaModel):
    def __init__(self, ipfilters=None):
        self.ipfilters = ipfilters  # type: list[GetIpfilterListResponseBodyDataIpfilters]

    def validate(self):
        if self.ipfilters:
            for k in self.ipfilters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetIpfilterListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ipfilters'] = []
        if self.ipfilters is not None:
            for k in self.ipfilters:
                result['ipfilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ipfilters = []
        if m.get('ipfilters') is not None:
            for k in m.get('ipfilters'):
                temp_model = GetIpfilterListResponseBodyDataIpfilters()
                self.ipfilters.append(temp_model.from_map(k))
        return self


class GetIpfilterListResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, data=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: GetIpfilterListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetIpfilterListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = GetIpfilterListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetIpfilterListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIpfilterListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIpfilterListResponse, self).to_map()
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
            temp_model = GetIpfilterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListRequest(TeaModel):
    def __init__(self, end_time=None, offset=None, offset_create_time=None, offset_create_time_desc=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None,
                 start_time=None, total=None):
        self.end_time = end_time  # type: str
        self.offset = offset  # type: str
        self.offset_create_time = offset_create_time  # type: str
        self.offset_create_time_desc = offset_create_time_desc  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.total = total  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTrackListResponseBodyDataStat(TeaModel):
    def __init__(self, create_time=None, rcpt_click_count=None, rcpt_click_rate=None, rcpt_open_count=None,
                 rcpt_open_rate=None, rcpt_unique_click_count=None, rcpt_unique_click_rate=None, rcpt_unique_open_count=None,
                 rcpt_unique_open_rate=None, total_number=None):
        self.create_time = create_time  # type: str
        self.rcpt_click_count = rcpt_click_count  # type: str
        self.rcpt_click_rate = rcpt_click_rate  # type: str
        self.rcpt_open_count = rcpt_open_count  # type: str
        self.rcpt_open_rate = rcpt_open_rate  # type: str
        self.rcpt_unique_click_count = rcpt_unique_click_count  # type: str
        self.rcpt_unique_click_rate = rcpt_unique_click_rate  # type: str
        self.rcpt_unique_open_count = rcpt_unique_open_count  # type: str
        self.rcpt_unique_open_rate = rcpt_unique_open_rate  # type: str
        self.total_number = total_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrackListResponseBodyDataStat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count
        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate
        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count
        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate
        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count
        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate
        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count
        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')
        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')
        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')
        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')
        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')
        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')
        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')
        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class GetTrackListResponseBodyData(TeaModel):
    def __init__(self, stat=None):
        self.stat = stat  # type: list[GetTrackListResponseBodyDataStat]

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTrackListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k in m.get('stat'):
                temp_model = GetTrackListResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k))
        return self


class GetTrackListResponseBody(TeaModel):
    def __init__(self, offset_create_time=None, offset_create_time_desc=None, page_no=None, page_size=None,
                 request_id=None, total=None, data=None):
        self.offset_create_time = offset_create_time  # type: str
        self.offset_create_time_desc = offset_create_time_desc  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int
        self.data = data  # type: GetTrackListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTrackListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('data') is not None:
            temp_model = GetTrackListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetTrackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTrackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTrackListResponse, self).to_map()
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
            temp_model = GetTrackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListByMailFromAndTagNameRequest(TeaModel):
    def __init__(self, account_name=None, end_time=None, offset=None, offset_create_time=None,
                 offset_create_time_desc=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None, tag_name=None, total=None):
        self.account_name = account_name  # type: str
        self.end_time = end_time  # type: str
        self.offset = offset  # type: str
        self.offset_create_time = offset_create_time  # type: str
        self.offset_create_time_desc = offset_create_time_desc  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.tag_name = tag_name  # type: str
        self.total = total  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrackListByMailFromAndTagNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTrackListByMailFromAndTagNameResponseBodyTrackListStat(TeaModel):
    def __init__(self, create_time=None, rcpt_click_count=None, rcpt_click_rate=None, rcpt_open_count=None,
                 rcpt_open_rate=None, rcpt_unique_click_count=None, rcpt_unique_click_rate=None, rcpt_unique_open_count=None,
                 rcpt_unique_open_rate=None, total_number=None):
        self.create_time = create_time  # type: str
        self.rcpt_click_count = rcpt_click_count  # type: str
        self.rcpt_click_rate = rcpt_click_rate  # type: str
        self.rcpt_open_count = rcpt_open_count  # type: str
        self.rcpt_open_rate = rcpt_open_rate  # type: str
        self.rcpt_unique_click_count = rcpt_unique_click_count  # type: str
        self.rcpt_unique_click_rate = rcpt_unique_click_rate  # type: str
        self.rcpt_unique_open_count = rcpt_unique_open_count  # type: str
        self.rcpt_unique_open_rate = rcpt_unique_open_rate  # type: str
        self.total_number = total_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrackListByMailFromAndTagNameResponseBodyTrackListStat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count
        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate
        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count
        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate
        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count
        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate
        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count
        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')
        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')
        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')
        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')
        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')
        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')
        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')
        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class GetTrackListByMailFromAndTagNameResponseBodyTrackList(TeaModel):
    def __init__(self, stat=None):
        self.stat = stat  # type: list[GetTrackListByMailFromAndTagNameResponseBodyTrackListStat]

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTrackListByMailFromAndTagNameResponseBodyTrackList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['Stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.stat = []
        if m.get('Stat') is not None:
            for k in m.get('Stat'):
                temp_model = GetTrackListByMailFromAndTagNameResponseBodyTrackListStat()
                self.stat.append(temp_model.from_map(k))
        return self


class GetTrackListByMailFromAndTagNameResponseBody(TeaModel):
    def __init__(self, offset_create_time=None, offset_create_time_desc=None, page_no=None, page_size=None,
                 request_id=None, total=None, track_list=None):
        self.offset_create_time = offset_create_time  # type: str
        self.offset_create_time_desc = offset_create_time_desc  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int
        self.track_list = track_list  # type: GetTrackListByMailFromAndTagNameResponseBodyTrackList

    def validate(self):
        if self.track_list:
            self.track_list.validate()

    def to_map(self):
        _map = super(GetTrackListByMailFromAndTagNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.track_list is not None:
            result['TrackList'] = self.track_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TrackList') is not None:
            temp_model = GetTrackListByMailFromAndTagNameResponseBodyTrackList()
            self.track_list = temp_model.from_map(m['TrackList'])
        return self


class GetTrackListByMailFromAndTagNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTrackListByMailFromAndTagNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTrackListByMailFromAndTagNameResponse, self).to_map()
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
            temp_model = GetTrackListByMailFromAndTagNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMailAddressRequest(TeaModel):
    def __init__(self, mail_address_id=None, owner_id=None, password=None, reply_address=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.mail_address_id = mail_address_id  # type: int
        self.owner_id = owner_id  # type: long
        self.password = password  # type: str
        self.reply_address = reply_address  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMailAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyMailAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMailAddressResponseBody, self).to_map()
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


class ModifyMailAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMailAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMailAddressResponse, self).to_map()
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
            temp_model = ModifyMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPWByDomainRequest(TeaModel):
    def __init__(self, domain_name=None, password=None, resource_owner_id=None):
        self.domain_name = domain_name  # type: str
        self.password = password  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPWByDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyPWByDomainResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPWByDomainResponseBody, self).to_map()
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


class ModifyPWByDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPWByDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPWByDomainResponse, self).to_map()
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
            temp_model = ModifyPWByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTagRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, tag_id=None,
                 tag_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_id = tag_id  # type: int
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ModifyTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTagResponseBody, self).to_map()
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


class ModifyTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTagResponse, self).to_map()
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
            temp_model = ModifyTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByParamRequest(TeaModel):
    def __init__(self, key_word=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, status=None):
        self.key_word = key_word  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDomainByParamResponseBodyDataDomain(TeaModel):
    def __init__(self, cname_auth_status=None, confirm_status=None, create_time=None, domain_id=None,
                 domain_name=None, domain_record=None, domain_status=None, icp_status=None, mx_auth_status=None,
                 spf_auth_status=None, utc_create_time=None):
        self.cname_auth_status = cname_auth_status  # type: str
        self.confirm_status = confirm_status  # type: str
        self.create_time = create_time  # type: str
        self.domain_id = domain_id  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_record = domain_record  # type: str
        self.domain_status = domain_status  # type: str
        self.icp_status = icp_status  # type: str
        self.mx_auth_status = mx_auth_status  # type: str
        self.spf_auth_status = spf_auth_status  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByParamResponseBodyDataDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.confirm_status is not None:
            result['ConfirmStatus'] = self.confirm_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_record is not None:
            result['DomainRecord'] = self.domain_record
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('ConfirmStatus') is not None:
            self.confirm_status = m.get('ConfirmStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainRecord') is not None:
            self.domain_record = m.get('DomainRecord')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryDomainByParamResponseBodyData(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: list[QueryDomainByParamResponseBodyDataDomain]

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDomainByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain = []
        if m.get('domain') is not None:
            for k in m.get('domain'):
                temp_model = QueryDomainByParamResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class QueryDomainByParamResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, data=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryDomainByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDomainByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryDomainByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryDomainByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainByParamResponse, self).to_map()
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
            temp_model = QueryDomainByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvalidAddressRequest(TeaModel):
    def __init__(self, end_time=None, key_word=None, length=None, next_start=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.key_word = key_word  # type: str
        self.length = length  # type: int
        self.next_start = next_start  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvalidAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryInvalidAddressResponseBodyDataMailDetail(TeaModel):
    def __init__(self, last_update_time=None, to_address=None, utc_last_update_time=None):
        self.last_update_time = last_update_time  # type: str
        self.to_address = to_address  # type: str
        self.utc_last_update_time = utc_last_update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvalidAddressResponseBodyDataMailDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')
        return self


class QueryInvalidAddressResponseBodyData(TeaModel):
    def __init__(self, mail_detail=None):
        self.mail_detail = mail_detail  # type: list[QueryInvalidAddressResponseBodyDataMailDetail]

    def validate(self):
        if self.mail_detail:
            for k in self.mail_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryInvalidAddressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailDetail'] = []
        if self.mail_detail is not None:
            for k in self.mail_detail:
                result['mailDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mail_detail = []
        if m.get('mailDetail') is not None:
            for k in m.get('mailDetail'):
                temp_model = QueryInvalidAddressResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k))
        return self


class QueryInvalidAddressResponseBody(TeaModel):
    def __init__(self, next_start=None, request_id=None, total_count=None, data=None):
        self.next_start = next_start  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryInvalidAddressResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryInvalidAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryInvalidAddressResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryInvalidAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryInvalidAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryInvalidAddressResponse, self).to_map()
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
            temp_model = QueryInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMailAddressByParamRequest(TeaModel):
    def __init__(self, key_word=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, sendtype=None):
        self.key_word = key_word  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sendtype = sendtype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMailAddressByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class QueryMailAddressByParamResponseBodyDataMailAddress(TeaModel):
    def __init__(self, account_name=None, account_status=None, create_time=None, daily_count=None,
                 daily_req_count=None, domain_status=None, mail_address_id=None, month_count=None, month_req_count=None,
                 reply_address=None, reply_status=None, sendtype=None):
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.create_time = create_time  # type: str
        self.daily_count = daily_count  # type: str
        self.daily_req_count = daily_req_count  # type: str
        self.domain_status = domain_status  # type: str
        self.mail_address_id = mail_address_id  # type: str
        self.month_count = month_count  # type: str
        self.month_req_count = month_req_count  # type: str
        self.reply_address = reply_address  # type: str
        self.reply_status = reply_status  # type: str
        self.sendtype = sendtype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMailAddressByParamResponseBodyDataMailAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.daily_count is not None:
            result['DailyCount'] = self.daily_count
        if self.daily_req_count is not None:
            result['DailyReqCount'] = self.daily_req_count
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.month_count is not None:
            result['MonthCount'] = self.month_count
        if self.month_req_count is not None:
            result['MonthReqCount'] = self.month_req_count
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_status is not None:
            result['ReplyStatus'] = self.reply_status
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DailyCount') is not None:
            self.daily_count = m.get('DailyCount')
        if m.get('DailyReqCount') is not None:
            self.daily_req_count = m.get('DailyReqCount')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('MonthCount') is not None:
            self.month_count = m.get('MonthCount')
        if m.get('MonthReqCount') is not None:
            self.month_req_count = m.get('MonthReqCount')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyStatus') is not None:
            self.reply_status = m.get('ReplyStatus')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class QueryMailAddressByParamResponseBodyData(TeaModel):
    def __init__(self, mail_address=None):
        self.mail_address = mail_address  # type: list[QueryMailAddressByParamResponseBodyDataMailAddress]

    def validate(self):
        if self.mail_address:
            for k in self.mail_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMailAddressByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailAddress'] = []
        if self.mail_address is not None:
            for k in self.mail_address:
                result['mailAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mail_address = []
        if m.get('mailAddress') is not None:
            for k in m.get('mailAddress'):
                temp_model = QueryMailAddressByParamResponseBodyDataMailAddress()
                self.mail_address.append(temp_model.from_map(k))
        return self


class QueryMailAddressByParamResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, data=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryMailAddressByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMailAddressByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryMailAddressByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryMailAddressByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMailAddressByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMailAddressByParamResponse, self).to_map()
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
            temp_model = QueryMailAddressByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverByParamRequest(TeaModel):
    def __init__(self, key_word=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, status=None):
        self.key_word = key_word  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReceiverByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryReceiverByParamResponseBodyDataReceiver(TeaModel):
    def __init__(self, count=None, create_time=None, desc=None, receiver_id=None, receivers_alias=None,
                 receivers_name=None, receivers_status=None, utc_create_time=None):
        self.count = count  # type: str
        self.create_time = create_time  # type: str
        self.desc = desc  # type: str
        self.receiver_id = receiver_id  # type: str
        self.receivers_alias = receivers_alias  # type: str
        self.receivers_name = receivers_name  # type: str
        self.receivers_status = receivers_status  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReceiverByParamResponseBodyDataReceiver, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.receivers_status is not None:
            result['ReceiversStatus'] = self.receivers_status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ReceiversStatus') is not None:
            self.receivers_status = m.get('ReceiversStatus')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryReceiverByParamResponseBodyData(TeaModel):
    def __init__(self, receiver=None):
        self.receiver = receiver  # type: list[QueryReceiverByParamResponseBodyDataReceiver]

    def validate(self):
        if self.receiver:
            for k in self.receiver:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryReceiverByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receiver'] = []
        if self.receiver is not None:
            for k in self.receiver:
                result['receiver'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.receiver = []
        if m.get('receiver') is not None:
            for k in m.get('receiver'):
                temp_model = QueryReceiverByParamResponseBodyDataReceiver()
                self.receiver.append(temp_model.from_map(k))
        return self


class QueryReceiverByParamResponseBody(TeaModel):
    def __init__(self, next_start=None, page_size=None, request_id=None, total_count=None, data=None):
        self.next_start = next_start  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryReceiverByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryReceiverByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryReceiverByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryReceiverByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryReceiverByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryReceiverByParamResponse, self).to_map()
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
            temp_model = QueryReceiverByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverDetailRequest(TeaModel):
    def __init__(self, key_word=None, next_start=None, owner_id=None, page_size=None, receiver_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.key_word = key_word  # type: str
        self.next_start = next_start  # type: str
        self.owner_id = owner_id  # type: long
        self.page_size = page_size  # type: int
        self.receiver_id = receiver_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReceiverDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryReceiverDetailResponseBodyDataDetail(TeaModel):
    def __init__(self, create_time=None, data=None, email=None, utc_create_time=None):
        self.create_time = create_time  # type: str
        self.data = data  # type: str
        self.email = email  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReceiverDetailResponseBodyDataDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.email is not None:
            result['Email'] = self.email
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryReceiverDetailResponseBodyData(TeaModel):
    def __init__(self, detail=None):
        self.detail = detail  # type: list[QueryReceiverDetailResponseBodyDataDetail]

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryReceiverDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = QueryReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class QueryReceiverDetailResponseBody(TeaModel):
    def __init__(self, data_schema=None, next_start=None, request_id=None, total_count=None, data=None):
        self.data_schema = data_schema  # type: str
        self.next_start = next_start  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryReceiverDetailResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryReceiverDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_schema is not None:
            result['DataSchema'] = self.data_schema
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSchema') is not None:
            self.data_schema = m.get('DataSchema')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryReceiverDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryReceiverDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryReceiverDetailResponse, self).to_map()
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
            temp_model = QueryReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagByParamRequest(TeaModel):
    def __init__(self, key_word=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.key_word = key_word  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTagByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTagByParamResponseBodyDataTag(TeaModel):
    def __init__(self, tag_id=None, tag_name=None):
        self.tag_id = tag_id  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTagByParamResponseBodyDataTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryTagByParamResponseBodyData(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[QueryTagByParamResponseBodyDataTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTagByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = QueryTagByParamResponseBodyDataTag()
                self.tag.append(temp_model.from_map(k))
        return self


class QueryTagByParamResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, data=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryTagByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTagByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryTagByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryTagByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTagByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTagByParamResponse, self).to_map()
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
            temp_model = QueryTagByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskByParamRequest(TeaModel):
    def __init__(self, key_word=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, status=None):
        self.key_word = key_word  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTaskByParamResponseBodyDataTask(TeaModel):
    def __init__(self, address_type=None, create_time=None, receivers_name=None, request_count=None, tag_name=None,
                 task_id=None, task_status=None, template_name=None, utc_create_time=None):
        self.address_type = address_type  # type: str
        self.create_time = create_time  # type: str
        self.receivers_name = receivers_name  # type: str
        self.request_count = request_count  # type: str
        self.tag_name = tag_name  # type: str
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str
        self.template_name = template_name  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskByParamResponseBodyDataTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryTaskByParamResponseBodyData(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[QueryTaskByParamResponseBodyDataTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['task'] = []
        if self.task is not None:
            for k in self.task:
                result['task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task = []
        if m.get('task') is not None:
            for k in m.get('task'):
                temp_model = QueryTaskByParamResponseBodyDataTask()
                self.task.append(temp_model.from_map(k))
        return self


class QueryTaskByParamResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, data=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: QueryTaskByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTaskByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryTaskByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryTaskByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTaskByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskByParamResponse, self).to_map()
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
            temp_model = QueryTaskByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveReceiverDetailRequest(TeaModel):
    def __init__(self, detail=None, owner_id=None, receiver_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.detail = detail  # type: str
        self.owner_id = owner_id  # type: long
        self.receiver_id = receiver_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveReceiverDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SaveReceiverDetailResponseBodyDataDetail(TeaModel):
    def __init__(self, email=None):
        self.email = email  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveReceiverDetailResponseBodyDataDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class SaveReceiverDetailResponseBodyData(TeaModel):
    def __init__(self, detail=None):
        self.detail = detail  # type: list[SaveReceiverDetailResponseBodyDataDetail]

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveReceiverDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = SaveReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class SaveReceiverDetailResponseBody(TeaModel):
    def __init__(self, data=None, error_count=None, request_id=None, success_count=None):
        self.data = data  # type: SaveReceiverDetailResponseBodyData
        self.error_count = error_count  # type: int
        self.request_id = request_id  # type: str
        self.success_count = success_count  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SaveReceiverDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SaveReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class SaveReceiverDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveReceiverDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveReceiverDetailResponse, self).to_map()
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
            temp_model = SaveReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTestByTemplateRequest(TeaModel):
    def __init__(self, account_name=None, birthday=None, email=None, gender=None, mobile=None, nick_name=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, template_id=None, user_name=None):
        self.account_name = account_name  # type: str
        self.birthday = birthday  # type: str
        self.email = email  # type: str
        self.gender = gender  # type: str
        self.mobile = mobile  # type: str
        self.nick_name = nick_name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_id = template_id  # type: int
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTestByTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.email is not None:
            result['Email'] = self.email
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SendTestByTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTestByTemplateResponseBody, self).to_map()
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


class SendTestByTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendTestByTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendTestByTemplateResponse, self).to_map()
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
            temp_model = SendTestByTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsByTagNameAndBatchIDRequest(TeaModel):
    def __init__(self, account_name=None, end_time=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None, tag_name=None):
        self.account_name = account_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SenderStatisticsByTagNameAndBatchIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat(TeaModel):
    def __init__(self, create_time=None, faild_count=None, request_count=None, succeeded_percent=None,
                 success_count=None, unavailable_count=None, unavailable_percent=None):
        self.create_time = create_time  # type: str
        self.faild_count = faild_count  # type: str
        self.request_count = request_count  # type: str
        self.succeeded_percent = succeeded_percent  # type: str
        self.success_count = success_count  # type: str
        self.unavailable_count = unavailable_count  # type: str
        self.unavailable_percent = unavailable_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.faild_count is not None:
            result['faildCount'] = self.faild_count
        if self.request_count is not None:
            result['requestCount'] = self.request_count
        if self.succeeded_percent is not None:
            result['succeededPercent'] = self.succeeded_percent
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.unavailable_count is not None:
            result['unavailableCount'] = self.unavailable_count
        if self.unavailable_percent is not None:
            result['unavailablePercent'] = self.unavailable_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('faildCount') is not None:
            self.faild_count = m.get('faildCount')
        if m.get('requestCount') is not None:
            self.request_count = m.get('requestCount')
        if m.get('succeededPercent') is not None:
            self.succeeded_percent = m.get('succeededPercent')
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('unavailableCount') is not None:
            self.unavailable_count = m.get('unavailableCount')
        if m.get('unavailablePercent') is not None:
            self.unavailable_percent = m.get('unavailablePercent')
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBodyData(TeaModel):
    def __init__(self, stat=None):
        self.stat = stat  # type: list[SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat]

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SenderStatisticsByTagNameAndBatchIDResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k in m.get('stat'):
                temp_model = SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k))
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, data=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.data = data  # type: SenderStatisticsByTagNameAndBatchIDResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SenderStatisticsByTagNameAndBatchIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class SenderStatisticsByTagNameAndBatchIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SenderStatisticsByTagNameAndBatchIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SenderStatisticsByTagNameAndBatchIDResponse, self).to_map()
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
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsDetailByParamRequest(TeaModel):
    def __init__(self, account_name=None, end_time=None, length=None, next_start=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None, status=None, tag_name=None, to_address=None):
        self.account_name = account_name  # type: str
        self.end_time = end_time  # type: str
        self.length = length  # type: int
        self.next_start = next_start  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.tag_name = tag_name  # type: str
        self.to_address = to_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SenderStatisticsDetailByParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SenderStatisticsDetailByParamResponseBodyDataMailDetail(TeaModel):
    def __init__(self, account_name=None, last_update_time=None, message=None, status=None, to_address=None,
                 utc_last_update_time=None):
        self.account_name = account_name  # type: str
        self.last_update_time = last_update_time  # type: str
        self.message = message  # type: str
        self.status = status  # type: int
        self.to_address = to_address  # type: str
        self.utc_last_update_time = utc_last_update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SenderStatisticsDetailByParamResponseBodyDataMailDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')
        return self


class SenderStatisticsDetailByParamResponseBodyData(TeaModel):
    def __init__(self, mail_detail=None):
        self.mail_detail = mail_detail  # type: list[SenderStatisticsDetailByParamResponseBodyDataMailDetail]

    def validate(self):
        if self.mail_detail:
            for k in self.mail_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SenderStatisticsDetailByParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailDetail'] = []
        if self.mail_detail is not None:
            for k in self.mail_detail:
                result['mailDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mail_detail = []
        if m.get('mailDetail') is not None:
            for k in m.get('mailDetail'):
                temp_model = SenderStatisticsDetailByParamResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k))
        return self


class SenderStatisticsDetailByParamResponseBody(TeaModel):
    def __init__(self, next_start=None, request_id=None, data=None):
        self.next_start = next_start  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: SenderStatisticsDetailByParamResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SenderStatisticsDetailByParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = SenderStatisticsDetailByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class SenderStatisticsDetailByParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SenderStatisticsDetailByParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SenderStatisticsDetailByParamResponse, self).to_map()
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
            temp_model = SenderStatisticsDetailByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendMailRequest(TeaModel):
    def __init__(self, account_name=None, address_type=None, click_trace=None, from_alias=None, html_body=None,
                 owner_id=None, reply_address=None, reply_address_alias=None, reply_to_address=None,
                 resource_owner_account=None, resource_owner_id=None, subject=None, tag_name=None, text_body=None, to_address=None):
        self.account_name = account_name  # type: str
        self.address_type = address_type  # type: int
        self.click_trace = click_trace  # type: str
        self.from_alias = from_alias  # type: str
        self.html_body = html_body  # type: str
        self.owner_id = owner_id  # type: long
        self.reply_address = reply_address  # type: str
        self.reply_address_alias = reply_address_alias  # type: str
        self.reply_to_address = reply_to_address  # type: bool
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.subject = subject  # type: str
        self.tag_name = tag_name  # type: str
        self.text_body = text_body  # type: str
        self.to_address = to_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleSendMailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.reply_to_address is not None:
            result['ReplyToAddress'] = self.reply_to_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ReplyToAddress') is not None:
            self.reply_to_address = m.get('ReplyToAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SingleSendMailResponseBody(TeaModel):
    def __init__(self, env_id=None, request_id=None):
        self.env_id = env_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleSendMailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleSendMailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SingleSendMailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SingleSendMailResponse, self).to_map()
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
            temp_model = SingleSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpProtectionRequest(TeaModel):
    def __init__(self, ip_protection=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.ip_protection = ip_protection  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpProtectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpProtectionResponseBody, self).to_map()
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


class UpdateIpProtectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIpProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIpProtectionResponse, self).to_map()
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
            temp_model = UpdateIpProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMailAddressMsgCallBackUrlRequest(TeaModel):
    def __init__(self, mail_from=None, notify_url=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.mail_from = mail_from  # type: str
        self.notify_url = notify_url  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMailAddressMsgCallBackUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_from is not None:
            result['MailFrom'] = self.mail_from
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MailFrom') is not None:
            self.mail_from = m.get('MailFrom')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateMailAddressMsgCallBackUrlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMailAddressMsgCallBackUrlResponseBody, self).to_map()
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


class UpdateMailAddressMsgCallBackUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMailAddressMsgCallBackUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMailAddressMsgCallBackUrlResponse, self).to_map()
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
            temp_model = UpdateMailAddressMsgCallBackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


