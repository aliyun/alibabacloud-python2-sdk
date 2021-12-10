# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelRepoBuildResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CancelRepoBuildResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateRepoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateRepoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateRepoBuildRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateRepoWebhookResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateRepoWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateUserInfoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateUserInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteRepoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteRepoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteRepoBuildRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteRepoWebhookResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteRepoWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetAuthorizationTokenResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetAuthorizationTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetImageLayerResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetImageLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetImageManifestRequest(TeaModel):
    def __init__(self, schema_version=None):
        self.schema_version = schema_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageManifestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetImageManifestResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetImageManifestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetNamespaceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetNamespaceListRequest(TeaModel):
    def __init__(self, authorize=None, status=None):
        self.authorize = authorize  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNamespaceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetNamespaceListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetNamespaceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRegionRequest(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetRegionResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRegionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRegionListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRegionListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoBuildListRequest(TeaModel):
    def __init__(self, page=None, page_size=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoBuildListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRepoBuildListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoBuildListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoBuildRuleListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoBuildRuleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoBuildStatusResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoBuildStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoListRequest(TeaModel):
    def __init__(self, page=None, page_size=None, status=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoListByNamespaceRequest(TeaModel):
    def __init__(self, page=None, page_size=None, status=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoListByNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoListByNamespaceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoListByNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoTagResponseBody(TeaModel):
    def __init__(self, digest=None, image_create=None, image_id=None, image_size=None, image_update=None,
                 request_id=None, status=None, tag=None):
        self.digest = digest  # type: str
        self.image_create = image_create  # type: long
        self.image_id = image_id  # type: str
        self.image_size = image_size  # type: long
        self.image_update = image_update  # type: long
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['digest'] = self.digest
        if self.image_create is not None:
            result['imageCreate'] = self.image_create
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.image_size is not None:
            result['imageSize'] = self.image_size
        if self.image_update is not None:
            result['imageUpdate'] = self.image_update
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('digest') is not None:
            self.digest = m.get('digest')
        if m.get('imageCreate') is not None:
            self.image_create = m.get('imageCreate')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('imageSize') is not None:
            self.image_size = m.get('imageSize')
        if m.get('imageUpdate') is not None:
            self.image_update = m.get('imageUpdate')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class GetRepoTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRepoTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagResponse, self).to_map()
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
            temp_model = GetRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanListRequest(TeaModel):
    def __init__(self, page=None, page_size=None, severity=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.severity = severity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagScanListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class GetRepoTagScanListResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoTagScanListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoTagScanStatusResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoTagScanStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoTagScanSummaryResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoTagScanSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoTagsRequest(TeaModel):
    def __init__(self, page=None, page_size=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRepoTagsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRepoWebhookResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetRepoWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetResourceQuotaResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GetResourceQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class StartImageScanResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(StartImageScanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class StartRepoBuildByRuleResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(StartRepoBuildByRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateRepoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateRepoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateRepoBuildRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateRepoWebhookResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateRepoWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateUserInfoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateUserInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


