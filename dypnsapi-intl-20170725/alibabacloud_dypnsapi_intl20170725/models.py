# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CheckVerificationRequest(TeaModel):
    def __init__(self, code=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 service_sid=None, to=None, verification_id=None):
        # The verification code.
        self.code = code  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid  # type: str
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to  # type: str
        # The unique authentication ID that is returned by calling the StartVerification operation.
        self.verification_id = verification_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        if self.verification_id is not None:
            result['VerificationId'] = self.verification_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('VerificationId') is not None:
            self.verification_id = m.get('VerificationId')
        return self


class CheckVerificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None):
        # The HTTP status code that was returned.
        self.code = code  # type: str
        # The message that was returned.
        self.message = message  # type: str
        # The data that was returned for the successful request. Example: "Model": { "phoneNumber": "", "channel": "", "verificationId": "", "status": "approved" },
        self.model = model  # type: dict[str, any]
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
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
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckVerificationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckVerificationResponse, self).to_map()
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
            temp_model = CheckVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchVerificationRequest(TeaModel):
    def __init__(self, code=None, current_page=None, owner_id=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, send_date=None, service_sid=None, to=None, verification_id=None):
        # The verification code.
        self.code = code  # type: str
        # The number of the page to return. Pages start from page 1.
        self.current_page = current_page  # type: long
        self.owner_id = owner_id  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The time when a text message is sent, in milliseconds. You can query text messages that were sent within the last 30 days.
        # 
        # Example: 1677600000000.
        self.send_date = send_date  # type: long
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid  # type: str
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to  # type: str
        # The unique authentication ID that is returned by calling the StartVerification operation.
        self.verification_id = verification_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        if self.verification_id is not None:
            result['VerificationId'] = self.verification_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('VerificationId') is not None:
            self.verification_id = m.get('VerificationId')
        return self


class SearchVerificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None):
        # The HTTP status code that was returned for the request.
        self.code = code  # type: str
        # The message that was returned.
        self.message = message  # type: str
        # The data that was returned for the request. Example: "Model": { "records": \[ { "sendDate":, "channel": "", "serviceSid": "", "to": "", "updatedDate":, "verificationId": "", "status": "" } ], "pageNo": , "totalPage": 1, "pageSize": 20, "totalCount": 1, }
        self.model = model  # type: dict[str, any]
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
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
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchVerificationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchVerificationResponse, self).to_map()
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
            temp_model = SearchVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVerificationRequest(TeaModel):
    def __init__(self, channel=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 service_sid=None, to=None):
        # The channels that you can use for verification.
        # 
        # Valid values:
        # 
        # *   Voice
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   SMS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   WhatsApp
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.channel = channel  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid  # type: str
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class StartVerificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None):
        # The HTTP status code that was returned for the request.
        self.code = code  # type: str
        # The message that was returned.
        self.message = message  # type: str
        # The data that was returned only if the request was successful. Example: "Model": { "verifyCode": "", "verificationId": "", "status": "" }
        self.model = model  # type: dict[str, any]
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
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
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartVerificationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartVerificationResponse, self).to_map()
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
            temp_model = StartVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


