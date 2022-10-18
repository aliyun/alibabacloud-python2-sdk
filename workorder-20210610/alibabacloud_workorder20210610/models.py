# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CloseTicketRequest(TeaModel):
    def __init__(self, ticket_id=None):
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class CloseTicketResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTicketResponseBody, self).to_map()
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


class CloseTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseTicketResponse, self).to_map()
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
            temp_model = CloseTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequestSecretInfo(TeaModel):
    def __init__(self, content=None, file_name_list=None):
        self.content = content  # type: str
        self.file_name_list = file_name_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketRequestSecretInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        return self


class CreateTicketRequest(TeaModel):
    def __init__(self, category_id=None, creator_id=None, description=None, email=None, file_name_list=None,
                 secret_info=None, severity=None, title=None):
        self.category_id = category_id  # type: str
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.email = email  # type: str
        self.file_name_list = file_name_list  # type: list[str]
        self.secret_info = secret_info  # type: CreateTicketRequestSecretInfo
        self.severity = severity  # type: int
        self.title = title  # type: str

    def validate(self):
        if self.secret_info:
            self.secret_info.validate()

    def to_map(self):
        _map = super(CreateTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.secret_info is not None:
            result['SecretInfo'] = self.secret_info.to_map()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('SecretInfo') is not None:
            temp_model = CreateTicketRequestSecretInfo()
            self.secret_info = temp_model.from_map(m['SecretInfo'])
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateTicketShrinkRequest(TeaModel):
    def __init__(self, category_id=None, creator_id=None, description=None, email=None, file_name_list_shrink=None,
                 secret_info_shrink=None, severity=None, title=None):
        self.category_id = category_id  # type: str
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.email = email  # type: str
        self.file_name_list_shrink = file_name_list_shrink  # type: str
        self.secret_info_shrink = secret_info_shrink  # type: str
        self.severity = severity  # type: int
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.file_name_list_shrink is not None:
            result['FileNameList'] = self.file_name_list_shrink
        if self.secret_info_shrink is not None:
            result['SecretInfo'] = self.secret_info_shrink
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FileNameList') is not None:
            self.file_name_list_shrink = m.get('FileNameList')
        if m.get('SecretInfo') is not None:
            self.secret_info_shrink = m.get('SecretInfo')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketResponseBody, self).to_map()
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


class CreateTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTicketResponse, self).to_map()
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateTicketRequest(TeaModel):
    def __init__(self, content=None, score=None, solved=None, ticket_id=None):
        self.content = content  # type: str
        self.score = score  # type: str
        self.solved = solved  # type: bool
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.score is not None:
            result['Score'] = self.score
        if self.solved is not None:
            result['Solved'] = self.solved
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Solved') is not None:
            self.solved = m.get('Solved')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class EvaluateTicketResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateTicketResponseBody, self).to_map()
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


class EvaluateTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EvaluateTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EvaluateTicketResponse, self).to_map()
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
            temp_model = EvaluateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachmentUploadUrlRequest(TeaModel):
    def __init__(self, file_name=None):
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAttachmentUploadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetAttachmentUploadUrlResponseBodyData(TeaModel):
    def __init__(self, get_signed_url=None, object_key=None, put_signed_url=None):
        self.get_signed_url = get_signed_url  # type: str
        self.object_key = object_key  # type: str
        self.put_signed_url = put_signed_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAttachmentUploadUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_signed_url is not None:
            result['GetSignedUrl'] = self.get_signed_url
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.put_signed_url is not None:
            result['PutSignedUrl'] = self.put_signed_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GetSignedUrl') is not None:
            self.get_signed_url = m.get('GetSignedUrl')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('PutSignedUrl') is not None:
            self.put_signed_url = m.get('PutSignedUrl')
        return self


class GetAttachmentUploadUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetAttachmentUploadUrlResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAttachmentUploadUrlResponseBody, self).to_map()
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
            temp_model = GetAttachmentUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAttachmentUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAttachmentUploadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAttachmentUploadUrlResponse, self).to_map()
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
            temp_model = GetAttachmentUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMqConsumerTagResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMqConsumerTagResponseBody, self).to_map()
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


class GetMqConsumerTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMqConsumerTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMqConsumerTagResponse, self).to_map()
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
            temp_model = GetMqConsumerTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTicketRequest(TeaModel):
    def __init__(self, ticket_id=None):
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class GetTicketResponseBodyDataSeverity(TeaModel):
    def __init__(self, label=None, value=None):
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTicketResponseBodyDataSeverity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTicketResponseBodyDataStatus(TeaModel):
    def __init__(self, label=None, value=None):
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTicketResponseBodyDataStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTicketResponseBodyData(TeaModel):
    def __init__(self, category_id=None, create_time=None, creator_id=None, description=None, severity=None,
                 status=None, ticket_id=None, title=None):
        self.category_id = category_id  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.severity = severity  # type: GetTicketResponseBodyDataSeverity
        self.status = status  # type: GetTicketResponseBodyDataStatus
        self.ticket_id = ticket_id  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.severity:
            self.severity.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(GetTicketResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.severity is not None:
            result['Severity'] = self.severity.to_map()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Severity') is not None:
            temp_model = GetTicketResponseBodyDataSeverity()
            self.severity = temp_model.from_map(m['Severity'])
        if m.get('Status') is not None:
            temp_model = GetTicketResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        self.code = code  # type: int
        self.data = data  # type: GetTicketResponseBodyData
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTicketResponseBodyData()
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
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTicketResponse, self).to_map()
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
            temp_model = GetTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoriesRequest(TeaModel):
    def __init__(self, language=None, name=None, product_id=None):
        self.language = language  # type: str
        self.name = name  # type: str
        self.product_id = product_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCategoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListCategoriesResponseBodyData(TeaModel):
    def __init__(self, category_id=None, category_name=None):
        self.category_id = category_id  # type: long
        self.category_name = category_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCategoriesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListCategoriesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListCategoriesResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCategoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCategoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCategoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCategoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCategoriesResponse, self).to_map()
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
            temp_model = ListCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(self, language=None, name=None):
        self.language = language  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListProductsResponseBodyDataProductList(TeaModel):
    def __init__(self, product_id=None, product_name=None):
        self.product_id = product_id  # type: long
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsResponseBodyDataProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListProductsResponseBodyData(TeaModel):
    def __init__(self, directory_id=None, directory_name=None, product_list=None):
        self.directory_id = directory_id  # type: long
        self.directory_name = directory_name  # type: str
        self.product_list = product_list  # type: list[ListProductsResponseBodyDataProductList]

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListProductsResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k))
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListProductsResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProductsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsResponse, self).to_map()
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketNotesRequest(TeaModel):
    def __init__(self, ticket_id=None):
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketNotesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ListTicketNotesResponseBodyDataAttachments(TeaModel):
    def __init__(self, name=None, url=None):
        self.name = name  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketNotesResponseBodyDataAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListTicketNotesResponseBodyDataDialog(TeaModel):
    def __init__(self, content=None, schema=None):
        self.content = content  # type: str
        self.schema = schema  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketNotesResponseBodyDataDialog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class ListTicketNotesResponseBodyDataUser(TeaModel):
    def __init__(self, name=None, role=None):
        self.name = name  # type: str
        self.role = role  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketNotesResponseBodyDataUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListTicketNotesResponseBodyData(TeaModel):
    def __init__(self, attachments=None, create_time=None, dialog=None, dialog_id=None, status=None, tip=None,
                 type=None, user=None):
        self.attachments = attachments  # type: list[ListTicketNotesResponseBodyDataAttachments]
        self.create_time = create_time  # type: long
        self.dialog = dialog  # type: ListTicketNotesResponseBodyDataDialog
        self.dialog_id = dialog_id  # type: long
        self.status = status  # type: int
        self.tip = tip  # type: str
        self.type = type  # type: int
        self.user = user  # type: ListTicketNotesResponseBodyDataUser

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()
        if self.dialog:
            self.dialog.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(ListTicketNotesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['Attachments'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dialog is not None:
            result['Dialog'] = self.dialog.to_map()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tip is not None:
            result['Tip'] = self.tip
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k in m.get('Attachments'):
                temp_model = ListTicketNotesResponseBodyDataAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dialog') is not None:
            temp_model = ListTicketNotesResponseBodyDataDialog()
            self.dialog = temp_model.from_map(m['Dialog'])
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tip') is not None:
            self.tip = m.get('Tip')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            temp_model = ListTicketNotesResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListTicketNotesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListTicketNotesResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTicketNotesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTicketNotesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTicketNotesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTicketNotesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTicketNotesResponse, self).to_map()
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
            temp_model = ListTicketNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketsRequest(TeaModel):
    def __init__(self, end_date=None, keyword=None, page_number=None, page_size=None, start_date=None,
                 status_list=None, ticket_id=None, ticket_id_list=None):
        self.end_date = end_date  # type: long
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: long
        self.status_list = status_list  # type: list[str]
        self.ticket_id = ticket_id  # type: str
        self.ticket_id_list = ticket_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.ticket_id_list is not None:
            result['TicketIdList'] = self.ticket_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list = m.get('TicketIdList')
        return self


class ListTicketsShrinkRequest(TeaModel):
    def __init__(self, end_date=None, keyword=None, page_number=None, page_size=None, start_date=None,
                 status_list=None, ticket_id=None, ticket_id_list_shrink=None):
        self.end_date = end_date  # type: long
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: long
        self.status_list = status_list  # type: list[str]
        self.ticket_id = ticket_id  # type: str
        self.ticket_id_list_shrink = ticket_id_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.ticket_id_list_shrink is not None:
            result['TicketIdList'] = self.ticket_id_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list_shrink = m.get('TicketIdList')
        return self


class ListTicketsResponseBodyDataStatus(TeaModel):
    def __init__(self, label=None, value=None):
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsResponseBodyDataStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTicketsResponseBodyData(TeaModel):
    def __init__(self, status=None, ticket_id=None, title=None):
        self.status = status  # type: ListTicketsResponseBodyDataStatus
        self.ticket_id = ticket_id  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(ListTicketsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = ListTicketsResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListTicketsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListTicketsResponseBodyData]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTicketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTicketsResponseBodyData()
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
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTicketsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTicketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTicketsResponse, self).to_map()
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
            temp_model = ListTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReopenTicketRequest(TeaModel):
    def __init__(self, content=None, ticket_id=None):
        self.content = content  # type: str
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReopenTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReopenTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReopenTicketResponseBody, self).to_map()
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


class ReopenTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReopenTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReopenTicketResponse, self).to_map()
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
            temp_model = ReopenTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplyTicketRequest(TeaModel):
    def __init__(self, content=None, encrypt=None, file_name_list=None, ticket_id=None):
        self.content = content  # type: str
        self.encrypt = encrypt  # type: bool
        self.file_name_list = file_name_list  # type: list[str]
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplyTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReplyTicketShrinkRequest(TeaModel):
    def __init__(self, content=None, encrypt=None, file_name_list_shrink=None, ticket_id=None):
        self.content = content  # type: str
        self.encrypt = encrypt  # type: bool
        self.file_name_list_shrink = file_name_list_shrink  # type: str
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplyTicketShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name_list_shrink is not None:
            result['FileNameList'] = self.file_name_list_shrink
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileNameList') is not None:
            self.file_name_list_shrink = m.get('FileNameList')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class ReplyTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplyTicketResponseBody, self).to_map()
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


class ReplyTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReplyTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplyTicketResponse, self).to_map()
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
            temp_model = ReplyTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


