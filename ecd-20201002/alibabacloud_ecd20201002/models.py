# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApproveFotaUpdateRequest(TeaModel):
    def __init__(self, app_version=None, client_id=None, desktop_id=None, login_token=None, region_id=None,
                 session_id=None, uuid=None):
        self.app_version = app_version  # type: str
        self.client_id = client_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveFotaUpdateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApproveFotaUpdateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveFotaUpdateResponseBody, self).to_map()
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


class ApproveFotaUpdateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApproveFotaUpdateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApproveFotaUpdateResponse, self).to_map()
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
            temp_model = ApproveFotaUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(self, client_id=None, end_user_id=None, login_token=None, new_password=None, office_site_id=None,
                 old_password=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.login_token = login_token  # type: str
        self.new_password = new_password  # type: str
        self.office_site_id = office_site_id  # type: str
        self.old_password = old_password  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangePasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ChangePasswordResponseBody(TeaModel):
    def __init__(self, login_token=None, request_id=None):
        self.login_token = login_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangePasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangePasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangePasswordResponse, self).to_map()
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
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFingerPrintTemplateRequest(TeaModel):
    def __init__(self, client_id=None, client_token=None, index=None, login_token=None, region_id=None,
                 session_id=None):
        self.client_id = client_id  # type: str
        self.client_token = client_token  # type: str
        self.index = index  # type: int
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFingerPrintTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.index is not None:
            result['Index'] = self.index
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DeleteFingerPrintTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFingerPrintTemplateResponseBody, self).to_map()
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


class DeleteFingerPrintTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFingerPrintTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFingerPrintTemplateResponse, self).to_map()
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
            temp_model = DeleteFingerPrintTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, client_id=None, directory_id=None, region_id=None):
        self.client_id = client_id  # type: str
        self.directory_id = directory_id  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(self, desktop_access_type=None, directory_id=None, directory_type=None, provider_id=None,
                 sso_service_url=None):
        self.desktop_access_type = desktop_access_type  # type: str
        self.directory_id = directory_id  # type: str
        self.directory_type = directory_type  # type: str
        self.provider_id = provider_id  # type: str
        self.sso_service_url = sso_service_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(self, directories=None, request_id=None):
        self.directories = directories  # type: list[DescribeDirectoriesResponseBodyDirectories]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDirectoriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponse, self).to_map()
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
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFingerPrintTemplatesRequest(TeaModel):
    def __init__(self, client_id=None, login_token=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFingerPrintTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates(TeaModel):
    def __init__(self, client_id=None, creation_time=None, description=None, end_user_id=None, index=None,
                 login_time=None, office_site_id=None):
        self.client_id = client_id  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.end_user_id = end_user_id  # type: str
        self.index = index  # type: long
        self.login_time = login_time  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.index is not None:
            result['Index'] = self.index
        if self.login_time is not None:
            result['LoginTime'] = self.login_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DescribeFingerPrintTemplatesResponseBody(TeaModel):
    def __init__(self, finger_print_templates=None, request_id=None):
        self.finger_print_templates = finger_print_templates  # type: list[DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.finger_print_templates:
            for k in self.finger_print_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFingerPrintTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FingerPrintTemplates'] = []
        if self.finger_print_templates is not None:
            for k in self.finger_print_templates:
                result['FingerPrintTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.finger_print_templates = []
        if m.get('FingerPrintTemplates') is not None:
            for k in m.get('FingerPrintTemplates'):
                temp_model = DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates()
                self.finger_print_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFingerPrintTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFingerPrintTemplatesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFingerPrintTemplatesResponse, self).to_map()
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
            temp_model = DescribeFingerPrintTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDesktopsRequest(TeaModel):
    def __init__(self, client_id=None, desktop_access_type=None, desktop_id=None, desktop_name=None,
                 desktop_status=None, directory_id=None, keyword=None, login_region_id=None, login_token=None, max_results=None,
                 next_token=None, office_site_id=None, order_by=None, query_fota_update=None, region_id=None,
                 search_region_id=None, session_id=None, sort_type=None, without_latency=None):
        self.client_id = client_id  # type: str
        self.desktop_access_type = desktop_access_type  # type: str
        self.desktop_id = desktop_id  # type: list[str]
        self.desktop_name = desktop_name  # type: str
        self.desktop_status = desktop_status  # type: str
        self.directory_id = directory_id  # type: str
        # 关键字。支持模糊搜索桌面ID、云桌面名称和终端用户自定义的桌面名称。
        self.keyword = keyword  # type: str
        self.login_region_id = login_region_id  # type: str
        self.login_token = login_token  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.order_by = order_by  # type: str
        self.query_fota_update = query_fota_update  # type: bool
        self.region_id = region_id  # type: str
        self.search_region_id = search_region_id  # type: str
        self.session_id = session_id  # type: str
        self.sort_type = sort_type  # type: str
        self.without_latency = without_latency  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.without_latency is not None:
            result['WithoutLatency'] = self.without_latency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('WithoutLatency') is not None:
            self.without_latency = m.get('WithoutLatency')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsClients(TeaModel):
    def __init__(self, client_type=None, status=None):
        # 客户端类型，取值：
        # 
        # - macos：Mac客户端
        # - ios：IOS客户端
        # - android：Android客户端
        # - html5：Web客户端
        # - windows：Windows客户端
        # - linux：Linux客户端
        self.client_type = client_type  # type: str
        # 客户端状态，取值：
        # 
        # - ON：允许登录
        # - OFF：不允许登录
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktopsClients, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers(TeaModel):
    def __init__(self, allow_client_setting=None, cron_expression=None, enforce=None, execution_time=None,
                 interval=None, operation_type=None, reset_type=None, timer_type=None):
        self.allow_client_setting = allow_client_setting  # type: bool
        self.cron_expression = cron_expression  # type: str
        self.enforce = enforce  # type: bool
        self.execution_time = execution_time  # type: str
        self.interval = interval  # type: int
        self.operation_type = operation_type  # type: str
        self.reset_type = reset_type  # type: str
        self.timer_type = timer_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.enforce is not None:
            result['Enforce'] = self.enforce
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(self, disk_id=None, disk_size=None, disk_type=None):
        self.disk_id = disk_id  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktopsDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate(TeaModel):
    def __init__(self, channel=None, current_app_version=None, force=None, new_app_version=None, project=None,
                 release_note=None, release_note_en=None, release_note_jp=None, size=None):
        self.channel = channel  # type: str
        self.current_app_version = current_app_version  # type: str
        self.force = force  # type: bool
        self.new_app_version = new_app_version  # type: str
        self.project = project  # type: str
        self.release_note = release_note  # type: str
        self.release_note_en = release_note_en  # type: str
        self.release_note_jp = release_note_jp  # type: str
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version
        if self.force is not None:
            result['Force'] = self.force
        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version
        if self.project is not None:
            result['Project'] = self.project
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsSessions(TeaModel):
    def __init__(self, end_user_id=None, establishment_time=None):
        self.end_user_id = end_user_id  # type: str
        self.establishment_time = establishment_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktopsSessions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')
        return self


class DescribeGlobalDesktopsResponseBodyDesktops(TeaModel):
    def __init__(self, charge_type=None, clients=None, connection_status=None, cpu=None, creation_time=None,
                 desktop_group_id=None, desktop_id=None, desktop_name=None, desktop_status=None, desktop_timers=None,
                 desktop_type=None, directory_id=None, disks=None, end_user_id=None, end_user_ids=None, expired_time=None,
                 fota_update=None, gpu_memory=None, hibernation_beta=None, host_name=None, image_id=None, last_start_time=None,
                 local_name=None, management_flags=None, memory=None, network_interface_ip=None, office_site_id=None, os=None,
                 os_type=None, platform=None, policy_group_id=None, protocol_type=None, real_desktop_id=None,
                 region_id=None, session_type=None, sessions=None, support_hibernation=None, user_custom_name=None):
        self.charge_type = charge_type  # type: str
        # 支持的客户端信息
        self.clients = clients  # type: list[DescribeGlobalDesktopsResponseBodyDesktopsClients]
        self.connection_status = connection_status  # type: str
        self.cpu = cpu  # type: int
        self.creation_time = creation_time  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.desktop_name = desktop_name  # type: str
        self.desktop_status = desktop_status  # type: str
        self.desktop_timers = desktop_timers  # type: list[DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers]
        self.desktop_type = desktop_type  # type: str
        self.directory_id = directory_id  # type: str
        self.disks = disks  # type: list[DescribeGlobalDesktopsResponseBodyDesktopsDisks]
        self.end_user_id = end_user_id  # type: str
        self.end_user_ids = end_user_ids  # type: list[str]
        self.expired_time = expired_time  # type: str
        self.fota_update = fota_update  # type: DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate
        self.gpu_memory = gpu_memory  # type: int
        self.hibernation_beta = hibernation_beta  # type: bool
        self.host_name = host_name  # type: str
        self.image_id = image_id  # type: str
        self.last_start_time = last_start_time  # type: str
        self.local_name = local_name  # type: str
        self.management_flags = management_flags  # type: list[str]
        self.memory = memory  # type: long
        self.network_interface_ip = network_interface_ip  # type: str
        self.office_site_id = office_site_id  # type: str
        self.os = os  # type: str
        self.os_type = os_type  # type: str
        self.platform = platform  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.protocol_type = protocol_type  # type: str
        self.real_desktop_id = real_desktop_id  # type: str
        self.region_id = region_id  # type: str
        self.session_type = session_type  # type: str
        self.sessions = sessions  # type: list[DescribeGlobalDesktopsResponseBodyDesktopsSessions]
        self.support_hibernation = support_hibernation  # type: bool
        self.user_custom_name = user_custom_name  # type: str

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.desktop_timers:
            for k in self.desktop_timers:
                if k:
                    k.validate()
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBodyDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k in self.desktop_timers:
                result['DesktopTimers'].append(k.to_map() if k else None)
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.os is not None:
            result['Os'] = self.os
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.real_desktop_id is not None:
            result['RealDesktopId'] = self.real_desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation
        if self.user_custom_name is not None:
            result['UserCustomName'] = self.user_custom_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k in m.get('DesktopTimers'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k))
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FotaUpdate') is not None:
            temp_model = DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate()
            self.fota_update = temp_model.from_map(m['FotaUpdate'])
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RealDesktopId') is not None:
            self.real_desktop_id = m.get('RealDesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')
        if m.get('UserCustomName') is not None:
            self.user_custom_name = m.get('UserCustomName')
        return self


class DescribeGlobalDesktopsResponseBody(TeaModel):
    def __init__(self, desktops=None, next_token=None, request_id=None):
        self.desktops = desktops  # type: list[DescribeGlobalDesktopsResponseBodyDesktops]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGlobalDesktopsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGlobalDesktopsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalDesktopsResponse, self).to_map()
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
            temp_model = DescribeGlobalDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfficeSitesRequest(TeaModel):
    def __init__(self, client_id=None, office_site_id=None, region_id=None):
        self.client_id = client_id  # type: str
        self.office_site_id = office_site_id  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOfficeSitesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSites(TeaModel):
    def __init__(self, desktop_access_type=None, desktop_vpc_endpoint=None, office_site_id=None,
                 office_site_type=None, provider_id=None, sso_service_url=None):
        self.desktop_access_type = desktop_access_type  # type: str
        self.desktop_vpc_endpoint = desktop_vpc_endpoint  # type: str
        self.office_site_id = office_site_id  # type: str
        self.office_site_type = office_site_type  # type: str
        self.provider_id = provider_id  # type: str
        self.sso_service_url = sso_service_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBodyOfficeSites, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class DescribeOfficeSitesResponseBody(TeaModel):
    def __init__(self, office_sites=None, request_id=None):
        self.office_sites = office_sites  # type: list[DescribeOfficeSitesResponseBodyOfficeSites]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.office_sites:
            for k in self.office_sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k in self.office_sites:
                result['OfficeSites'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k in m.get('OfficeSites'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOfficeSitesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOfficeSitesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOfficeSitesResponse, self).to_map()
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
            temp_model = DescribeOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, client_id=None, region_id=None):
        self.client_id = client_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_endpoint=None, region_id=None):
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(self, client_id=None, desktop_id=None, login_token=None, max_results=None, next_token=None,
                 region_id=None, session_id=None, snapshot_id=None):
        self.client_id = client_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.login_token = login_token  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, creation_time=None, description=None, desktop_id=None, progress=None, remain_time=None,
                 snapshot_id=None, snapshot_name=None, snapshot_type=None, source_disk_size=None, source_disk_type=None,
                 status=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.desktop_id = desktop_id  # type: str
        self.progress = progress  # type: str
        self.remain_time = remain_time  # type: int
        self.snapshot_id = snapshot_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.source_disk_size = source_disk_size  # type: str
        self.source_disk_type = source_disk_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, snapshots=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.snapshots = snapshots  # type: list[DescribeSnapshotsResponseBodySnapshots]

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSnapshotsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponse, self).to_map()
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
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptPasswordRequest(TeaModel):
    def __init__(self, client_id=None, directory_id=None, login_token=None, office_site_id=None, password=None,
                 region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.directory_id = directory_id  # type: str
        self.login_token = login_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.password = password  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class EncryptPasswordResponseBody(TeaModel):
    def __init__(self, encrypted_password=None, request_id=None):
        self.encrypted_password = encrypted_password  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EncryptPasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EncryptPasswordResponse, self).to_map()
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
            temp_model = EncryptPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudDriveServiceMountTokenRequest(TeaModel):
    def __init__(self, client_id=None, login_token=None, office_site_id=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.login_token = login_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudDriveServiceMountTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetCloudDriveServiceMountTokenResponseBodyToken(TeaModel):
    def __init__(self, domain_id=None, expired_after=None, status=None, token=None, total_size=None, used_size=None):
        self.domain_id = domain_id  # type: str
        self.expired_after = expired_after  # type: str
        self.status = status  # type: str
        self.token = token  # type: str
        self.total_size = total_size  # type: long
        self.used_size = used_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudDriveServiceMountTokenResponseBodyToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.expired_after is not None:
            result['ExpiredAfter'] = self.expired_after
        if self.status is not None:
            result['Status'] = self.status
        if self.token is not None:
            result['Token'] = self.token
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.used_size is not None:
            result['UsedSize'] = self.used_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('ExpiredAfter') is not None:
            self.expired_after = m.get('ExpiredAfter')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')
        return self


class GetCloudDriveServiceMountTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: GetCloudDriveServiceMountTokenResponseBodyToken

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(GetCloudDriveServiceMountTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            temp_model = GetCloudDriveServiceMountTokenResponseBodyToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class GetCloudDriveServiceMountTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCloudDriveServiceMountTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCloudDriveServiceMountTokenResponse, self).to_map()
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
            temp_model = GetCloudDriveServiceMountTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_type=None, client_version=None, command_content=None,
                 desktop_id=None, login_token=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, session_id=None, task_id=None, uuid=None):
        self.client_id = client_id  # type: str
        self.client_os = client_os  # type: str
        self.client_type = client_type  # type: str
        self.client_version = client_version  # type: str
        self.command_content = command_content  # type: str
        self.desktop_id = desktop_id  # type: str
        self.login_token = login_token  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.session_id = session_id  # type: str
        self.task_id = task_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(self, request_id=None, task_code=None, task_id=None, task_message=None, task_status=None,
                 ticket=None):
        self.request_id = request_id  # type: str
        self.task_code = task_code  # type: str
        self.task_id = task_id  # type: str
        self.task_message = task_message  # type: str
        self.task_status = task_status  # type: str
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_message is not None:
            result['TaskMessage'] = self.task_message
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConnectionTicketResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnectionTicketResponse, self).to_map()
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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(self, authentication_code=None, client_id=None, client_os=None, client_type=None,
                 client_version=None, current_stage=None, directory_id=None, end_user_id=None, keep_alive=None,
                 keep_alive_token=None, new_password=None, office_site_id=None, old_password=None, password=None, region_id=None,
                 session_id=None, token_code=None, uuid=None):
        # The verification code that is generated by the virtual MFA device. This parameter is required if you set `CurrentStage` to `MFAVerify`.
        self.authentication_code = authentication_code  # type: str
        # The ID of the Alibaba Cloud Workspace client. The system generates a unique ID for each client.
        self.client_id = client_id  # type: str
        # The OS that the client runs.
        self.client_os = client_os  # type: str
        # The type of the software client.
        self.client_type = client_type  # type: str
        # The version of the client. When you use an Alibaba Cloud Workspace client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version  # type: str
        # The logon authentication stage. Valid values:
        # 
        # *   `ADPassword`: the stage to verify the identity of the Active Directory (AD) user. You must specify the value when the system verifies the identity of a convenience account or an AD account.
        # *   `MFABind`: the stage to bind a virtual multi-factor authentication (MFA) device.
        # *   `MFAVerify`: the stage to obtain the verification code that is generated by the virtual MFA device.
        # *   `TokenVerify`: the stage to perform two-factor authentication for the client.
        # *   `ChangePassword`: the stage to change the password of the user.
        # *   `VerifyKeepAlive`: the stage to exchange the logon credential. This parameter is valid if KeepAliveToken is valid.
        self.current_stage = current_stage  # type: str
        # The ID of the workspace. The parameter is the same as the `OfficeSiteId` parameter. We recommend that you use `OfficeSiteId` instead of `DirectoryId`. You can specify a value for either the `DirectoryId` parameter or the `OfficeSiteId` parameter, but not both.
        self.directory_id = directory_id  # type: str
        # The name of the convenience user or the AD user. This parameter is required if you set `CurrentStage` to `ADPassword`.
        self.end_user_id = end_user_id  # type: str
        # Specifies whether to keep the user logged on to the client. 
        # Valid values:
        # * null: Default value. Do not keep the user logged on to the client.
        # * true: Keep the user logged on to the client.
        # * false:  Do not keep the user logged on to the client.
        self.keep_alive = keep_alive  # type: bool
        # The token that is used to keep the user logged on to the client. After the user logs on to the client and KeepAlive is set to true, the `KeepAliveToken` is returned. You can call the `GetLoginToken` operation within the valid duration``, and set `CurrentStage` to `VerifyKeepAlive` to obtain the logon token (LoginToken). This parameter is required if you set `CurrentStage` to `VerifyKeepAlive```.
        self.keep_alive_token = keep_alive_token  # type: str
        # The new password. This parameter is required if you set `CurrentStage` to `ChangePassword`.
        self.new_password = new_password  # type: str
        # The ID of the workspace.
        self.office_site_id = office_site_id  # type: str
        # The current password. This parameter is required if you set `CurrentStage` to `ChangePassword`.
        self.old_password = old_password  # type: str
        # The password of the convenience user or the AD user. This parameter is required if you set `CurrentStage` to `ADPassword`.
        self.password = password  # type: str
        # The ID of the region. You can call the [DescribeRegions](~~436773~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the session.
        # 
        # *   If the virtual multi-factor authentication (MFA) device is not bound or two-factor authentication is not enabled for the client, you do not need to specify a value for `SessionId`.
        # *   If the virtual MFA device is not bound or two-factor authentication is enabled for the client, you must specify a value for `SessionId` to verify the user identity after you specify a value for `ADPassword`. The value of the `SessionId` parameter is returned only if the CurrentStage parameter is set to `ADPassword` when you call the `GetLoginToken` operation.
        self.session_id = session_id  # type: str
        # If two-factor authentication is enabled in the Elastic Desktop Service (EDS) console and the system detects that the identity of the logon user may have security risks, the system sends a verification code for two-factor authentication to the email address of the user. This parameter is required if you set `CurrentStage` to `TokenVerify`.
        self.token_code = token_code  # type: str
        # The unique identifier of the client. When you use an Alibaba Cloud Workspace client, you can view the client version in the **About** dialog box on the client logon page.
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetLoginTokenResponseBodyRiskVerifyInfo(TeaModel):
    def __init__(self, email=None, last_lock_duration=None, locked=None, phone=None):
        self.email = email  # type: str
        self.last_lock_duration = last_lock_duration  # type: long
        self.locked = locked  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenResponseBodyRiskVerifyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.last_lock_duration is not None:
            result['LastLockDuration'] = self.last_lock_duration
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLockDuration') is not None:
            self.last_lock_duration = m.get('LastLockDuration')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(self, email=None, end_user_id=None, industry=None, keep_alive_token=None, label=None,
                 login_token=None, next_stage=None, phone=None, props=None, qr_code_png=None, request_id=None,
                 risk_verify_info=None, secret=None, session_id=None, tenant_id=None, window_display_mode=None):
        # The email address of the user. The system returns the email address in the return value of the LoginToken parameter after the user logs on to the client.
        # 
        # *   For a convenience user, the return value is the email address specified when the administrator creates the convenience user.
        # *   For an AD user, the return value is in the following format: `Username@Name of the AD domain`.
        self.email = email  # type: str
        # The account of the convenience user or the AD user.
        self.end_user_id = end_user_id  # type: str
        # > This is a parameter only for internal use.
        self.industry = industry  # type: str
        # The token used to keep the user logged on. After the user logs on to the client and select the Keep Logon option, `KeepAliveToken` is returned when you call the operation. If the user does not select the Keep Logon option, null is returned.
        self.keep_alive_token = keep_alive_token  # type: str
        # The attribute of the convenience user. For an AD user, null is returned.
        self.label = label  # type: str
        # The logon token.
        self.login_token = login_token  # type: str
        # The next stage that is expected to enter. For example, if the administrator enables MFA authentication in the EDS console, `MFAVerify` is returned after the username and password pass the authentication (after you set CurrentStage to `ADPassword` stage). This indicates that the MFA authentication is required.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.next_stage = next_stage  # type: str
        # Enter the mobile number of the convenience user. For an AD user, null is returned.
        self.phone = phone  # type: str
        # > This is a parameter only for internal use.
        self.props = props  # type: dict[str, str]
        # The QR code that is generated when the virtual MFA device is bound. The value is encoded in Base64. This parameter can be empty. This parameter is required only when the CurrentStage parameter is set to `MFABind`.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.qr_code_png = qr_code_png  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.risk_verify_info = risk_verify_info  # type: GetLoginTokenResponseBodyRiskVerifyInfo
        # The key that is generated when you bind the virtual MFA device. This parameter is required when the CurrentStage parameter is set to `MFABind`.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.secret = secret  # type: str
        # The ID of the session. The ID is returned the first time you call the `GetLoginToken` operation in the session. If MFA is required, you must specify this parameter in subsequent stages.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.session_id = session_id  # type: str
        # The ID of the Alibaba Cloud account. The ID is used for hardware client authentication.
        self.tenant_id = tenant_id  # type: long
        # > This is a parameter only for internal use.
        self.window_display_mode = window_display_mode  # type: str

    def validate(self):
        if self.risk_verify_info:
            self.risk_verify_info.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.label is not None:
            result['Label'] = self.label
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.next_stage is not None:
            result['NextStage'] = self.next_stage
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.props is not None:
            result['Props'] = self.props
        if self.qr_code_png is not None:
            result['QrCodePng'] = self.qr_code_png
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_verify_info is not None:
            result['RiskVerifyInfo'] = self.risk_verify_info.to_map()
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.window_display_mode is not None:
            result['WindowDisplayMode'] = self.window_display_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('NextStage') is not None:
            self.next_stage = m.get('NextStage')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('QrCodePng') is not None:
            self.qr_code_png = m.get('QrCodePng')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskVerifyInfo') is not None:
            temp_model = GetLoginTokenResponseBodyRiskVerifyInfo()
            self.risk_verify_info = temp_model.from_map(m['RiskVerifyInfo'])
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WindowDisplayMode') is not None:
            self.window_display_mode = m.get('WindowDisplayMode')
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLoginTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponse, self).to_map()
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsKeepAliveRequest(TeaModel):
    def __init__(self, client_id=None, office_site_id=None, region_id=None):
        self.client_id = client_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsKeepAliveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class IsKeepAliveResponseBody(TeaModel):
    def __init__(self, is_keep_alive=None, office_site_id=None, request_id=None, tenant_id=None):
        self.is_keep_alive = is_keep_alive  # type: bool
        self.office_site_id = office_site_id  # type: str
        self.request_id = request_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsKeepAliveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_keep_alive is not None:
            result['IsKeepAlive'] = self.is_keep_alive
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsKeepAlive') is not None:
            self.is_keep_alive = m.get('IsKeepAlive')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class IsKeepAliveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IsKeepAliveResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IsKeepAliveResponse, self).to_map()
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
            temp_model = IsKeepAliveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEdsAgentReportConfigRequest(TeaModel):
    def __init__(self, ali_uid=None, desktop_id=None, ecs_instance_id=None):
        self.ali_uid = ali_uid  # type: long
        self.desktop_id = desktop_id  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEdsAgentReportConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        return self


class QueryEdsAgentReportConfigResponseBodyData(TeaModel):
    def __init__(self, config=None):
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEdsAgentReportConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class QueryEdsAgentReportConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryEdsAgentReportConfigResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEdsAgentReportConfigResponseBody, self).to_map()
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
            temp_model = QueryEdsAgentReportConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryEdsAgentReportConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEdsAgentReportConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEdsAgentReportConfigResponse, self).to_map()
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
            temp_model = QueryEdsAgentReportConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_token=None, client_version=None, desktop_id=None,
                 login_token=None, region_id=None, session_id=None, session_token=None, uuid=None):
        # The client ID. The system generates a unique ID for each client.
        self.client_id = client_id  # type: str
        # The operating system (OS) of the device that runs the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client).
        self.client_os = client_os  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence of a request?](~~25693~~)
        self.client_token = client_token  # type: str
        # The client version. If you use a WUYING client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version  # type: str
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        self.desktop_id = desktop_id  # type: list[str]
        # The logon token.
        self.login_token = login_token  # type: str
        # The region ID. You can call the [DescribeRegions](~~196646~~) operation to query the regions supported by WUYING Workspace.
        self.region_id = region_id  # type: str
        # The session ID.
        self.session_id = session_id  # type: str
        # The logon token.
        self.session_token = session_token  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RebootDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootDesktopsResponseBody, self).to_map()
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


class RebootDesktopsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebootDesktopsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebootDesktopsResponse, self).to_map()
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
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshLoginTokenRequest(TeaModel):
    def __init__(self, client_id=None, directory_id=None, end_user_id=None, login_token=None, office_site_id=None,
                 region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.directory_id = directory_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.login_token = login_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshLoginTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RefreshLoginTokenResponseBody(TeaModel):
    def __init__(self, login_token=None, request_id=None):
        self.login_token = login_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshLoginTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshLoginTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshLoginTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshLoginTokenResponse, self).to_map()
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
            temp_model = RefreshLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportEdsAgentInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, desktop_id=None, ecs_instance_id=None, eds_agent_info=None):
        self.ali_uid = ali_uid  # type: long
        self.desktop_id = desktop_id  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.eds_agent_info = eds_agent_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportEdsAgentInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.eds_agent_info is not None:
            result['EdsAgentInfo'] = self.eds_agent_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EdsAgentInfo') is not None:
            self.eds_agent_info = m.get('EdsAgentInfo')
        return self


class ReportEdsAgentInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportEdsAgentInfoResponseBody, self).to_map()
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


class ReportEdsAgentInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportEdsAgentInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportEdsAgentInfoResponse, self).to_map()
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
            temp_model = ReportEdsAgentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportSessionStatusRequest(TeaModel):
    def __init__(self, end_user_id=None, instance_id=None, region_id=None, session_change_time=None,
                 session_id=None, session_status=None):
        self.end_user_id = end_user_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.session_change_time = session_change_time  # type: long
        self.session_id = session_id  # type: str
        self.session_status = session_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportSessionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_change_time is not None:
            result['SessionChangeTime'] = self.session_change_time
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionChangeTime') is not None:
            self.session_change_time = m.get('SessionChangeTime')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        return self


class ReportSessionStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportSessionStatusResponseBody, self).to_map()
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


class ReportSessionStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportSessionStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportSessionStatusResponse, self).to_map()
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
            temp_model = ReportSessionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetPasswordRequest(TeaModel):
    def __init__(self, client_id=None, client_token=None, email=None, end_user_id=None, office_site_id=None,
                 region_id=None, phone=None):
        self.client_id = client_id  # type: str
        self.client_token = client_token  # type: str
        self.email = email  # type: str
        self.end_user_id = end_user_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.region_id = region_id  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.phone is not None:
            result['phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        return self


class ResetPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetPasswordResponseBody, self).to_map()
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


class ResetPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetPasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetPasswordResponse, self).to_map()
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
            temp_model = ResetPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(self, client_id=None, login_token=None, region_id=None, session_id=None, snapshot_id=None):
        self.client_id = client_id  # type: str
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSnapshotResponseBody, self).to_map()
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


class ResetSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetSnapshotResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetSnapshotResponse, self).to_map()
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
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTokenCodeRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_version=None, end_user_id=None, login_token=None,
                 office_site_id=None, session_id=None, token_code=None):
        self.client_id = client_id  # type: str
        self.client_os = client_os  # type: str
        self.client_version = client_version  # type: str
        self.end_user_id = end_user_id  # type: str
        self.login_token = login_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.session_id = session_id  # type: str
        self.token_code = token_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTokenCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        return self


class SendTokenCodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTokenCodeResponseBody, self).to_map()
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


class SendTokenCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendTokenCodeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendTokenCodeResponse, self).to_map()
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
            temp_model = SendTokenCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFingerPrintTemplateRequest(TeaModel):
    def __init__(self, client_id=None, client_token=None, description=None, encrypted_finger_print_template=None,
                 encrypted_key=None, finger_print_template=None, login_token=None, password=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.encrypted_finger_print_template = encrypted_finger_print_template  # type: str
        self.encrypted_key = encrypted_key  # type: str
        self.finger_print_template = finger_print_template  # type: str
        self.login_token = login_token  # type: str
        self.password = password  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFingerPrintTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypted_finger_print_template is not None:
            result['EncryptedFingerPrintTemplate'] = self.encrypted_finger_print_template
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.finger_print_template is not None:
            result['FingerPrintTemplate'] = self.finger_print_template
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptedFingerPrintTemplate') is not None:
            self.encrypted_finger_print_template = m.get('EncryptedFingerPrintTemplate')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('FingerPrintTemplate') is not None:
            self.finger_print_template = m.get('FingerPrintTemplate')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SetFingerPrintTemplateResponseBody(TeaModel):
    def __init__(self, encrypted_password=None, index=None, request_id=None):
        self.encrypted_password = encrypted_password  # type: str
        self.index = index  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFingerPrintTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.index is not None:
            result['Index'] = self.index
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFingerPrintTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetFingerPrintTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetFingerPrintTemplateResponse, self).to_map()
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
            temp_model = SetFingerPrintTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFingerPrintTemplateDescriptionRequest(TeaModel):
    def __init__(self, client_id=None, client_token=None, description=None, index=None, login_token=None,
                 region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.index = index  # type: int
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFingerPrintTemplateDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.index is not None:
            result['Index'] = self.index
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SetFingerPrintTemplateDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFingerPrintTemplateDescriptionResponseBody, self).to_map()
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


class SetFingerPrintTemplateDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetFingerPrintTemplateDescriptionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetFingerPrintTemplateDescriptionResponse, self).to_map()
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
            temp_model = SetFingerPrintTemplateDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_token=None, client_version=None, desktop_id=None,
                 login_token=None, region_id=None, session_id=None, uuid=None):
        # The ID of the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client). The system generates a unique ID for each client.
        self.client_id = client_id  # type: str
        # The operating system (OS) of the device that run the client.
        self.client_os = client_os  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The client version. If you use a WUYING client, you can click **About** on the client logon page to view the version of the client.
        self.client_version = client_version  # type: str
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        self.desktop_id = desktop_id  # type: list[str]
        # The logon token.
        self.login_token = login_token  # type: str
        # The region ID. You can call the [DescribeRegions](~~196646~~) operation to query the regions supported by WUYING Workspace.
        self.region_id = region_id  # type: str
        # The session ID.
        self.session_id = session_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class StartDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDesktopsResponseBody, self).to_map()
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


class StartDesktopsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartDesktopsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDesktopsResponse, self).to_map()
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
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordContentRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_version=None, desktop_id=None, file_path=None,
                 login_token=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.client_os = client_os  # type: str
        self.client_version = client_version  # type: str
        self.desktop_id = desktop_id  # type: str
        self.file_path = file_path  # type: str
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StartRecordContentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordContentResponseBody, self).to_map()
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


class StartRecordContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartRecordContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartRecordContentResponse, self).to_map()
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
            temp_model = StartRecordContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_token=None, client_version=None, desktop_id=None,
                 login_token=None, region_id=None, session_id=None, session_token=None):
        # The client ID. The system generates a unique ID for each client.
        self.client_id = client_id  # type: str
        # The operating system (OS) of the device that runs the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client).
        self.client_os = client_os  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence of a request?](~~25693~~)
        self.client_token = client_token  # type: str
        # The client version. If you use a WUYING client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version  # type: str
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        self.desktop_id = desktop_id  # type: list[str]
        # The logon token.
        self.login_token = login_token  # type: str
        # The region ID. You can call the [DescribeRegions](~~196646~~) operation to query the regions supported by WUYING Workspace.
        self.region_id = region_id  # type: str
        # The session ID.
        self.session_id = session_id  # type: str
        # The logon token.
        self.session_token = session_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        return self


class StopDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDesktopsResponseBody, self).to_map()
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


class StopDesktopsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDesktopsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDesktopsResponse, self).to_map()
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
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordContentRequest(TeaModel):
    def __init__(self, client_id=None, client_os=None, client_version=None, desktop_id=None, login_token=None,
                 region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.client_os = client_os  # type: str
        self.client_version = client_version  # type: str
        self.desktop_id = desktop_id  # type: str
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopRecordContentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordContentResponseBody, self).to_map()
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


class StopRecordContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopRecordContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopRecordContentResponse, self).to_map()
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
            temp_model = StopRecordContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindUserDesktopRequest(TeaModel):
    def __init__(self, client_id=None, client_type=None, force=None, login_token=None, region_id=None,
                 session_id=None, user_desktop_id=None):
        self.client_id = client_id  # type: str
        self.client_type = client_type  # type: str
        self.force = force  # type: bool
        self.login_token = login_token  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str
        self.user_desktop_id = user_desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindUserDesktopRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.force is not None:
            result['Force'] = self.force
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')
        return self


class UnbindUserDesktopResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindUserDesktopResponseBody, self).to_map()
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


class UnbindUserDesktopResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindUserDesktopResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindUserDesktopResponse, self).to_map()
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
            temp_model = UnbindUserDesktopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCredentialRequest(TeaModel):
    def __init__(self, client_id=None, credential=None, credential_type=None, encrypted_key=None, login_token=None,
                 office_site_id=None, region_id=None, session_id=None):
        self.client_id = client_id  # type: str
        self.credential = credential  # type: str
        self.credential_type = credential_type  # type: str
        self.encrypted_key = encrypted_key  # type: str
        self.login_token = login_token  # type: str
        self.office_site_id = office_site_id  # type: str
        self.region_id = region_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.credential is not None:
            result['Credential'] = self.credential
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Credential') is not None:
            self.credential = m.get('Credential')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class VerifyCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCredentialResponseBody, self).to_map()
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


class VerifyCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyCredentialResponse, self).to_map()
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
            temp_model = VerifyCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


