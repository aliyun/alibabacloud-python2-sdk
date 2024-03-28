# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCorsDomainRequest(TeaModel):
    def __init__(self, domain=None, space_id=None):
        self.domain = domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCorsDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddCorsDomainResponseBody(TeaModel):
    def __init__(self, domain_id=None, request_id=None):
        self.domain_id = domain_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCorsDomainResponseBody, self).to_map()
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


class AddCorsDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCorsDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCorsDomainResponse, self).to_map()
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
            temp_model = AddCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, app_secret=None, space_id=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDingtalkOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddDingtalkOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDingtalkOpenPlatformConfigResponseBody, self).to_map()
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


class AddDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddDingtalkOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDingtalkOpenPlatformConfigResponse, self).to_map()
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
            temp_model = AddDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachWebHostingCertificateRequest(TeaModel):
    def __init__(self, cert_name=None, cert_type=None, domain=None, private_key=None, server_certificate=None,
                 space_id=None):
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain = domain  # type: str
        self.private_key = private_key  # type: str
        self.server_certificate = server_certificate  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachWebHostingCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AttachWebHostingCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachWebHostingCertificateResponseBody, self).to_map()
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


class AttachWebHostingCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachWebHostingCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachWebHostingCertificateResponse, self).to_map()
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
            temp_model = AttachWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteWebHostingFilesRequest(TeaModel):
    def __init__(self, file_paths=None, space_id=None):
        self.file_paths = file_paths  # type: list[str]
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteWebHostingFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class BatchDeleteWebHostingFilesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteWebHostingFilesResponseBody, self).to_map()
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


class BatchDeleteWebHostingFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteWebHostingFilesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteWebHostingFilesResponse, self).to_map()
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
            temp_model = BatchDeleteWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindWebHostingCustomDomainRequest(TeaModel):
    def __init__(self, custom_domain=None, space_id=None):
        self.custom_domain = custom_domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindWebHostingCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class BindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindWebHostingCustomDomainResponseBody, self).to_map()
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


class BindWebHostingCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindWebHostingCustomDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindWebHostingCustomDomainResponse, self).to_map()
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
            temp_model = BindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMpServerlessRoleExistsRequest(TeaModel):
    def __init__(self, role_name=None):
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMpServerlessRoleExistsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckMpServerlessRoleExistsResponseBody(TeaModel):
    def __init__(self, exists=None, request_id=None):
        self.exists = exists  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMpServerlessRoleExistsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exists is not None:
            result['Exists'] = self.exists
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMpServerlessRoleExistsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckMpServerlessRoleExistsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckMpServerlessRoleExistsResponse, self).to_map()
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
            temp_model = CheckMpServerlessRoleExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBExportTaskRequest(TeaModel):
    def __init__(self, collection=None, fields=None, file_type=None, space_id=None):
        self.collection = collection  # type: str
        self.fields = fields  # type: str
        self.file_type = file_type  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBExportTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBExportTaskResponse, self).to_map()
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
            temp_model = CreateDBExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBImportTaskRequest(TeaModel):
    def __init__(self, collection=None, file_type=None, mode=None, space_id=None):
        self.collection = collection  # type: str
        self.file_type = file_type  # type: str
        self.mode = mode  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBImportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBImportTaskResponseBody(TeaModel):
    def __init__(self, access_key_id=None, expire_time=None, file_key=None, host=None, policy=None, request_id=None,
                 signature=None, task_id=None):
        self.access_key_id = access_key_id  # type: str
        self.expire_time = expire_time  # type: str
        self.file_key = file_key  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBImportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBImportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBImportTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBImportTaskResponse, self).to_map()
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
            temp_model = CreateDBImportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRestoreTaskRequest(TeaModel):
    def __init__(self, backup_id=None, new_collections=None, origin_collections=None, space_id=None):
        self.backup_id = backup_id  # type: str
        self.new_collections = new_collections  # type: str
        self.origin_collections = origin_collections  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBRestoreTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.new_collections is not None:
            result['NewCollections'] = self.new_collections
        if self.origin_collections is not None:
            result['OriginCollections'] = self.origin_collections
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('NewCollections') is not None:
            self.new_collections = m.get('NewCollections')
        if m.get('OriginCollections') is not None:
            self.origin_collections = m.get('OriginCollections')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBRestoreTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBRestoreTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBRestoreTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBRestoreTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBRestoreTaskResponse, self).to_map()
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
            temp_model = CreateDBRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(self, desc=None, memory=None, name=None, runtime=None, space_id=None, timeout=None):
        self.desc = desc  # type: str
        self.memory = memory  # type: int
        self.name = name  # type: str
        self.runtime = runtime  # type: str
        self.space_id = space_id  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateFunctionResponseBodySpec(TeaModel):
    def __init__(self, instance_concurrency=None, memory=None, runtime=None, timeout=None):
        self.instance_concurrency = instance_concurrency  # type: str
        self.memory = memory  # type: str
        self.runtime = runtime  # type: str
        self.timeout = timeout  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionResponseBodySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(self, created_at=None, desc=None, modified_at=None, name=None, request_id=None, spec=None):
        self.created_at = created_at  # type: str
        self.desc = desc  # type: str
        self.modified_at = modified_at  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.spec = spec  # type: CreateFunctionResponseBodySpec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(CreateFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = CreateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionResponse, self).to_map()
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
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionDeploymentRequest(TeaModel):
    def __init__(self, name=None, space_id=None):
        self.name = name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateFunctionDeploymentResponseBody(TeaModel):
    def __init__(self, deployment_id=None, request_id=None, upload_signed_url=None):
        self.deployment_id = deployment_id  # type: str
        self.request_id = request_id  # type: str
        self.upload_signed_url = upload_signed_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_signed_url is not None:
            result['UploadSignedUrl'] = self.upload_signed_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadSignedUrl') is not None:
            self.upload_signed_url = m.get('UploadSignedUrl')
        return self


class CreateFunctionDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionDeploymentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionDeploymentResponse, self).to_map()
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
            temp_model = CreateFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpaceRequest(TeaModel):
    def __init__(self, desc=None, name=None, workspace_id=None):
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateSpaceResponseBody(TeaModel):
    def __init__(self, request_id=None, space_id=None):
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateSpaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSpaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSpaceResponse, self).to_map()
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
            temp_model = CreateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpaceWithOrderRequest(TeaModel):
    def __init__(self, desc=None, name=None, package_version=None, period=None, subscription_type=None,
                 use_coupon=None):
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.package_version = package_version  # type: str
        self.period = period  # type: int
        self.subscription_type = subscription_type  # type: str
        self.use_coupon = use_coupon  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpaceWithOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.period is not None:
            result['Period'] = self.period
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        return self


class CreateSpaceWithOrderResponseBody(TeaModel):
    def __init__(self, instance_id=None, order_id=None, request_id=None, space_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpaceWithOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateSpaceWithOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSpaceWithOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSpaceWithOrderResponse, self).to_map()
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
            temp_model = CreateSpaceWithOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, space_id=None):
        self.app_id = app_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAntOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteAntOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAntOpenPlatformConfigResponseBody, self).to_map()
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


class DeleteAntOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAntOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAntOpenPlatformConfigResponse, self).to_map()
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
            temp_model = DeleteAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCorsDomainRequest(TeaModel):
    def __init__(self, domain_id=None, space_id=None):
        self.domain_id = domain_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCorsDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteCorsDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCorsDomainResponseBody, self).to_map()
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


class DeleteCorsDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCorsDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCorsDomainResponse, self).to_map()
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
            temp_model = DeleteCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBCollectionRequest(TeaModel):
    def __init__(self, body=None, space_id=None):
        self.body = body  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteDBCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBCollectionResponseBody, self).to_map()
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


class DeleteDBCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDBCollectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBCollectionResponse, self).to_map()
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
            temp_model = DeleteDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, space_id=None):
        self.app_id = app_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDingtalkOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteDingtalkOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDingtalkOpenPlatformConfigResponseBody, self).to_map()
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


class DeleteDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDingtalkOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDingtalkOpenPlatformConfigResponse, self).to_map()
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
            temp_model = DeleteDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, id=None, space_id=None):
        self.id = id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileResponseBody, self).to_map()
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


class DeleteFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileResponse, self).to_map()
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionRequest(TeaModel):
    def __init__(self, name=None, space_id=None):
        self.name = name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFunctionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionResponseBody, self).to_map()
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


class DeleteFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFunctionResponse, self).to_map()
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
            temp_model = DeleteFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpaceRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteSpaceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpaceResponseBody, self).to_map()
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


class DeleteSpaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSpaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSpaceResponse, self).to_map()
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
            temp_model = DeleteSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingCertificateRequest(TeaModel):
    def __init__(self, domain=None, space_id=None):
        self.domain = domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebHostingCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWebHostingCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebHostingCertificateResponseBody, self).to_map()
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


class DeleteWebHostingCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebHostingCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebHostingCertificateResponse, self).to_map()
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
            temp_model = DeleteWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingFileRequest(TeaModel):
    def __init__(self, file_path=None, space_id=None):
        self.file_path = file_path  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebHostingFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWebHostingFileResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebHostingFileResponseBody, self).to_map()
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


class DeleteWebHostingFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebHostingFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebHostingFileResponse, self).to_map()
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
            temp_model = DeleteWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, space_id=None):
        self.app_id = app_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWechatOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWechatOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWechatOpenPlatformConfigResponseBody, self).to_map()
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


class DeleteWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWechatOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWechatOpenPlatformConfigResponse, self).to_map()
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
            temp_model = DeleteWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployFunctionRequest(TeaModel):
    def __init__(self, deployment_id=None, space_id=None):
        self.deployment_id = deployment_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeployFunctionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployFunctionResponseBody, self).to_map()
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


class DeployFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployFunctionResponse, self).to_map()
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
            temp_model = DeployFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainRequest(TeaModel):
    def __init__(self, space_id=None, tenant_id=None, type=None):
        self.space_id = space_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyAuthConfig(TeaModel):
    def __init__(self, auth_delta=None, auth_key=None, auth_type=None, config_id=None):
        self.auth_delta = auth_delta  # type: int
        self.auth_key = auth_key  # type: str
        self.auth_type = auth_type  # type: str
        self.config_id = config_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBodyAuthConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.config_id is not None:
            result['configId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('configId') is not None:
            self.config_id = m.get('configId')
        return self


class DescribeCdnDomainResponseBodyCorsConfig(TeaModel):
    def __init__(self, access_origin_control=None, allow_origin=None, config_id=None):
        self.access_origin_control = access_origin_control  # type: bool
        self.allow_origin = allow_origin  # type: str
        self.config_id = config_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBodyCorsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.allow_origin is not None:
            result['AllowOrigin'] = self.allow_origin
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('AllowOrigin') is not None:
            self.allow_origin = m.get('AllowOrigin')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DescribeCdnDomainResponseBodyIpConfig(TeaModel):
    def __init__(self, config_id=None, ip_list=None, type=None):
        self.config_id = config_id  # type: str
        self.ip_list = ip_list  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBodyIpConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyRefererConfig(TeaModel):
    def __init__(self, allow_empty=None, config_id=None, disable_ast=None, refer_list=None, type=None):
        self.allow_empty = allow_empty  # type: str
        self.config_id = config_id  # type: str
        self.disable_ast = disable_ast  # type: str
        self.refer_list = refer_list  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBodyRefererConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_empty is not None:
            result['AllowEmpty'] = self.allow_empty
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.disable_ast is not None:
            result['DisableAst'] = self.disable_ast
        if self.refer_list is not None:
            result['ReferList'] = self.refer_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowEmpty') is not None:
            self.allow_empty = m.get('AllowEmpty')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DisableAst') is not None:
            self.disable_ast = m.get('DisableAst')
        if m.get('ReferList') is not None:
            self.refer_list = m.get('ReferList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyUaConfig(TeaModel):
    def __init__(self, config_id=None, type=None, ua_list=None):
        self.config_id = config_id  # type: str
        self.type = type  # type: str
        self.ua_list = ua_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBodyUaConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.type is not None:
            result['Type'] = self.type
        if self.ua_list is not None:
            result['UaList'] = self.ua_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UaList') is not None:
            self.ua_list = m.get('UaList')
        return self


class DescribeCdnDomainResponseBody(TeaModel):
    def __init__(self, auth_config=None, cors_config=None, domain_name=None, ip_config=None, referer_config=None,
                 request_id=None, service_status=None, space_id=None, ua_config=None):
        self.auth_config = auth_config  # type: DescribeCdnDomainResponseBodyAuthConfig
        self.cors_config = cors_config  # type: DescribeCdnDomainResponseBodyCorsConfig
        self.domain_name = domain_name  # type: str
        self.ip_config = ip_config  # type: DescribeCdnDomainResponseBodyIpConfig
        self.referer_config = referer_config  # type: DescribeCdnDomainResponseBodyRefererConfig
        self.request_id = request_id  # type: str
        self.service_status = service_status  # type: str
        self.space_id = space_id  # type: str
        self.ua_config = ua_config  # type: DescribeCdnDomainResponseBodyUaConfig

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cors_config:
            self.cors_config.validate()
        if self.ip_config:
            self.ip_config.validate()
        if self.referer_config:
            self.referer_config.validate()
        if self.ua_config:
            self.ua_config.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config.to_map()
        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.ip_config is not None:
            result['IpConfig'] = self.ip_config.to_map()
        if self.referer_config is not None:
            result['RefererConfig'] = self.referer_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.ua_config is not None:
            result['UaConfig'] = self.ua_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyAuthConfig()
            self.auth_config = temp_model.from_map(m['AuthConfig'])
        if m.get('CorsConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyCorsConfig()
            self.cors_config = temp_model.from_map(m['CorsConfig'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IpConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyIpConfig()
            self.ip_config = temp_model.from_map(m['IpConfig'])
        if m.get('RefererConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyRefererConfig()
            self.referer_config = temp_model.from_map(m['RefererConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('UaConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyUaConfig()
            self.ua_config = temp_model.from_map(m['UaConfig'])
        return self


class DescribeCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCdnDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainResponse, self).to_map()
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
            temp_model = DescribeCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCOpenStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFCOpenStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFCOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFCOpenStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFCOpenStatusResponse, self).to_map()
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
            temp_model = DescribeFCOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileUploadSignedUrlRequest(TeaModel):
    def __init__(self, content_type=None, file_id=None, filename=None, size=None, space_id=None):
        self.content_type = content_type  # type: str
        self.file_id = file_id  # type: str
        self.filename = filename  # type: str
        self.size = size  # type: long
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileUploadSignedUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.size is not None:
            result['Size'] = self.size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFileUploadSignedUrlResponseBody(TeaModel):
    def __init__(self, id=None, oss_callback_url=None, overwrite=None, request_id=None, sign_url=None):
        self.id = id  # type: str
        self.oss_callback_url = oss_callback_url  # type: str
        self.overwrite = overwrite  # type: bool
        self.request_id = request_id  # type: str
        self.sign_url = sign_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileUploadSignedUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_callback_url is not None:
            result['OssCallbackUrl'] = self.oss_callback_url
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_url is not None:
            result['SignUrl'] = self.sign_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssCallbackUrl') is not None:
            self.oss_callback_url = m.get('OssCallbackUrl')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignUrl') is not None:
            self.sign_url = m.get('SignUrl')
        return self


class DescribeFileUploadSignedUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFileUploadSignedUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFileUploadSignedUrlResponse, self).to_map()
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
            temp_model = DescribeFileUploadSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFunctionRequest(TeaModel):
    def __init__(self, name=None, space_id=None):
        self.name = name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFunctionResponseBodyDeployment(TeaModel):
    def __init__(self, created_at=None, deployment_id=None, download_signed_url=None, modified_at=None,
                 version_no=None):
        self.created_at = created_at  # type: str
        self.deployment_id = deployment_id  # type: str
        self.download_signed_url = download_signed_url  # type: str
        self.modified_at = modified_at  # type: str
        self.version_no = version_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFunctionResponseBodyDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        return self


class DescribeFunctionResponseBodyFunctionSpec(TeaModel):
    def __init__(self, instance_concurrency=None, memory=None, runtime=None, timeout=None):
        self.instance_concurrency = instance_concurrency  # type: int
        self.memory = memory  # type: str
        self.runtime = runtime  # type: str
        self.timeout = timeout  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFunctionResponseBodyFunctionSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class DescribeFunctionResponseBodyFunction(TeaModel):
    def __init__(self, created_at=None, desc=None, http_trigger_path=None, modified_at=None, name=None, spec=None,
                 timing_trigger_config=None, timing_trigger_user_payload=None):
        self.created_at = created_at  # type: str
        self.desc = desc  # type: str
        self.http_trigger_path = http_trigger_path  # type: str
        self.modified_at = modified_at  # type: str
        self.name = name  # type: str
        self.spec = spec  # type: DescribeFunctionResponseBodyFunctionSpec
        self.timing_trigger_config = timing_trigger_config  # type: str
        self.timing_trigger_user_payload = timing_trigger_user_payload  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(DescribeFunctionResponseBodyFunction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Spec') is not None:
            temp_model = DescribeFunctionResponseBodyFunctionSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class DescribeFunctionResponseBody(TeaModel):
    def __init__(self, deployment=None, function=None, request_id=None):
        self.deployment = deployment  # type: DescribeFunctionResponseBodyDeployment
        self.function = function  # type: DescribeFunctionResponseBodyFunction
        self.request_id = request_id  # type: str

    def validate(self):
        if self.deployment:
            self.deployment.validate()
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super(DescribeFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment is not None:
            result['Deployment'] = self.deployment.to_map()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deployment') is not None:
            temp_model = DescribeFunctionResponseBodyDeployment()
            self.deployment = temp_model.from_map(m['Deployment'])
        if m.get('Function') is not None:
            temp_model = DescribeFunctionResponseBodyFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFunctionResponse, self).to_map()
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
            temp_model = DescribeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpTriggerConfigRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHttpTriggerConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeHttpTriggerConfigResponseBody(TeaModel):
    def __init__(self, custom_domain=None, custom_domain_certificate_info=None, custom_domain_cname=None,
                 default_endpoint=None, enable_service=None, request_id=None):
        self.custom_domain = custom_domain  # type: str
        self.custom_domain_certificate_info = custom_domain_certificate_info  # type: str
        self.custom_domain_cname = custom_domain_cname  # type: str
        self.default_endpoint = default_endpoint  # type: str
        self.enable_service = enable_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHttpTriggerConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHttpTriggerConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHttpTriggerConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHttpTriggerConfigResponse, self).to_map()
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
            temp_model = DescribeHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceQuotaRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeResourceQuotaResponseBody(TeaModel):
    def __init__(self, cloud_storage_data_size_quota=None, request_id=None, static_web_data_size_quota=None):
        self.cloud_storage_data_size_quota = cloud_storage_data_size_quota  # type: float
        self.request_id = request_id  # type: str
        self.static_web_data_size_quota = static_web_data_size_quota  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_data_size_quota is not None:
            result['CloudStorageDataSizeQuota'] = self.cloud_storage_data_size_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.static_web_data_size_quota is not None:
            result['StaticWebDataSizeQuota'] = self.static_web_data_size_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudStorageDataSizeQuota') is not None:
            self.cloud_storage_data_size_quota = m.get('CloudStorageDataSizeQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StaticWebDataSizeQuota') is not None:
            self.static_web_data_size_quota = m.get('StaticWebDataSizeQuota')
        return self


class DescribeResourceQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceQuotaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceQuotaResponse, self).to_map()
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
            temp_model = DescribeResourceQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceUsageRequest(TeaModel):
    def __init__(self, end_time=None, format=None, page_number=None, page_size=None, space_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.format = format  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.space_id = space_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.format is not None:
            result['Format'] = self.format
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeResourceUsageResponseBodyDataListCloudDB(TeaModel):
    def __init__(self, data_size=None, read=None, write=None):
        self.data_size = data_size  # type: long
        self.read = read  # type: long
        self.write = write  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyDataListCloudDB, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.read is not None:
            result['Read'] = self.read
        if self.write is not None:
            result['Write'] = self.write
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Read') is not None:
            self.read = m.get('Read')
        if m.get('Write') is not None:
            self.write = m.get('Write')
        return self


class DescribeResourceUsageResponseBodyDataListCloudFunction(TeaModel):
    def __init__(self, compute=None, count=None, traffic=None):
        self.compute = compute  # type: long
        self.count = count  # type: long
        self.traffic = traffic  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyDataListCloudFunction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute
        if self.count is not None:
            result['Count'] = self.count
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Compute') is not None:
            self.compute = m.get('Compute')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeResourceUsageResponseBodyDataListCloudStorage(TeaModel):
    def __init__(self, data_size=None, download=None, traffic=None, upload=None):
        self.data_size = data_size  # type: long
        self.download = download  # type: long
        self.traffic = traffic  # type: long
        self.upload = upload  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyDataListCloudStorage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.download is not None:
            result['Download'] = self.download
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.upload is not None:
            result['Upload'] = self.upload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Download') is not None:
            self.download = m.get('Download')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Upload') is not None:
            self.upload = m.get('Upload')
        return self


class DescribeResourceUsageResponseBodyDataListStaticWeb(TeaModel):
    def __init__(self, data_size=None, traffic=None):
        self.data_size = data_size  # type: long
        self.traffic = traffic  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyDataListStaticWeb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeResourceUsageResponseBodyDataList(TeaModel):
    def __init__(self, cloud_db=None, cloud_function=None, cloud_storage=None, end_time=None, start_time=None,
                 static_web=None):
        self.cloud_db = cloud_db  # type: DescribeResourceUsageResponseBodyDataListCloudDB
        self.cloud_function = cloud_function  # type: DescribeResourceUsageResponseBodyDataListCloudFunction
        self.cloud_storage = cloud_storage  # type: DescribeResourceUsageResponseBodyDataListCloudStorage
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.static_web = static_web  # type: DescribeResourceUsageResponseBodyDataListStaticWeb

    def validate(self):
        if self.cloud_db:
            self.cloud_db.validate()
        if self.cloud_function:
            self.cloud_function.validate()
        if self.cloud_storage:
            self.cloud_storage.validate()
        if self.static_web:
            self.static_web.validate()

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_db is not None:
            result['CloudDB'] = self.cloud_db.to_map()
        if self.cloud_function is not None:
            result['CloudFunction'] = self.cloud_function.to_map()
        if self.cloud_storage is not None:
            result['CloudStorage'] = self.cloud_storage.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.static_web is not None:
            result['StaticWeb'] = self.static_web.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudDB') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudDB()
            self.cloud_db = temp_model.from_map(m['CloudDB'])
        if m.get('CloudFunction') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudFunction()
            self.cloud_function = temp_model.from_map(m['CloudFunction'])
        if m.get('CloudStorage') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudStorage()
            self.cloud_storage = temp_model.from_map(m['CloudStorage'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StaticWeb') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListStaticWeb()
            self.static_web = temp_model.from_map(m['StaticWeb'])
        return self


class DescribeResourceUsageResponseBodyPaginator(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, total=None):
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBodyPaginator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeResourceUsageResponseBody(TeaModel):
    def __init__(self, code=None, data_list=None, http_status_code=None, message=None, paginator=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.data_list = data_list  # type: list[DescribeResourceUsageResponseBodyDataList]
        self.http_status_code = http_status_code  # type: str
        self.message = message  # type: str
        self.paginator = paginator  # type: DescribeResourceUsageResponseBodyPaginator
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeResourceUsageResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Paginator') is not None:
            temp_model = DescribeResourceUsageResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeResourceUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceUsageResponse, self).to_map()
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
            temp_model = DescribeResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServicePolicyRequest(TeaModel):
    def __init__(self, collection_name=None, service_name=None, space_id=None):
        self.collection_name = collection_name  # type: str
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServicePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeServicePolicyResponseBody(TeaModel):
    def __init__(self, collection_name=None, policy=None, policy_name=None, request_id=None, service_name=None,
                 space_id=None):
        self.collection_name = collection_name  # type: str
        self.policy = policy  # type: str
        self.policy_name = policy_name  # type: str
        self.request_id = request_id  # type: str
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServicePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeServicePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServicePolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServicePolicyResponse, self).to_map()
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
            temp_model = DescribeServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpaceClientConfigRequest(TeaModel):
    def __init__(self, detail=None, space_id=None, workspace_id=None):
        self.detail = detail  # type: str
        self.space_id = space_id  # type: str
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpaceClientConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DescribeSpaceClientConfigResponseBody(TeaModel):
    def __init__(self, api_key=None, endpoint=None, file_upload_endpoint=None, name=None, private_key=None,
                 request_id=None, space_id=None):
        self.api_key = api_key  # type: str
        self.endpoint = endpoint  # type: str
        self.file_upload_endpoint = file_upload_endpoint  # type: str
        self.name = name  # type: str
        self.private_key = private_key  # type: str
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpaceClientConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_upload_endpoint is not None:
            result['FileUploadEndpoint'] = self.file_upload_endpoint
        if self.name is not None:
            result['Name'] = self.name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileUploadEndpoint') is not None:
            self.file_upload_endpoint = m.get('FileUploadEndpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSpaceClientConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSpaceClientConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSpaceClientConfigResponse, self).to_map()
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
            temp_model = DescribeSpaceClientConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpacesRequest(TeaModel):
    def __init__(self, emas_workspace_id=None, page_num=None, page_size=None, space_ids=None, spec_code=None,
                 tenant_id=None):
        self.emas_workspace_id = emas_workspace_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_ids = space_ids  # type: list[str]
        self.spec_code = spec_code  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids is not None:
            result['SpaceIds'] = self.space_ids
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids = m.get('SpaceIds')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSpacesShrinkRequest(TeaModel):
    def __init__(self, emas_workspace_id=None, page_num=None, page_size=None, space_ids_shrink=None, spec_code=None,
                 tenant_id=None):
        self.emas_workspace_id = emas_workspace_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_ids_shrink = space_ids_shrink  # type: str
        self.spec_code = spec_code  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpacesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids_shrink is not None:
            result['SpaceIds'] = self.space_ids_shrink
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids_shrink = m.get('SpaceIds')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSpacesResponseBodySpaces(TeaModel):
    def __init__(self, auto_renew=None, charge_type=None, description=None, emas_workspace_id=None, gmt_create=None,
                 gmt_modified=None, instance_id=None, name=None, order_type=None, package_end_date=None, package_start_date=None,
                 package_status=None, renew_duration=None, service_status=None, space_id=None, spec_code=None):
        self.auto_renew = auto_renew  # type: bool
        self.charge_type = charge_type  # type: str
        self.description = description  # type: str
        self.emas_workspace_id = emas_workspace_id  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.order_type = order_type  # type: str
        self.package_end_date = package_end_date  # type: str
        self.package_start_date = package_start_date  # type: str
        self.package_status = package_status  # type: str
        self.renew_duration = renew_duration  # type: str
        self.service_status = service_status  # type: str
        self.space_id = space_id  # type: str
        self.spec_code = spec_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpacesResponseBodySpaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.description is not None:
            result['Description'] = self.description
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.package_end_date is not None:
            result['PackageEndDate'] = self.package_end_date
        if self.package_start_date is not None:
            result['PackageStartDate'] = self.package_start_date
        if self.package_status is not None:
            result['PackageStatus'] = self.package_status
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PackageEndDate') is not None:
            self.package_end_date = m.get('PackageEndDate')
        if m.get('PackageStartDate') is not None:
            self.package_start_date = m.get('PackageStartDate')
        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        return self


class DescribeSpacesResponseBody(TeaModel):
    def __init__(self, count=None, gmt_create=None, request_id=None, spaces=None):
        self.count = count  # type: int
        self.gmt_create = gmt_create  # type: str
        self.request_id = request_id  # type: str
        self.spaces = spaces  # type: list[DescribeSpacesResponseBodySpaces]

    def validate(self):
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSpacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['Spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spaces = []
        if m.get('Spaces') is not None:
            for k in m.get('Spaces'):
                temp_model = DescribeSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class DescribeSpacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSpacesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSpacesResponse, self).to_map()
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
            temp_model = DescribeSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebHostingFileRequest(TeaModel):
    def __init__(self, file_path=None, space_id=None):
        self.file_path = file_path  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebHostingFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeWebHostingFileResponseBodyData(TeaModel):
    def __init__(self, content_type=None, etag=None, exists=None, file_path=None, last_modified_time=None,
                 signed_url=None, size=None):
        self.content_type = content_type  # type: str
        self.etag = etag  # type: str
        self.exists = exists  # type: bool
        self.file_path = file_path  # type: str
        self.last_modified_time = last_modified_time  # type: long
        self.signed_url = signed_url  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebHostingFileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exists is not None:
            result['Exists'] = self.exists
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeWebHostingFileResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeWebHostingFileResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWebHostingFileResponseBody, self).to_map()
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
            temp_model = DescribeWebHostingFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebHostingFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebHostingFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebHostingFileResponse, self).to_map()
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
            temp_model = DescribeWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExtensionRequest(TeaModel):
    def __init__(self, extension_id=None):
        self.extension_id = extension_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableExtensionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        return self


class EnableExtensionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableExtensionResponseBody, self).to_map()
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


class EnableExtensionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableExtensionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableExtensionResponse, self).to_map()
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
            temp_model = EnableExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingCertificateDetailRequest(TeaModel):
    def __init__(self, custom_domain=None, space_id=None):
        self.custom_domain = custom_domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingCertificateDetailResponseBodyData(TeaModel):
    def __init__(self, cert_domain_name=None, cert_expired_time=None, cert_life=None, cert_name=None,
                 cert_type=None, server_certificate_status=None):
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expired_time = cert_expired_time  # type: long
        self.cert_life = cert_life  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.server_certificate_status = server_certificate_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingCertificateDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expired_time is not None:
            result['CertExpiredTime'] = self.cert_expired_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpiredTime') is not None:
            self.cert_expired_time = m.get('CertExpiredTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        return self


class GetWebHostingCertificateDetailResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetWebHostingCertificateDetailResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWebHostingCertificateDetailResponseBody, self).to_map()
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
            temp_model = GetWebHostingCertificateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebHostingCertificateDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebHostingCertificateDetailResponse, self).to_map()
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
            temp_model = GetWebHostingCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingConfigRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingConfigResponseBodyData(TeaModel):
    def __init__(self, allowed_ips=None, default_domain=None, error_http_status=None, error_path=None,
                 index_path=None, space_id=None):
        self.allowed_ips = allowed_ips  # type: str
        self.default_domain = default_domain  # type: str
        self.error_http_status = error_http_status  # type: str
        self.error_path = error_path  # type: str
        self.index_path = index_path  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.error_http_status is not None:
            result['ErrorHttpStatus'] = self.error_http_status
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('ErrorHttpStatus') is not None:
            self.error_http_status = m.get('ErrorHttpStatus')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetWebHostingConfigResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWebHostingConfigResponseBody, self).to_map()
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
            temp_model = GetWebHostingConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebHostingConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebHostingConfigResponse, self).to_map()
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
            temp_model = GetWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingDomainVerificationContentRequest(TeaModel):
    def __init__(self, domain=None, space_id=None):
        self.domain = domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingDomainVerificationContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingDomainVerificationContentResponseBodyData(TeaModel):
    def __init__(self, content=None, domain=None):
        self.content = content  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingDomainVerificationContentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetWebHostingDomainVerificationContentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetWebHostingDomainVerificationContentResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWebHostingDomainVerificationContentResponseBody, self).to_map()
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
            temp_model = GetWebHostingDomainVerificationContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingDomainVerificationContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebHostingDomainVerificationContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebHostingDomainVerificationContentResponse, self).to_map()
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
            temp_model = GetWebHostingDomainVerificationContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingStatusRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingStatusResponseBodyData(TeaModel):
    def __init__(self, space_id=None, status=None):
        self.space_id = space_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWebHostingStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetWebHostingStatusResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWebHostingStatusResponseBody, self).to_map()
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
            temp_model = GetWebHostingStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebHostingStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebHostingStatusResponse, self).to_map()
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
            temp_model = GetWebHostingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingUploadCredentialRequest(TeaModel):
    def __init__(self, file_path=None, space_id=None):
        self.file_path = file_path  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingUploadCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingUploadCredentialResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, endpoint=None, expired_time=None, file_path=None, policy=None,
                 security_token=None, signature=None):
        self.access_key_id = access_key_id  # type: str
        self.endpoint = endpoint  # type: str
        self.expired_time = expired_time  # type: long
        self.file_path = file_path  # type: str
        self.policy = policy  # type: str
        self.security_token = security_token  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebHostingUploadCredentialResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetWebHostingUploadCredentialResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetWebHostingUploadCredentialResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWebHostingUploadCredentialResponseBody, self).to_map()
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
            temp_model = GetWebHostingUploadCredentialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingUploadCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebHostingUploadCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebHostingUploadCredentialResponse, self).to_map()
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
            temp_model = GetWebHostingUploadCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorsDomainsRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCorsDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListCorsDomainsResponseBodyDomains(TeaModel):
    def __init__(self, domain=None, domain_id=None):
        self.domain = domain  # type: str
        self.domain_id = domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCorsDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class ListCorsDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None):
        self.domains = domains  # type: list[ListCorsDomainsResponseBodyDomains]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCorsDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListCorsDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCorsDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCorsDomainsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCorsDomainsResponse, self).to_map()
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
            temp_model = ListCorsDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDingtalkOpenPlatformConfigsRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDingtalkOpenPlatformConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListDingtalkOpenPlatformConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, app_id=None, app_secret=None, create_time=None, update_time=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDingtalkOpenPlatformConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDingtalkOpenPlatformConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, request_id=None):
        self.configs = configs  # type: list[ListDingtalkOpenPlatformConfigsResponseBodyConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDingtalkOpenPlatformConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ListDingtalkOpenPlatformConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDingtalkOpenPlatformConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDingtalkOpenPlatformConfigsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDingtalkOpenPlatformConfigsResponse, self).to_map()
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
            temp_model = ListDingtalkOpenPlatformConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtensionsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExtensionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExtensionsResponseBodyExtensions(TeaModel):
    def __init__(self, enabled=None, extension_desc=None, extension_documentation_link=None, extension_id=None,
                 extension_name=None):
        self.enabled = enabled  # type: str
        self.extension_desc = extension_desc  # type: str
        self.extension_documentation_link = extension_documentation_link  # type: str
        self.extension_id = extension_id  # type: str
        self.extension_name = extension_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExtensionsResponseBodyExtensions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc
        if self.extension_documentation_link is not None:
            result['ExtensionDocumentationLink'] = self.extension_documentation_link
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')
        if m.get('ExtensionDocumentationLink') is not None:
            self.extension_documentation_link = m.get('ExtensionDocumentationLink')
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')
        return self


class ListExtensionsResponseBody(TeaModel):
    def __init__(self, extensions=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.extensions = extensions  # type: list[ListExtensionsResponseBodyExtensions]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.extensions:
            for k in self.extensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExtensionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Extensions'] = []
        if self.extensions is not None:
            for k in self.extensions:
                result['Extensions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.extensions = []
        if m.get('Extensions') is not None:
            for k in m.get('Extensions'):
                temp_model = ListExtensionsResponseBodyExtensions()
                self.extensions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExtensionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExtensionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExtensionsResponse, self).to_map()
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
            temp_model = ListExtensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(self, auth_delta=None, file_id=None, keyword=None, mode=None, next_token=None, page_size=None,
                 prefix=None, space_id=None):
        self.auth_delta = auth_delta  # type: int
        self.file_id = file_id  # type: str
        self.keyword = keyword  # type: str
        self.mode = mode  # type: str
        self.next_token = next_token  # type: str
        self.page_size = page_size  # type: int
        self.prefix = prefix  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListFileResponseBodyDataList(TeaModel):
    def __init__(self, auth_delta=None, gmt_create=None, gmt_modified=None, id=None, name=None, size=None, type=None,
                 url=None):
        self.auth_delta = auth_delta  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.size = size  # type: int
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListFileResponseBodyPaginator(TeaModel):
    def __init__(self, next_token=None, page_size=None):
        self.next_token = next_token  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileResponseBodyPaginator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(self, data_list=None, paginator=None, request_id=None):
        self.data_list = data_list  # type: list[ListFileResponseBodyDataList]
        self.paginator = paginator  # type: ListFileResponseBodyPaginator
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super(ListFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFileResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFileResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFileResponse, self).to_map()
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionRequest(TeaModel):
    def __init__(self, filter_by=None, page_num=None, page_size=None, space_id=None):
        self.filter_by = filter_by  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListFunctionResponseBodyDataListSpec(TeaModel):
    def __init__(self, instance_concurrency=None, memory=None, runtime=None, timeout=None):
        self.instance_concurrency = instance_concurrency  # type: int
        self.memory = memory  # type: str
        self.runtime = runtime  # type: str
        self.timeout = timeout  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionResponseBodyDataListSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ListFunctionResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, desc=None, http_trigger_path=None, modified_at=None, name=None, spec=None,
                 timing_trigger_config=None):
        self.created_at = created_at  # type: str
        self.desc = desc  # type: str
        self.http_trigger_path = http_trigger_path  # type: str
        self.modified_at = modified_at  # type: str
        self.name = name  # type: str
        self.spec = spec  # type: ListFunctionResponseBodyDataListSpec
        self.timing_trigger_config = timing_trigger_config  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(ListFunctionResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Spec') is not None:
            temp_model = ListFunctionResponseBodyDataListSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        return self


class ListFunctionResponseBodyPaginator(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, total=None):
        self.page_count = page_count  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionResponseBodyPaginator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionResponseBody(TeaModel):
    def __init__(self, data_list=None, paginator=None, request_id=None):
        self.data_list = data_list  # type: list[ListFunctionResponseBodyDataList]
        self.paginator = paginator  # type: ListFunctionResponseBodyPaginator
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super(ListFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionResponse, self).to_map()
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
            temp_model = ListFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionDeploymentRequest(TeaModel):
    def __init__(self, name=None, page_num=None, page_size=None, space_id=None, status=None):
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_id = space_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionDeploymentResponseBodyDataListStatus(TeaModel):
    def __init__(self, label=None, status=None):
        self.label = label  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionDeploymentResponseBodyDataListStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionDeploymentResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, deployment_id=None, download_signed_url=None, modified_at=None, status=None,
                 version_no=None):
        self.created_at = created_at  # type: str
        self.deployment_id = deployment_id  # type: str
        self.download_signed_url = download_signed_url  # type: str
        self.modified_at = modified_at  # type: str
        self.status = status  # type: ListFunctionDeploymentResponseBodyDataListStatus
        self.version_no = version_no  # type: str

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(ListFunctionDeploymentResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Status') is not None:
            temp_model = ListFunctionDeploymentResponseBodyDataListStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        return self


class ListFunctionDeploymentResponseBodyPaginator(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, total=None):
        self.page_count = page_count  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionDeploymentResponseBodyPaginator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionDeploymentResponseBody(TeaModel):
    def __init__(self, data_list=None, paginator=None, request_id=None):
        self.data_list = data_list  # type: list[ListFunctionDeploymentResponseBodyDataList]
        self.paginator = paginator  # type: ListFunctionDeploymentResponseBodyPaginator
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super(ListFunctionDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionDeploymentResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionDeploymentResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionDeploymentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionDeploymentResponse, self).to_map()
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
            temp_model = ListFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionLogRequest(TeaModel):
    def __init__(self, from_date=None, log_request_id=None, name=None, page_num=None, page_size=None, space_id=None,
                 status=None, to_date=None):
        self.from_date = from_date  # type: long
        self.log_request_id = log_request_id  # type: str
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_id = space_id  # type: str
        self.status = status  # type: str
        self.to_date = to_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class ListFunctionLogResponseBodyDataList(TeaModel):
    def __init__(self, contents=None, function_name=None, levels=None, request_id=None, space_id=None, status=None,
                 timestamps=None):
        self.contents = contents  # type: list[str]
        self.function_name = function_name  # type: str
        self.levels = levels  # type: list[str]
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str
        self.status = status  # type: str
        self.timestamps = timestamps  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionLogResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        return self


class ListFunctionLogResponseBodyPaginator(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, total=None):
        self.page_count = page_count  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionLogResponseBodyPaginator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionLogResponseBody(TeaModel):
    def __init__(self, data_list=None, paginator=None, request_id=None):
        self.data_list = data_list  # type: list[ListFunctionLogResponseBodyDataList]
        self.paginator = paginator  # type: ListFunctionLogResponseBodyPaginator
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super(ListFunctionLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionLogResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionLogResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionLogResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionLogResponse, self).to_map()
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
            temp_model = ListFunctionLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenPlatformConfigRequest(TeaModel):
    def __init__(self, platform=None, space_id=None):
        self.platform = platform  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListOpenPlatformConfigResponseBodySecretList(TeaModel):
    def __init__(self, app_cert=None, app_id=None, app_secret=None, platform=None, private_key=None,
                 public_cert=None, public_key=None, root_cert=None, sign_mode=None, space_id=None):
        self.app_cert = app_cert  # type: str
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.platform = platform  # type: str
        self.private_key = private_key  # type: str
        self.public_cert = public_cert  # type: str
        self.public_key = public_key  # type: str
        self.root_cert = root_cert  # type: str
        self.sign_mode = sign_mode  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpenPlatformConfigResponseBodySecretList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_list=None):
        self.request_id = request_id  # type: str
        self.secret_list = secret_list  # type: list[ListOpenPlatformConfigResponseBodySecretList]

    def validate(self):
        if self.secret_list:
            for k in self.secret_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOpenPlatformConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecretList'] = []
        if self.secret_list is not None:
            for k in self.secret_list:
                result['SecretList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secret_list = []
        if m.get('SecretList') is not None:
            for k in m.get('SecretList'):
                temp_model = ListOpenPlatformConfigResponseBodySecretList()
                self.secret_list.append(temp_model.from_map(k))
        return self


class ListOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOpenPlatformConfigResponse, self).to_map()
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
            temp_model = ListOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpaceRequest(TeaModel):
    def __init__(self, emas_workspace_id=None, page_num=None, page_size=None, space_ids=None):
        self.emas_workspace_id = emas_workspace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_ids = space_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids is not None:
            result['SpaceIds'] = self.space_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids = m.get('SpaceIds')
        return self


class ListSpaceShrinkRequest(TeaModel):
    def __init__(self, emas_workspace_id=None, page_num=None, page_size=None, space_ids_shrink=None):
        self.emas_workspace_id = emas_workspace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.space_ids_shrink = space_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpaceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids_shrink is not None:
            result['SpaceIds'] = self.space_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids_shrink = m.get('SpaceIds')
        return self


class ListSpaceResponseBodySpaces(TeaModel):
    def __init__(self, desc=None, gmt_create=None, gmt_last_access=None, name=None, space_id=None, status=None):
        self.desc = desc  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_last_access = gmt_last_access  # type: long
        self.name = name  # type: str
        self.space_id = space_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpaceResponseBodySpaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_last_access is not None:
            result['GmtLastAccess'] = self.gmt_last_access
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtLastAccess') is not None:
            self.gmt_last_access = m.get('GmtLastAccess')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSpaceResponseBody(TeaModel):
    def __init__(self, count=None, gmt_create=None, request_id=None, spaces=None):
        self.count = count  # type: int
        self.gmt_create = gmt_create  # type: str
        self.request_id = request_id  # type: str
        self.spaces = spaces  # type: list[ListSpaceResponseBodySpaces]

    def validate(self):
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSpaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['Spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spaces = []
        if m.get('Spaces') is not None:
            for k in m.get('Spaces'):
                temp_model = ListSpaceResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ListSpaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSpaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSpaceResponse, self).to_map()
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
            temp_model = ListSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingCustomDomainsRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWebHostingCustomDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListWebHostingCustomDomainsResponseBodyData(TeaModel):
    def __init__(self, access_control_allow_origin=None, access_origin_control=None, cname=None, create_time=None,
                 description=None, domain=None, enable_cors=None, force_redirect_type=None, ssl_protocol=None, status=None,
                 update_time=None):
        self.access_control_allow_origin = access_control_allow_origin  # type: str
        self.access_origin_control = access_origin_control  # type: bool
        self.cname = cname  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.enable_cors = enable_cors  # type: bool
        self.force_redirect_type = force_redirect_type  # type: str
        self.ssl_protocol = ssl_protocol  # type: str
        self.status = status  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWebHostingCustomDomainsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWebHostingCustomDomainsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListWebHostingCustomDomainsResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWebHostingCustomDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWebHostingCustomDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWebHostingCustomDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWebHostingCustomDomainsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWebHostingCustomDomainsResponse, self).to_map()
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
            temp_model = ListWebHostingCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingFilesRequest(TeaModel):
    def __init__(self, marker=None, page_size=None, prefix=None, space_id=None):
        self.marker = marker  # type: str
        self.page_size = page_size  # type: int
        self.prefix = prefix  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWebHostingFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListWebHostingFilesResponseBodyDataWebHostingFiles(TeaModel):
    def __init__(self, content_type=None, etag=None, file_path=None, last_modified_time=None, signed_url=None,
                 size=None):
        self.content_type = content_type  # type: str
        self.etag = etag  # type: str
        self.file_path = file_path  # type: str
        self.last_modified_time = last_modified_time  # type: long
        self.signed_url = signed_url  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWebHostingFilesResponseBodyDataWebHostingFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListWebHostingFilesResponseBodyData(TeaModel):
    def __init__(self, count=None, next_marker=None, web_hosting_files=None):
        self.count = count  # type: int
        self.next_marker = next_marker  # type: str
        self.web_hosting_files = web_hosting_files  # type: list[ListWebHostingFilesResponseBodyDataWebHostingFiles]

    def validate(self):
        if self.web_hosting_files:
            for k in self.web_hosting_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWebHostingFilesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        result['WebHostingFiles'] = []
        if self.web_hosting_files is not None:
            for k in self.web_hosting_files:
                result['WebHostingFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        self.web_hosting_files = []
        if m.get('WebHostingFiles') is not None:
            for k in m.get('WebHostingFiles'):
                temp_model = ListWebHostingFilesResponseBodyDataWebHostingFiles()
                self.web_hosting_files.append(temp_model.from_map(k))
        return self


class ListWebHostingFilesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListWebHostingFilesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListWebHostingFilesResponseBody, self).to_map()
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
            temp_model = ListWebHostingFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWebHostingFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWebHostingFilesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWebHostingFilesResponse, self).to_map()
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
            temp_model = ListWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebHostingConfigRequest(TeaModel):
    def __init__(self, allowed_ips=None, error_http_status=None, error_path=None, index_path=None, space_id=None):
        self.allowed_ips = allowed_ips  # type: str
        self.error_http_status = error_http_status  # type: str
        self.error_path = error_path  # type: str
        self.index_path = index_path  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebHostingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        if self.error_http_status is not None:
            result['ErrorHttpStatus'] = self.error_http_status
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        if m.get('ErrorHttpStatus') is not None:
            self.error_http_status = m.get('ErrorHttpStatus')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ModifyWebHostingConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebHostingConfigResponseBody, self).to_map()
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


class ModifyWebHostingConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebHostingConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebHostingConfigResponse, self).to_map()
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
            temp_model = ModifyWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenServiceRequest(TeaModel):
    def __init__(self, service_name=None, space_id=None):
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class OpenServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenServiceResponseBody, self).to_map()
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


class OpenServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenServiceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenServiceResponse, self).to_map()
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
            temp_model = OpenServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenWebHostingServiceRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenWebHostingServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class OpenWebHostingServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenWebHostingServiceResponseBody, self).to_map()
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


class OpenWebHostingServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenWebHostingServiceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenWebHostingServiceResponse, self).to_map()
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
            temp_model = OpenWebHostingServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupCollectionsRequest(TeaModel):
    def __init__(self, backup_id=None, space_id=None):
        self.backup_id = backup_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBBackupCollectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryDBBackupCollectionsResponseBody(TeaModel):
    def __init__(self, collections=None, request_id=None):
        self.collections = collections  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBBackupCollectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDBBackupCollectionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDBBackupCollectionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDBBackupCollectionsResponse, self).to_map()
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
            temp_model = QueryDBBackupCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupDumpTimesRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBBackupDumpTimesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryDBBackupDumpTimesResponseBodyBackupDumpTimes(TeaModel):
    def __init__(self, backup_id=None, dump_time=None):
        self.backup_id = backup_id  # type: str
        self.dump_time = dump_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBBackupDumpTimesResponseBodyBackupDumpTimes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dump_time is not None:
            result['DumpTime'] = self.dump_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DumpTime') is not None:
            self.dump_time = m.get('DumpTime')
        return self


class QueryDBBackupDumpTimesResponseBody(TeaModel):
    def __init__(self, backup_dump_times=None, request_id=None):
        self.backup_dump_times = backup_dump_times  # type: list[QueryDBBackupDumpTimesResponseBodyBackupDumpTimes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.backup_dump_times:
            for k in self.backup_dump_times:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDBBackupDumpTimesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupDumpTimes'] = []
        if self.backup_dump_times is not None:
            for k in self.backup_dump_times:
                result['BackupDumpTimes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_dump_times = []
        if m.get('BackupDumpTimes') is not None:
            for k in m.get('BackupDumpTimes'):
                temp_model = QueryDBBackupDumpTimesResponseBodyBackupDumpTimes()
                self.backup_dump_times.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDBBackupDumpTimesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDBBackupDumpTimesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDBBackupDumpTimesResponse, self).to_map()
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
            temp_model = QueryDBBackupDumpTimesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBExportTaskStatusRequest(TeaModel):
    def __init__(self, space_id=None, task_id=None):
        self.space_id = space_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBExportTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBExportTaskStatusResponseBody(TeaModel):
    def __init__(self, detail_message=None, download_url=None, exported_count=None, request_id=None, status=None):
        self.detail_message = detail_message  # type: str
        self.download_url = download_url  # type: str
        self.exported_count = exported_count  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBExportTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.exported_count is not None:
            result['ExportedCount'] = self.exported_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExportedCount') is not None:
            self.exported_count = m.get('ExportedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDBExportTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDBExportTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDBExportTaskStatusResponse, self).to_map()
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
            temp_model = QueryDBExportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBImportTaskStatusRequest(TeaModel):
    def __init__(self, space_id=None, task_id=None):
        self.space_id = space_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBImportTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBImportTaskStatusResponseBody(TeaModel):
    def __init__(self, detail_message=None, failed_count=None, request_id=None, status=None, success_count=None):
        self.detail_message = detail_message  # type: str
        self.failed_count = failed_count  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success_count = success_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBImportTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBImportTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDBImportTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDBImportTaskStatusResponse, self).to_map()
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
            temp_model = QueryDBImportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBRestoreTaskStatusRequest(TeaModel):
    def __init__(self, space_id=None, task_id=None):
        self.space_id = space_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBRestoreTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBRestoreTaskStatusResponseBody(TeaModel):
    def __init__(self, detail_message=None, failed_count=None, request_id=None, status=None, success_count=None):
        self.detail_message = detail_message  # type: str
        self.failed_count = failed_count  # type: long
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success_count = success_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDBRestoreTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBRestoreTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDBRestoreTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDBRestoreTaskStatusResponse, self).to_map()
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
            temp_model = QueryDBRestoreTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServiceStatusRequest(TeaModel):
    def __init__(self, service_name=None, space_id=None):
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryServiceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, service_status=None):
        self.request_id = request_id  # type: str
        self.service_status = service_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class QueryServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryServiceStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryServiceStatusResponse, self).to_map()
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
            temp_model = QueryServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceConsumptionRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceConsumptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QuerySpaceConsumptionResponseBodyCsUsage(TeaModel):
    def __init__(self, cdn_traffic=None, download_count=None, storage_size=None, upload_count=None):
        self.cdn_traffic = cdn_traffic  # type: long
        self.download_count = download_count  # type: long
        self.storage_size = storage_size  # type: long
        self.upload_count = upload_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponseBodyCsUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.download_count is not None:
            result['DownloadCount'] = self.download_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upload_count is not None:
            result['UploadCount'] = self.upload_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UploadCount') is not None:
            self.upload_count = m.get('UploadCount')
        return self


class QuerySpaceConsumptionResponseBodyDbUsage(TeaModel):
    def __init__(self, read_count=None, storage_size=None, write_count=None):
        self.read_count = read_count  # type: long
        self.storage_size = storage_size  # type: long
        self.write_count = write_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponseBodyDbUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.write_count is not None:
            result['WriteCount'] = self.write_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')
        return self


class QuerySpaceConsumptionResponseBodyFcUsage(TeaModel):
    def __init__(self, cost=None, request_count=None, tx_traffic=None):
        self.cost = cost  # type: long
        self.request_count = request_count  # type: long
        self.tx_traffic = tx_traffic  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponseBodyFcUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tx_traffic is not None:
            result['TxTraffic'] = self.tx_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TxTraffic') is not None:
            self.tx_traffic = m.get('TxTraffic')
        return self


class QuerySpaceConsumptionResponseBodyWhUsage(TeaModel):
    def __init__(self, cdn_traffic=None, storage_size=None):
        self.cdn_traffic = cdn_traffic  # type: long
        self.storage_size = storage_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponseBodyWhUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class QuerySpaceConsumptionResponseBody(TeaModel):
    def __init__(self, cs_usage=None, cycle_end_time=None, cycle_start_time=None, db_usage=None, fc_usage=None,
                 gmt_create=None, request_id=None, space_id=None, spec_code=None, wh_usage=None):
        self.cs_usage = cs_usage  # type: QuerySpaceConsumptionResponseBodyCsUsage
        self.cycle_end_time = cycle_end_time  # type: long
        self.cycle_start_time = cycle_start_time  # type: long
        self.db_usage = db_usage  # type: QuerySpaceConsumptionResponseBodyDbUsage
        self.fc_usage = fc_usage  # type: QuerySpaceConsumptionResponseBodyFcUsage
        self.gmt_create = gmt_create  # type: str
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str
        self.spec_code = spec_code  # type: str
        self.wh_usage = wh_usage  # type: QuerySpaceConsumptionResponseBodyWhUsage

    def validate(self):
        if self.cs_usage:
            self.cs_usage.validate()
        if self.db_usage:
            self.db_usage.validate()
        if self.fc_usage:
            self.fc_usage.validate()
        if self.wh_usage:
            self.wh_usage.validate()

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_usage is not None:
            result['CsUsage'] = self.cs_usage.to_map()
        if self.cycle_end_time is not None:
            result['CycleEndTime'] = self.cycle_end_time
        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time
        if self.db_usage is not None:
            result['DbUsage'] = self.db_usage.to_map()
        if self.fc_usage is not None:
            result['FcUsage'] = self.fc_usage.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.wh_usage is not None:
            result['WhUsage'] = self.wh_usage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CsUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyCsUsage()
            self.cs_usage = temp_model.from_map(m['CsUsage'])
        if m.get('CycleEndTime') is not None:
            self.cycle_end_time = m.get('CycleEndTime')
        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')
        if m.get('DbUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyDbUsage()
            self.db_usage = temp_model.from_map(m['DbUsage'])
        if m.get('FcUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyFcUsage()
            self.fc_usage = temp_model.from_map(m['FcUsage'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('WhUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyWhUsage()
            self.wh_usage = temp_model.from_map(m['WhUsage'])
        return self


class QuerySpaceConsumptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySpaceConsumptionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySpaceConsumptionResponse, self).to_map()
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
            temp_model = QuerySpaceConsumptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceSpecDetailRequest(TeaModel):
    def __init__(self, spec_code=None):
        self.spec_code = spec_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceSpecDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        return self


class QuerySpaceSpecDetailResponseBody(TeaModel):
    def __init__(self, cs_cdn_traffic=None, cs_download_count=None, cs_storage_size=None, cs_upload_count=None,
                 db_read_count=None, db_storage_size=None, db_write_count=None, fc_cost=None, fc_request_count=None,
                 fc_tx_traffic=None, gmt_create=None, request_id=None, spec_code=None, spec_detail_text=None, wh_cdn_traffic=None,
                 wh_storage_size=None):
        self.cs_cdn_traffic = cs_cdn_traffic  # type: long
        self.cs_download_count = cs_download_count  # type: long
        self.cs_storage_size = cs_storage_size  # type: long
        self.cs_upload_count = cs_upload_count  # type: long
        self.db_read_count = db_read_count  # type: long
        self.db_storage_size = db_storage_size  # type: long
        self.db_write_count = db_write_count  # type: long
        self.fc_cost = fc_cost  # type: long
        self.fc_request_count = fc_request_count  # type: long
        self.fc_tx_traffic = fc_tx_traffic  # type: long
        self.gmt_create = gmt_create  # type: str
        self.request_id = request_id  # type: str
        self.spec_code = spec_code  # type: str
        self.spec_detail_text = spec_detail_text  # type: str
        self.wh_cdn_traffic = wh_cdn_traffic  # type: long
        self.wh_storage_size = wh_storage_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceSpecDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_cdn_traffic is not None:
            result['CsCdnTraffic'] = self.cs_cdn_traffic
        if self.cs_download_count is not None:
            result['CsDownloadCount'] = self.cs_download_count
        if self.cs_storage_size is not None:
            result['CsStorageSize'] = self.cs_storage_size
        if self.cs_upload_count is not None:
            result['CsUploadCount'] = self.cs_upload_count
        if self.db_read_count is not None:
            result['DbReadCount'] = self.db_read_count
        if self.db_storage_size is not None:
            result['DbStorageSize'] = self.db_storage_size
        if self.db_write_count is not None:
            result['DbWriteCount'] = self.db_write_count
        if self.fc_cost is not None:
            result['FcCost'] = self.fc_cost
        if self.fc_request_count is not None:
            result['FcRequestCount'] = self.fc_request_count
        if self.fc_tx_traffic is not None:
            result['FcTxTraffic'] = self.fc_tx_traffic
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.spec_detail_text is not None:
            result['SpecDetailText'] = self.spec_detail_text
        if self.wh_cdn_traffic is not None:
            result['WhCdnTraffic'] = self.wh_cdn_traffic
        if self.wh_storage_size is not None:
            result['WhStorageSize'] = self.wh_storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CsCdnTraffic') is not None:
            self.cs_cdn_traffic = m.get('CsCdnTraffic')
        if m.get('CsDownloadCount') is not None:
            self.cs_download_count = m.get('CsDownloadCount')
        if m.get('CsStorageSize') is not None:
            self.cs_storage_size = m.get('CsStorageSize')
        if m.get('CsUploadCount') is not None:
            self.cs_upload_count = m.get('CsUploadCount')
        if m.get('DbReadCount') is not None:
            self.db_read_count = m.get('DbReadCount')
        if m.get('DbStorageSize') is not None:
            self.db_storage_size = m.get('DbStorageSize')
        if m.get('DbWriteCount') is not None:
            self.db_write_count = m.get('DbWriteCount')
        if m.get('FcCost') is not None:
            self.fc_cost = m.get('FcCost')
        if m.get('FcRequestCount') is not None:
            self.fc_request_count = m.get('FcRequestCount')
        if m.get('FcTxTraffic') is not None:
            self.fc_tx_traffic = m.get('FcTxTraffic')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('SpecDetailText') is not None:
            self.spec_detail_text = m.get('SpecDetailText')
        if m.get('WhCdnTraffic') is not None:
            self.wh_cdn_traffic = m.get('WhCdnTraffic')
        if m.get('WhStorageSize') is not None:
            self.wh_storage_size = m.get('WhStorageSize')
        return self


class QuerySpaceSpecDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySpaceSpecDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySpaceSpecDetailResponse, self).to_map()
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
            temp_model = QuerySpaceSpecDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceUsageRequest(TeaModel):
    def __init__(self, end_time=None, interval=None, space_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.interval = interval  # type: int
        self.space_id = space_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage(TeaModel):
    def __init__(self, cdn_traffic=None, download_count=None, storage_size=None, upload_count=None):
        self.cdn_traffic = cdn_traffic  # type: long
        self.download_count = download_count  # type: long
        self.storage_size = storage_size  # type: long
        self.upload_count = upload_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.download_count is not None:
            result['DownloadCount'] = self.download_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upload_count is not None:
            result['UploadCount'] = self.upload_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UploadCount') is not None:
            self.upload_count = m.get('UploadCount')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage(TeaModel):
    def __init__(self, read_count=None, storage_size=None, write_count=None):
        self.read_count = read_count  # type: long
        self.storage_size = storage_size  # type: long
        self.write_count = write_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.write_count is not None:
            result['WriteCount'] = self.write_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage(TeaModel):
    def __init__(self, cost=None, request_count=None, tx_traffic=None):
        self.cost = cost  # type: long
        self.request_count = request_count  # type: long
        self.tx_traffic = tx_traffic  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tx_traffic is not None:
            result['TxTraffic'] = self.tx_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TxTraffic') is not None:
            self.tx_traffic = m.get('TxTraffic')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage(TeaModel):
    def __init__(self, cdn_traffic=None, storage_size=None):
        self.cdn_traffic = cdn_traffic  # type: long
        self.storage_size = storage_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataList(TeaModel):
    def __init__(self, cs_usage=None, db_usage=None, effective_bill_flag=None, fc_usage=None, timestamp=None,
                 wh_usage=None):
        self.cs_usage = cs_usage  # type: QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage
        self.db_usage = db_usage  # type: QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage
        # 标记该数据是否出账。
        # - true：正常出账。
        # - false：不出账，例如在空间停服的情况下，用量数据不用于出账。
        self.effective_bill_flag = effective_bill_flag  # type: bool
        self.fc_usage = fc_usage  # type: QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage
        self.timestamp = timestamp  # type: str
        self.wh_usage = wh_usage  # type: QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage

    def validate(self):
        if self.cs_usage:
            self.cs_usage.validate()
        if self.db_usage:
            self.db_usage.validate()
        if self.fc_usage:
            self.fc_usage.validate()
        if self.wh_usage:
            self.wh_usage.validate()

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBodySpaceUsageDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_usage is not None:
            result['CsUsage'] = self.cs_usage.to_map()
        if self.db_usage is not None:
            result['DbUsage'] = self.db_usage.to_map()
        if self.effective_bill_flag is not None:
            result['EffectiveBillFlag'] = self.effective_bill_flag
        if self.fc_usage is not None:
            result['FcUsage'] = self.fc_usage.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.wh_usage is not None:
            result['WhUsage'] = self.wh_usage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CsUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage()
            self.cs_usage = temp_model.from_map(m['CsUsage'])
        if m.get('DbUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage()
            self.db_usage = temp_model.from_map(m['DbUsage'])
        if m.get('EffectiveBillFlag') is not None:
            self.effective_bill_flag = m.get('EffectiveBillFlag')
        if m.get('FcUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage()
            self.fc_usage = temp_model.from_map(m['FcUsage'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('WhUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage()
            self.wh_usage = temp_model.from_map(m['WhUsage'])
        return self


class QuerySpaceUsageResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, space_id=None, space_usage_data_list=None, start_time=None):
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.space_id = space_id  # type: str
        self.space_usage_data_list = space_usage_data_list  # type: list[QuerySpaceUsageResponseBodySpaceUsageDataList]
        self.start_time = start_time  # type: str

    def validate(self):
        if self.space_usage_data_list:
            for k in self.space_usage_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySpaceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        result['SpaceUsageDataList'] = []
        if self.space_usage_data_list is not None:
            for k in self.space_usage_data_list:
                result['SpaceUsageDataList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        self.space_usage_data_list = []
        if m.get('SpaceUsageDataList') is not None:
            for k in m.get('SpaceUsageDataList'):
                temp_model = QuerySpaceUsageResponseBodySpaceUsageDataList()
                self.space_usage_data_list.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySpaceUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySpaceUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySpaceUsageResponse, self).to_map()
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
            temp_model = QuerySpaceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebHostingCustomDomainCacheRequest(TeaModel):
    def __init__(self, domain_name=None, space_id=None):
        self.domain_name = domain_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebHostingCustomDomainCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RefreshWebHostingCustomDomainCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebHostingCustomDomainCacheResponseBody, self).to_map()
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


class RefreshWebHostingCustomDomainCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshWebHostingCustomDomainCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshWebHostingCustomDomainCacheResponse, self).to_map()
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
            temp_model = RefreshWebHostingCustomDomainCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterFileRequest(TeaModel):
    def __init__(self, id=None, space_id=None):
        self.id = id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RegisterFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterFileResponseBody, self).to_map()
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


class RegisterFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterFileResponse, self).to_map()
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
            temp_model = RegisterFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDBCollectionRequest(TeaModel):
    def __init__(self, new_collection=None, origin_collection=None, space_id=None):
        self.new_collection = new_collection  # type: str
        self.origin_collection = origin_collection  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenameDBCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_collection is not None:
            result['NewCollection'] = self.new_collection
        if self.origin_collection is not None:
            result['OriginCollection'] = self.origin_collection
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewCollection') is not None:
            self.new_collection = m.get('NewCollection')
        if m.get('OriginCollection') is not None:
            self.origin_collection = m.get('OriginCollection')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RenameDBCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenameDBCollectionResponseBody, self).to_map()
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


class RenameDBCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenameDBCollectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenameDBCollectionResponse, self).to_map()
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
            temp_model = RenameDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetServerSecretRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetServerSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ResetServerSecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetServerSecretResponseBody, self).to_map()
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


class ResetServerSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetServerSecretResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetServerSecretResponse, self).to_map()
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
            temp_model = ResetServerSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDBCommandRequest(TeaModel):
    def __init__(self, body=None, space_id=None):
        self.body = body  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunDBCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RunDBCommandResponseBody(TeaModel):
    def __init__(self, affected_docs=None, request_id=None, result=None):
        self.affected_docs = affected_docs  # type: int
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunDBCommandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_docs is not None:
            result['AffectedDocs'] = self.affected_docs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AffectedDocs') is not None:
            self.affected_docs = m.get('AffectedDocs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RunDBCommandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RunDBCommandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunDBCommandResponse, self).to_map()
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
            temp_model = RunDBCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunFunctionRequest(TeaModel):
    def __init__(self, body=None, space_id=None):
        self.body = body  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RunFunctionResponseBodyRuntimeMeta(TeaModel):
    def __init__(self, billing_duration=None, invocation_duration=None, max_memory_usage=None, request_id=None):
        self.billing_duration = billing_duration  # type: int
        self.invocation_duration = invocation_duration  # type: int
        self.max_memory_usage = max_memory_usage  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunFunctionResponseBodyRuntimeMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_duration is not None:
            result['BillingDuration'] = self.billing_duration
        if self.invocation_duration is not None:
            result['InvocationDuration'] = self.invocation_duration
        if self.max_memory_usage is not None:
            result['MaxMemoryUsage'] = self.max_memory_usage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingDuration') is not None:
            self.billing_duration = m.get('BillingDuration')
        if m.get('InvocationDuration') is not None:
            self.invocation_duration = m.get('InvocationDuration')
        if m.get('MaxMemoryUsage') is not None:
            self.max_memory_usage = m.get('MaxMemoryUsage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunFunctionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, runtime_meta=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.runtime_meta = runtime_meta  # type: RunFunctionResponseBodyRuntimeMeta

    def validate(self):
        if self.runtime_meta:
            self.runtime_meta.validate()

    def to_map(self):
        _map = super(RunFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.runtime_meta is not None:
            result['RuntimeMeta'] = self.runtime_meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RuntimeMeta') is not None:
            temp_model = RunFunctionResponseBodyRuntimeMeta()
            self.runtime_meta = temp_model.from_map(m['RuntimeMeta'])
        return self


class RunFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RunFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunFunctionResponse, self).to_map()
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
            temp_model = RunFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAntOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_cert=None, app_id=None, private_key=None, public_cert=None, public_key=None,
                 root_cert=None, sign_mode=None, space_id=None):
        self.app_cert = app_cert  # type: str
        self.app_id = app_id  # type: str
        self.private_key = private_key  # type: str
        self.public_cert = public_cert  # type: str
        self.public_key = public_key  # type: str
        self.root_cert = root_cert  # type: str
        self.sign_mode = sign_mode  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveAntOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveAntOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveAntOpenPlatformConfigResponseBody, self).to_map()
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


class SaveAntOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveAntOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveAntOpenPlatformConfigResponse, self).to_map()
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
            temp_model = SaveAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAppAuthTokenRequest(TeaModel):
    def __init__(self, app_auth_token=None, app_id=None, isv_app_id=None, space_id=None):
        self.app_auth_token = app_auth_token  # type: str
        self.app_id = app_id  # type: str
        self.isv_app_id = isv_app_id  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveAppAuthTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_auth_token is not None:
            result['AppAuthToken'] = self.app_auth_token
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.isv_app_id is not None:
            result['IsvAppId'] = self.isv_app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppAuthToken') is not None:
            self.app_auth_token = m.get('AppAuthToken')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IsvAppId') is not None:
            self.isv_app_id = m.get('IsvAppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveAppAuthTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveAppAuthTokenResponseBody, self).to_map()
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


class SaveAppAuthTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveAppAuthTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveAppAuthTokenResponse, self).to_map()
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
            temp_model = SaveAppAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveCdnDomainConfigRequest(TeaModel):
    def __init__(self, auth_config=None, cors_config=None, ip_config=None, referer_config=None, space_id=None,
                 tenant_id=None, type=None, ua_config=None):
        self.auth_config = auth_config  # type: str
        self.cors_config = cors_config  # type: str
        self.ip_config = ip_config  # type: str
        self.referer_config = referer_config  # type: str
        self.space_id = space_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.ua_config = ua_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveCdnDomainConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config
        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config
        if self.ip_config is not None:
            result['IpConfig'] = self.ip_config
        if self.referer_config is not None:
            result['RefererConfig'] = self.referer_config
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.ua_config is not None:
            result['UaConfig'] = self.ua_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            self.auth_config = m.get('AuthConfig')
        if m.get('CorsConfig') is not None:
            self.cors_config = m.get('CorsConfig')
        if m.get('IpConfig') is not None:
            self.ip_config = m.get('IpConfig')
        if m.get('RefererConfig') is not None:
            self.referer_config = m.get('RefererConfig')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UaConfig') is not None:
            self.ua_config = m.get('UaConfig')
        return self


class SaveCdnDomainConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveCdnDomainConfigResponseBody, self).to_map()
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


class SaveCdnDomainConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveCdnDomainConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveCdnDomainConfigResponse, self).to_map()
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
            temp_model = SaveCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainConfigRequest(TeaModel):
    def __init__(self, domain_name=None, force_redirect_type=None, space_id=None):
        self.domain_name = domain_name  # type: str
        self.force_redirect_type = force_redirect_type  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWebHostingCustomDomainConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainConfigResponseBody, self).to_map()
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


class SaveWebHostingCustomDomainConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveWebHostingCustomDomainConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainConfigResponse, self).to_map()
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
            temp_model = SaveWebHostingCustomDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainCorsConfigRequest(TeaModel):
    def __init__(self, access_control_allow_origin=None, access_origin_control=None, domain_name=None,
                 enable_cors=None, space_id=None):
        self.access_control_allow_origin = access_control_allow_origin  # type: str
        self.access_origin_control = access_origin_control  # type: bool
        self.domain_name = domain_name  # type: str
        self.enable_cors = enable_cors  # type: bool
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainCorsConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWebHostingCustomDomainCorsConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainCorsConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveWebHostingCustomDomainCorsConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveWebHostingCustomDomainCorsConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveWebHostingCustomDomainCorsConfigResponse, self).to_map()
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
            temp_model = SaveWebHostingCustomDomainCorsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, app_secret=None, space_id=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWechatOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWechatOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveWechatOpenPlatformConfigResponseBody, self).to_map()
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


class SaveWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveWechatOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveWechatOpenPlatformConfigResponse, self).to_map()
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
            temp_model = SaveWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindWebHostingCustomDomainRequest(TeaModel):
    def __init__(self, custom_domain=None, space_id=None):
        self.custom_domain = custom_domain  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindWebHostingCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UnbindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindWebHostingCustomDomainResponseBody, self).to_map()
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


class UnbindWebHostingCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindWebHostingCustomDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindWebHostingCustomDomainResponse, self).to_map()
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
            temp_model = UnbindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(self, app_id=None, app_secret=None, space_id=None):
        self.app_id = app_id  # type: str
        self.app_secret = app_secret  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDingtalkOpenPlatformConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateDingtalkOpenPlatformConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDingtalkOpenPlatformConfigResponseBody, self).to_map()
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


class UpdateDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDingtalkOpenPlatformConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDingtalkOpenPlatformConfigResponse, self).to_map()
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
            temp_model = UpdateDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(self, desc=None, http_trigger_path=None, instance_concurrency=None, memory=None, name=None,
                 runtime=None, space_id=None, timeout=None, timing_trigger_config=None, timing_trigger_user_payload=None):
        self.desc = desc  # type: str
        self.http_trigger_path = http_trigger_path  # type: str
        self.instance_concurrency = instance_concurrency  # type: int
        self.memory = memory  # type: int
        self.name = name  # type: str
        self.runtime = runtime  # type: str
        self.space_id = space_id  # type: str
        self.timeout = timeout  # type: int
        self.timing_trigger_config = timing_trigger_config  # type: str
        self.timing_trigger_user_payload = timing_trigger_user_payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class UpdateFunctionResponseBodySpec(TeaModel):
    def __init__(self, instance_concurrency=None, memory=None, runtime=None, timeout=None):
        self.instance_concurrency = instance_concurrency  # type: int
        self.memory = memory  # type: str
        self.runtime = runtime  # type: str
        self.timeout = timeout  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionResponseBodySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(self, created_at=None, desc=None, http_trigger_path=None, modified_at=None, name=None,
                 request_id=None, spec=None, timing_trigger_config=None, timing_trigger_user_payload=None):
        self.created_at = created_at  # type: str
        self.desc = desc  # type: str
        self.http_trigger_path = http_trigger_path  # type: str
        self.modified_at = modified_at  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.spec = spec  # type: UpdateFunctionResponseBodySpec
        self.timing_trigger_config = timing_trigger_config  # type: str
        self.timing_trigger_user_payload = timing_trigger_user_payload  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(UpdateFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = UpdateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFunctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionResponse, self).to_map()
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
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpTriggerConfigRequest(TeaModel):
    def __init__(self, custom_domain=None, custom_domain_certificate=None, custom_domain_private_key=None,
                 enable_service=None, space_id=None):
        self.custom_domain = custom_domain  # type: str
        self.custom_domain_certificate = custom_domain_certificate  # type: str
        self.custom_domain_private_key = custom_domain_private_key  # type: str
        self.enable_service = enable_service  # type: bool
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHttpTriggerConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate is not None:
            result['CustomDomainCertificate'] = self.custom_domain_certificate
        if self.custom_domain_private_key is not None:
            result['CustomDomainPrivateKey'] = self.custom_domain_private_key
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificate') is not None:
            self.custom_domain_certificate = m.get('CustomDomainCertificate')
        if m.get('CustomDomainPrivateKey') is not None:
            self.custom_domain_private_key = m.get('CustomDomainPrivateKey')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateHttpTriggerConfigResponseBody(TeaModel):
    def __init__(self, custom_domain=None, custom_domain_certificate_info=None, custom_domain_cname=None,
                 default_endpoint=None, enable_service=None, request_id=None):
        self.custom_domain = custom_domain  # type: str
        self.custom_domain_certificate_info = custom_domain_certificate_info  # type: str
        self.custom_domain_cname = custom_domain_cname  # type: str
        self.default_endpoint = default_endpoint  # type: str
        self.enable_service = enable_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHttpTriggerConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateHttpTriggerConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHttpTriggerConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHttpTriggerConfigResponse, self).to_map()
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
            temp_model = UpdateHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServicePolicyRequest(TeaModel):
    def __init__(self, collection_name=None, policy=None, policy_name=None, service_name=None, space_id=None):
        self.collection_name = collection_name  # type: str
        self.policy = policy  # type: str
        self.policy_name = policy_name  # type: str
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServicePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateServicePolicyResponseBody(TeaModel):
    def __init__(self, collection_name=None, policy=None, policy_name=None, request_id=None, service_name=None,
                 space_id=None):
        self.collection_name = collection_name  # type: str
        self.policy = policy  # type: str
        self.policy_name = policy_name  # type: str
        self.request_id = request_id  # type: str
        self.service_name = service_name  # type: str
        self.space_id = space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServicePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateServicePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServicePolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServicePolicyResponse, self).to_map()
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
            temp_model = UpdateServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSpaceRequest(TeaModel):
    def __init__(self, desc=None, space_id=None, status=None):
        self.desc = desc  # type: str
        self.space_id = space_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSpaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateSpaceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSpaceResponseBody, self).to_map()
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


class UpdateSpaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSpaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSpaceResponse, self).to_map()
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
            temp_model = UpdateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWebHostingDomainOwnerRequest(TeaModel):
    def __init__(self, domain=None, space_id=None, verify_type=None):
        self.domain = domain  # type: str
        self.space_id = space_id  # type: str
        self.verify_type = verify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyWebHostingDomainOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyWebHostingDomainOwnerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyWebHostingDomainOwnerResponseBody, self).to_map()
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


class VerifyWebHostingDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyWebHostingDomainOwnerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyWebHostingDomainOwnerResponse, self).to_map()
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
            temp_model = VerifyWebHostingDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


