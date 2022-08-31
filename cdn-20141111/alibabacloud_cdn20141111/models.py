# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCdnDomainRequest(TeaModel):
    def __init__(self, cdn_type=None, check_url=None, domain_name=None, owner_account=None, owner_id=None,
                 priorities=None, region=None, resource_group_id=None, scope=None, security_token=None, source_port=None,
                 source_type=None, sources=None, top_level_domain=None):
        self.cdn_type = cdn_type  # type: str
        self.check_url = check_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.priorities = priorities  # type: str
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.security_token = security_token  # type: str
        self.source_port = source_port  # type: int
        self.source_type = source_type  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.priorities is not None:
            result['Priorities'] = self.priorities
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Priorities') is not None:
            self.priorities = m.get('Priorities')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCdnDomainResponseBody, self).to_map()
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


class AddCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCdnDomainResponse, self).to_map()
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
            temp_model = AddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainDetailRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel(TeaModel):
    def __init__(self, content=None, enabled=None, port=None, priority=None, type=None):
        self.content = content  # type: str
        self.enabled = enabled  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels(TeaModel):
    def __init__(self, source_model=None):
        self.source_model = source_model  # type: list[DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel]

    def validate(self):
        if self.source_model:
            for k in self.source_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceModel'] = []
        if self.source_model is not None:
            for k in self.source_model:
                result['SourceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source_model = []
        if m.get('SourceModel') is not None:
            for k in m.get('SourceModel'):
                temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel()
                self.source_model.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModel(TeaModel):
    def __init__(self, cdn_type=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, https_cname=None, region=None, resource_group_id=None, scope=None,
                 server_certificate_status=None, source_models=None, source_port=None, source_type=None, sources=None):
        self.cdn_type = cdn_type  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.https_cname = https_cname  # type: str
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.source_models = source_models  # type: DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels
        self.source_port = source_port  # type: int
        self.source_type = source_type  # type: str
        self.sources = sources  # type: DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSources

    def validate(self):
        if self.source_models:
            self.source_models.validate()
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponseBodyGetDomainDetailModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.https_cname is not None:
            result['HttpsCname'] = self.https_cname
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.source_models is not None:
            result['SourceModels'] = self.source_models.to_map()
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpsCname') is not None:
            self.https_cname = m.get('HttpsCname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('SourceModels') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels()
            self.source_models = temp_model.from_map(m['SourceModels'])
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Sources') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeCdnDomainDetailResponseBody(TeaModel):
    def __init__(self, get_domain_detail_model=None, request_id=None):
        self.get_domain_detail_model = get_domain_detail_model  # type: DescribeCdnDomainDetailResponseBodyGetDomainDetailModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.get_domain_detail_model:
            self.get_domain_detail_model.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_domain_detail_model is not None:
            result['GetDomainDetailModel'] = self.get_domain_detail_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GetDomainDetailModel') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModel()
            self.get_domain_detail_model = temp_model.from_map(m['GetDomainDetailModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCdnDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainDetailResponse, self).to_map()
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
            temp_model = DescribeCdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainLogsRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, log_day=None, owner_id=None, page_number=None,
                 page_size=None, security_token=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.log_day = log_day  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_day is not None:
            result['LogDay'] = self.log_day
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogDay') is not None:
            self.log_day = m.get('LogDay')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(self, end_time=None, log_name=None, log_path=None, log_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.log_name = log_name  # type: str
        self.log_path = log_path  # type: str
        self.log_size = log_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetailsDomainLogDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetails(TeaModel):
    def __init__(self, domain_log_detail=None):
        self.domain_log_detail = domain_log_detail  # type: list[DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetailsDomainLogDetail]

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainLogDetail'] = []
        if self.domain_log_detail is not None:
            for k in self.domain_log_detail:
                result['DomainLogDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_log_detail = []
        if m.get('DomainLogDetail') is not None:
            for k in m.get('DomainLogDetail'):
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogModel(TeaModel):
    def __init__(self, domain_log_details=None, domain_name=None):
        self.domain_log_details = domain_log_details  # type: DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetails
        self.domain_name = domain_name  # type: str

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogModelDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeCdnDomainLogsResponseBody(TeaModel):
    def __init__(self, domain_log_model=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domain_log_model = domain_log_model  # type: DescribeCdnDomainLogsResponseBodyDomainLogModel
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domain_log_model:
            self.domain_log_model.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_model is not None:
            result['DomainLogModel'] = self.domain_log_model.to_map()
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
        if m.get('DomainLogModel') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogModel()
            self.domain_log_model = temp_model.from_map(m['DomainLogModel'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnDomainLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCdnDomainLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponse, self).to_map()
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
            temp_model = DescribeCdnDomainLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnServiceRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnServiceResponseBodyOperationLocksLockReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        return self


class DescribeCdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: list[DescribeCdnServiceResponseBodyOperationLocksLockReason]

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnServiceResponseBodyOperationLocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k in self.lock_reason:
                result['LockReason'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k in m.get('LockReason'):
                temp_model = DescribeCdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeCdnServiceResponseBody(TeaModel):
    def __init__(self, changing_affect_time=None, changing_charge_type=None, instance_id=None,
                 internet_charge_type=None, opening_time=None, operation_locks=None, request_id=None):
        self.changing_affect_time = changing_affect_time  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.opening_time = opening_time  # type: str
        self.operation_locks = operation_locks  # type: DescribeCdnServiceResponseBodyOperationLocks
        self.request_id = request_id  # type: str

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super(DescribeCdnServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeCdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnServiceResponse, self).to_map()
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
            temp_model = DescribeCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, domain_type=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None, owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_l2value=None, domestic_value=None, dynamic_domestic_value=None,
                 dynamic_overseas_value=None, dynamic_value=None, l_2value=None, overseas_l2value=None, overseas_value=None,
                 static_domestic_value=None, static_overseas_value=None, static_value=None, time_stamp=None, value=None):
        self.domestic_l2value = domestic_l2value  # type: str
        self.domestic_value = domestic_value  # type: str
        self.dynamic_domestic_value = dynamic_domestic_value  # type: str
        self.dynamic_overseas_value = dynamic_overseas_value  # type: str
        self.dynamic_value = dynamic_value  # type: str
        self.l_2value = l_2value  # type: str
        self.overseas_l2value = overseas_l2value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.static_domestic_value = static_domestic_value  # type: str
        self.static_overseas_value = static_overseas_value  # type: str
        self.static_value = static_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_l2value is not None:
            result['DomesticL2Value'] = self.domestic_l2value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.dynamic_domestic_value is not None:
            result['DynamicDomesticValue'] = self.dynamic_domestic_value
        if self.dynamic_overseas_value is not None:
            result['DynamicOverseasValue'] = self.dynamic_overseas_value
        if self.dynamic_value is not None:
            result['DynamicValue'] = self.dynamic_value
        if self.l_2value is not None:
            result['L2Value'] = self.l_2value
        if self.overseas_l2value is not None:
            result['OverseasL2Value'] = self.overseas_l2value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.static_domestic_value is not None:
            result['StaticDomesticValue'] = self.static_domestic_value
        if self.static_overseas_value is not None:
            result['StaticOverseasValue'] = self.static_overseas_value
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticL2Value') is not None:
            self.domestic_l2value = m.get('DomesticL2Value')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('DynamicDomesticValue') is not None:
            self.dynamic_domestic_value = m.get('DynamicDomesticValue')
        if m.get('DynamicOverseasValue') is not None:
            self.dynamic_overseas_value = m.get('DynamicOverseasValue')
        if m.get('DynamicValue') is not None:
            self.dynamic_value = m.get('DynamicValue')
        if m.get('L2Value') is not None:
            self.l_2value = m.get('L2Value')
        if m.get('OverseasL2Value') is not None:
            self.overseas_l2value = m.get('OverseasL2Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('StaticDomesticValue') is not None:
            self.static_domestic_value = m.get('StaticDomesticValue')
        if m.get('StaticOverseasValue') is not None:
            self.static_overseas_value = m.get('StaticOverseasValue')
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataResponseBodyBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataResponseBody(TeaModel):
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 isp_name=None, isp_name_en=None, location_name=None, location_name_en=None, request_id=None,
                 start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name = isp_name  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name = location_name  # type: str
        self.location_name_en = location_name_en  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataResponse, self).to_map()
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
            temp_model = DescribeDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByTimeStampRequest(TeaModel):
    def __init__(self, domain_name=None, isp_names=None, location_names=None, owner_id=None, time_point=None):
        self.domain_name = domain_name  # type: str
        self.isp_names = isp_names  # type: str
        self.location_names = location_names  # type: str
        self.owner_id = owner_id  # type: long
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataByTimeStampRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel(TeaModel):
    def __init__(self, bps=None, isp_name=None, location_name=None, time_stamp=None):
        self.bps = bps  # type: long
        self.isp_name = isp_name  # type: str
        self.location_name = location_name  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList(TeaModel):
    def __init__(self, bps_data_model=None):
        self.bps_data_model = bps_data_model  # type: list[DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel]

    def validate(self):
        if self.bps_data_model:
            for k in self.bps_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BpsDataModel'] = []
        if self.bps_data_model is not None:
            for k in self.bps_data_model:
                result['BpsDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bps_data_model = []
        if m.get('BpsDataModel') is not None:
            for k in m.get('BpsDataModel'):
                temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel()
                self.bps_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByTimeStampResponseBody(TeaModel):
    def __init__(self, bps_data_list=None, domain_name=None, request_id=None, time_stamp=None):
        self.bps_data_list = bps_data_list  # type: DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        if self.bps_data_list:
            self.bps_data_list.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByTimeStampResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_list is not None:
            result['BpsDataList'] = self.bps_data_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataList') is not None:
            temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList()
            self.bps_data_list = temp_model.from_map(m['BpsDataList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByTimeStampResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainBpsDataByTimeStampResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByTimeStampResponse, self).to_map()
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
            temp_model = DescribeDomainBpsDataByTimeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainFileSizeProportionDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, security_token=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData(TeaModel):
    def __init__(self, file_size=None, proportion=None):
        self.file_size = file_size  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue(TeaModel):
    def __init__(self, file_size_proportion_data=None):
        self.file_size_proportion_data = file_size_proportion_data  # type: list[DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData]

    def validate(self):
        if self.file_size_proportion_data:
            for k in self.file_size_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSizeProportionData'] = []
        if self.file_size_proportion_data is not None:
            for k in self.file_size_proportion_data:
                result['FileSizeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_size_proportion_data = []
        if m.get('FileSizeProportionData') is not None:
            for k in m.get('FileSizeProportionData'):
                temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData()
                self.file_size_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainFileSizeProportionDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 file_size_proportion_data_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.file_size_proportion_data_interval = file_size_proportion_data_interval  # type: DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.file_size_proportion_data_interval:
            self.file_size_proportion_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_size_proportion_data_interval is not None:
            result['FileSizeProportionDataInterval'] = self.file_size_proportion_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileSizeProportionDataInterval') is not None:
            temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval()
            self.file_size_proportion_data_interval = temp_model.from_map(m['FileSizeProportionDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainFileSizeProportionDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainFileSizeProportionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainFileSizeProportionDataResponse, self).to_map()
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
            temp_model = DescribeDomainFileSizeProportionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainFlowDataRequest(TeaModel):
    def __init__(self, domain_name=None, domain_type=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None, owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainFlowDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainFlowDataResponseBodyFlowDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_value=None, dynamic_domestic_value=None, dynamic_overseas_value=None,
                 dynamic_value=None, overseas_value=None, static_domestic_value=None, static_overseas_value=None,
                 static_value=None, time_stamp=None, value=None):
        self.domestic_value = domestic_value  # type: str
        self.dynamic_domestic_value = dynamic_domestic_value  # type: str
        self.dynamic_overseas_value = dynamic_overseas_value  # type: str
        self.dynamic_value = dynamic_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.static_domestic_value = static_domestic_value  # type: str
        self.static_overseas_value = static_overseas_value  # type: str
        self.static_value = static_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainFlowDataResponseBodyFlowDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.dynamic_domestic_value is not None:
            result['DynamicDomesticValue'] = self.dynamic_domestic_value
        if self.dynamic_overseas_value is not None:
            result['DynamicOverseasValue'] = self.dynamic_overseas_value
        if self.dynamic_value is not None:
            result['DynamicValue'] = self.dynamic_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.static_domestic_value is not None:
            result['StaticDomesticValue'] = self.static_domestic_value
        if self.static_overseas_value is not None:
            result['StaticOverseasValue'] = self.static_overseas_value
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('DynamicDomesticValue') is not None:
            self.dynamic_domestic_value = m.get('DynamicDomesticValue')
        if m.get('DynamicOverseasValue') is not None:
            self.dynamic_overseas_value = m.get('DynamicOverseasValue')
        if m.get('DynamicValue') is not None:
            self.dynamic_value = m.get('DynamicValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('StaticDomesticValue') is not None:
            self.static_domestic_value = m.get('StaticDomesticValue')
        if m.get('StaticOverseasValue') is not None:
            self.static_overseas_value = m.get('StaticOverseasValue')
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainFlowDataResponseBodyFlowDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainFlowDataResponseBodyFlowDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainFlowDataResponseBodyFlowDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainFlowDataResponseBodyFlowDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainFlowDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, flow_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.flow_data_per_interval = flow_data_per_interval  # type: DescribeDomainFlowDataResponseBodyFlowDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.flow_data_per_interval:
            self.flow_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainFlowDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.flow_data_per_interval is not None:
            result['FlowDataPerInterval'] = self.flow_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowDataPerInterval') is not None:
            temp_model = DescribeDomainFlowDataResponseBodyFlowDataPerInterval()
            self.flow_data_per_interval = temp_model.from_map(m['FlowDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainFlowDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainFlowDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainFlowDataResponse, self).to_map()
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
            temp_model = DescribeDomainFlowDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHitRateDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainHitRateDataResponseBodyHitRateInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainHitRateDataResponseBodyHitRateInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHitRateDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, hit_rate_interval=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.hit_rate_interval = hit_rate_interval  # type: DescribeDomainHitRateDataResponseBodyHitRateInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.hit_rate_interval:
            self.hit_rate_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_rate_interval is not None:
            result['HitRateInterval'] = self.hit_rate_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HitRateInterval') is not None:
            temp_model = DescribeDomainHitRateDataResponseBodyHitRateInterval()
            self.hit_rate_interval = temp_model.from_map(m['HitRateInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainHitRateDataResponse, self).to_map()
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
            temp_model = DescribeDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, code_proportion_data=None):
        self.code_proportion_data = code_proportion_data  # type: list[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData]

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k in self.code_proportion_data:
                result['CodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k in m.get('CodeProportionData'):
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponseBodyHttpCodeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, http_code_data=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.http_code_data = http_code_data  # type: DescribeDomainHttpCodeDataResponseBodyHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpCodeData') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataResponse, self).to_map()
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
            temp_model = DescribeDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainISPDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainISPDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainISPDataResponseBodyValueISPProportionData(TeaModel):
    def __init__(self, avg_object_size=None, avg_response_rate=None, avg_response_time=None, bps=None,
                 byte_hit_rate=None, bytes_proportion=None, isp=None, isp_ename=None, proportion=None, qps=None, req_err_rate=None,
                 req_hit_rate=None, total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.byte_hit_rate = byte_hit_rate  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.isp = isp  # type: str
        self.isp_ename = isp_ename  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.req_err_rate = req_err_rate  # type: str
        self.req_hit_rate = req_hit_rate  # type: str
        self.total_bytes = total_bytes  # type: str
        self.total_query = total_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainISPDataResponseBodyValueISPProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDomainISPDataResponseBodyValue(TeaModel):
    def __init__(self, ispproportion_data=None):
        self.ispproportion_data = ispproportion_data  # type: list[DescribeDomainISPDataResponseBodyValueISPProportionData]

    def validate(self):
        if self.ispproportion_data:
            for k in self.ispproportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainISPDataResponseBodyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ISPProportionData'] = []
        if self.ispproportion_data is not None:
            for k in self.ispproportion_data:
                result['ISPProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ispproportion_data = []
        if m.get('ISPProportionData') is not None:
            for k in m.get('ISPProportionData'):
                temp_model = DescribeDomainISPDataResponseBodyValueISPProportionData()
                self.ispproportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainISPDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 value=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.value = value  # type: DescribeDomainISPDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainISPDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Value') is not None:
            temp_model = DescribeDomainISPDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainISPDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainISPDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainISPDataResponse, self).to_map()
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
            temp_model = DescribeDomainISPDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, domain_type=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None, owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(self, acc_domestic_value=None, acc_overseas_value=None, acc_value=None, domestic_value=None,
                 dynamic_domestic_value=None, dynamic_overseas_value=None, dynamic_value=None, overseas_value=None,
                 static_domestic_value=None, static_overseas_value=None, static_value=None, time_stamp=None, value=None):
        self.acc_domestic_value = acc_domestic_value  # type: str
        self.acc_overseas_value = acc_overseas_value  # type: str
        self.acc_value = acc_value  # type: str
        self.domestic_value = domestic_value  # type: str
        self.dynamic_domestic_value = dynamic_domestic_value  # type: str
        self.dynamic_overseas_value = dynamic_overseas_value  # type: str
        self.dynamic_value = dynamic_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.static_domestic_value = static_domestic_value  # type: str
        self.static_overseas_value = static_overseas_value  # type: str
        self.static_value = static_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value
        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.dynamic_domestic_value is not None:
            result['DynamicDomesticValue'] = self.dynamic_domestic_value
        if self.dynamic_overseas_value is not None:
            result['DynamicOverseasValue'] = self.dynamic_overseas_value
        if self.dynamic_value is not None:
            result['DynamicValue'] = self.dynamic_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.static_domestic_value is not None:
            result['StaticDomesticValue'] = self.static_domestic_value
        if self.static_overseas_value is not None:
            result['StaticOverseasValue'] = self.static_overseas_value
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')
        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('DynamicDomesticValue') is not None:
            self.dynamic_domestic_value = m.get('DynamicDomesticValue')
        if m.get('DynamicOverseasValue') is not None:
            self.dynamic_overseas_value = m.get('DynamicOverseasValue')
        if m.get('DynamicValue') is not None:
            self.dynamic_value = m.get('DynamicValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('StaticDomesticValue') is not None:
            self.static_domestic_value = m.get('StaticDomesticValue')
        if m.get('StaticOverseasValue') is not None:
            self.static_overseas_value = m.get('StaticOverseasValue')
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainQpsDataResponseBodyQpsDataInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataResponseBodyQpsDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, qps_data_interval=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.qps_data_interval = qps_data_interval  # type: DescribeDomainQpsDataResponseBodyQpsDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataResponse, self).to_map()
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
            temp_model = DescribeDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRegionDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRegionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(self, avg_object_size=None, avg_response_rate=None, avg_response_time=None, bps=None,
                 byte_hit_rate=None, bytes_proportion=None, proportion=None, qps=None, region=None, region_ename=None,
                 req_err_rate=None, req_hit_rate=None, total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.byte_hit_rate = byte_hit_rate  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.req_err_rate = req_err_rate  # type: str
        self.req_hit_rate = req_hit_rate  # type: str
        self.total_bytes = total_bytes  # type: str
        self.total_query = total_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRegionDataResponseBodyValueRegionProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(self, region_proportion_data=None):
        self.region_proportion_data = region_proportion_data  # type: list[DescribeDomainRegionDataResponseBodyValueRegionProportionData]

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRegionDataResponseBodyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k in self.region_proportion_data:
                result['RegionProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k in m.get('RegionProportionData'):
                temp_model = DescribeDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRegionDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 value=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.value = value  # type: DescribeDomainRegionDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainRegionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Value') is not None:
            temp_model = DescribeDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRegionDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainRegionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRegionDataResponse, self).to_map()
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
            temp_model = DescribeDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainReqHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainReqHitRateDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, req_hit_rate_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.req_hit_rate_interval = req_hit_rate_interval  # type: DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.req_hit_rate_interval:
            self.req_hit_rate_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_hit_rate_interval is not None:
            result['ReqHitRateInterval'] = self.req_hit_rate_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqHitRateInterval') is not None:
            temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval()
            self.req_hit_rate_interval = temp_model.from_map(m['ReqHitRateInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainReqHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainReqHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataResponse, self).to_map()
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
            temp_model = DescribeDomainReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, fix_time_gap=None, interval=None, owner_id=None,
                 start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcBpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 src_bps_data_per_interval=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.src_bps_data_per_interval = src_bps_data_per_interval  # type: DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval
        self.start_time = start_time  # type: str

    def validate(self):
        if self.src_bps_data_per_interval:
            self.src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_bps_data_per_interval is not None:
            result['SrcBpsDataPerInterval'] = self.src_bps_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcBpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval()
            self.src_bps_data_per_interval = temp_model.from_map(m['SrcBpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcBpsDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainSrcBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataResponse, self).to_map()
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
            temp_model = DescribeDomainSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcFlowDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, fix_time_gap=None, interval=None, owner_id=None,
                 start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcFlowDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcFlowDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 src_flow_data_per_interval=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.src_flow_data_per_interval = src_flow_data_per_interval  # type: DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerInterval
        self.start_time = start_time  # type: str

    def validate(self):
        if self.src_flow_data_per_interval:
            self.src_flow_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcFlowDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_flow_data_per_interval is not None:
            result['SrcFlowDataPerInterval'] = self.src_flow_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcFlowDataPerInterval') is not None:
            temp_model = DescribeDomainSrcFlowDataResponseBodySrcFlowDataPerInterval()
            self.src_flow_data_per_interval = temp_model.from_map(m['SrcFlowDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcFlowDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainSrcFlowDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcFlowDataResponse, self).to_map()
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
            temp_model = DescribeDomainSrcFlowDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, security_token=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainUvDataResponseBodyUvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainUvDataResponseBodyUvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainUvDataResponseBodyUvDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainUvDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 uv_data_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.uv_data_interval = uv_data_interval  # type: DescribeDomainUvDataResponseBodyUvDataInterval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeDomainUvDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainUvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainUvDataResponse, self).to_map()
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
            temp_model = DescribeDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsBySourceRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, sources=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsBySourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo(TeaModel):
    def __init__(self, create_time=None, domain_cname=None, domain_name=None, status=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_cname = domain_cname  # type: str
        self.domain_name = domain_name  # type: str
        self.status = status  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_cname is not None:
            result['DomainCname'] = self.domain_cname
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainCname') is not None:
            self.domain_cname = m.get('DomainCname')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos(TeaModel):
    def __init__(self, domain_info=None):
        self.domain_info = domain_info  # type: list[DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo]

    def validate(self):
        if self.domain_info:
            for k in self.domain_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['domainInfo'] = []
        if self.domain_info is not None:
            for k in self.domain_info:
                result['domainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_info = []
        if m.get('domainInfo') is not None:
            for k in m.get('domainInfo'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains(TeaModel):
    def __init__(self, domain_names=None):
        self.domain_names = domain_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['domainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainNames') is not None:
            self.domain_names = m.get('domainNames')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsData(TeaModel):
    def __init__(self, domain_infos=None, domains=None, source=None):
        self.domain_infos = domain_infos  # type: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos
        self.domains = domains  # type: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains
        self.source = source  # type: str

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBodyDomainsListDomainsData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainInfos') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos()
            self.domain_infos = temp_model.from_map(m['DomainInfos'])
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeDomainsBySourceResponseBodyDomainsList(TeaModel):
    def __init__(self, domains_data=None):
        self.domains_data = domains_data  # type: list[DescribeDomainsBySourceResponseBodyDomainsListDomainsData]

    def validate(self):
        if self.domains_data:
            for k in self.domains_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBodyDomainsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainsData'] = []
        if self.domains_data is not None:
            for k in self.domains_data:
                result['DomainsData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains_data = []
        if m.get('DomainsData') is not None:
            for k in m.get('DomainsData'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsData()
                self.domains_data.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBody(TeaModel):
    def __init__(self, domains_list=None, request_id=None, sources=None):
        self.domains_list = domains_list  # type: DescribeDomainsBySourceResponseBodyDomainsList
        self.request_id = request_id  # type: str
        self.sources = sources  # type: str

    def validate(self):
        if self.domains_list:
            self.domains_list.validate()

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains_list is not None:
            result['DomainsList'] = self.domains_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainsList') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsList()
            self.domains_list = temp_model.from_map(m['DomainsList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainsBySourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainsBySourceResponse, self).to_map()
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
            temp_model = DescribeDomainsBySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsUsageByDayRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay(TeaModel):
    def __init__(self, bytes_hit_rate=None, max_bps=None, max_bps_time=None, max_src_bps=None,
                 max_src_bps_time=None, qps=None, request_hit_rate=None, time_stamp=None, total_access=None, total_traffic=None):
        self.bytes_hit_rate = bytes_hit_rate  # type: str
        self.max_bps = max_bps  # type: str
        self.max_bps_time = max_bps_time  # type: str
        self.max_src_bps = max_src_bps  # type: str
        self.max_src_bps_time = max_src_bps_time  # type: str
        self.qps = qps  # type: str
        self.request_hit_rate = request_hit_rate  # type: str
        self.time_stamp = time_stamp  # type: str
        self.total_access = total_access  # type: str
        self.total_traffic = total_traffic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDays(TeaModel):
    def __init__(self, usage_by_day=None):
        self.usage_by_day = usage_by_day  # type: list[DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay]

    def validate(self):
        if self.usage_by_day:
            for k in self.usage_by_day:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayResponseBodyUsageByDays, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageByDay'] = []
        if self.usage_by_day is not None:
            for k in self.usage_by_day:
                result['UsageByDay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_by_day = []
        if m.get('UsageByDay') is not None:
            for k in m.get('UsageByDay'):
                temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay()
                self.usage_by_day.append(temp_model.from_map(k))
        return self


class DescribeDomainsUsageByDayResponseBodyUsageTotal(TeaModel):
    def __init__(self, bytes_hit_rate=None, max_bps=None, max_bps_time=None, max_src_bps=None,
                 max_src_bps_time=None, request_hit_rate=None, total_access=None, total_traffic=None):
        self.bytes_hit_rate = bytes_hit_rate  # type: str
        self.max_bps = max_bps  # type: str
        self.max_bps_time = max_bps_time  # type: str
        self.max_src_bps = max_src_bps  # type: str
        self.max_src_bps_time = max_src_bps_time  # type: str
        self.request_hit_rate = request_hit_rate  # type: str
        self.total_access = total_access  # type: str
        self.total_traffic = total_traffic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayResponseBodyUsageTotal, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        return self


class DescribeDomainsUsageByDayResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 usage_by_days=None, usage_total=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.usage_by_days = usage_by_days  # type: DescribeDomainsUsageByDayResponseBodyUsageByDays
        self.usage_total = usage_total  # type: DescribeDomainsUsageByDayResponseBodyUsageTotal

    def validate(self):
        if self.usage_by_days:
            self.usage_by_days.validate()
        if self.usage_total:
            self.usage_total.validate()

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.usage_by_days is not None:
            result['UsageByDays'] = self.usage_by_days.to_map()
        if self.usage_total is not None:
            result['UsageTotal'] = self.usage_total.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UsageByDays') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDays()
            self.usage_by_days = temp_model.from_map(m['UsageByDays'])
        if m.get('UsageTotal') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageTotal()
            self.usage_total = temp_model.from_map(m['UsageTotal'])
        return self


class DescribeDomainsUsageByDayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainsUsageByDayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainsUsageByDayResponse, self).to_map()
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
            temp_model = DescribeDomainsUsageByDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRefreshQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRefreshQuotaResponseBody(TeaModel):
    def __init__(self, block_quota=None, block_remain=None, dir_quota=None, dir_remain=None, preload_quota=None,
                 preload_remain=None, request_id=None, url_quota=None, url_remain=None):
        self.block_quota = block_quota  # type: str
        self.block_remain = block_remain  # type: str
        self.dir_quota = dir_quota  # type: str
        self.dir_remain = dir_remain  # type: str
        self.preload_quota = preload_quota  # type: str
        self.preload_remain = preload_remain  # type: str
        self.request_id = request_id  # type: str
        self.url_quota = url_quota  # type: str
        self.url_remain = url_remain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRefreshQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        return self


class DescribeRefreshQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRefreshQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRefreshQuotaResponse, self).to_map()
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
            temp_model = DescribeRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopDomainsByFlowRequest(TeaModel):
    def __init__(self, end_time=None, limit=None, owner_id=None, product=None, start_time=None):
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
        self.product = product  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopDomainsByFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(self, domain_name=None, max_bps=None, max_bps_time=None, rank=None, total_access=None,
                 total_traffic=None, traffic_percent=None):
        self.domain_name = domain_name  # type: str
        self.max_bps = max_bps  # type: float
        self.max_bps_time = max_bps_time  # type: str
        self.rank = rank  # type: long
        self.total_access = total_access  # type: long
        self.total_traffic = total_traffic  # type: str
        self.traffic_percent = traffic_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        return self


class DescribeTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(self, top_domain=None):
        self.top_domain = top_domain  # type: list[DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain]

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTopDomainsByFlowResponseBodyTopDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k in m.get('TopDomain'):
                temp_model = DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeTopDomainsByFlowResponseBody(TeaModel):
    def __init__(self, domain_count=None, domain_online_count=None, end_time=None, request_id=None, start_time=None,
                 top_domains=None):
        self.domain_count = domain_count  # type: long
        self.domain_online_count = domain_online_count  # type: long
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.top_domains = top_domains  # type: DescribeTopDomainsByFlowResponseBodyTopDomains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super(DescribeTopDomainsByFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopDomains') is not None:
            temp_model = DescribeTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeTopDomainsByFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTopDomainsByFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTopDomainsByFlowResponse, self).to_map()
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
            temp_model = DescribeTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDomainsRequest(TeaModel):
    def __init__(self, cdn_type=None, check_domain_show=None, domain_name=None, domain_search_type=None,
                 domain_status=None, owner_id=None, page_number=None, page_size=None, resource_group_id=None, security_token=None,
                 sources=None):
        self.cdn_type = cdn_type  # type: str
        self.check_domain_show = check_domain_show  # type: bool
        self.domain_name = domain_name  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.domain_status = domain_status  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBodyDomainsPageDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cdn_type=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, resource_group_id=None, sandbox=None, source_type=None, sources=None,
                 ssl_protocol=None):
        self.cdn_type = cdn_type  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
        self.source_type = source_type  # type: str
        self.sources = sources  # type: DescribeUserDomainsResponseBodyDomainsPageDataSources
        self.ssl_protocol = ssl_protocol  # type: str

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Sources') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        return self


class DescribeUserDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeUserDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeUserDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
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
        if m.get('Domains') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsResponse, self).to_map()
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
            temp_model = DescribeUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdnServiceRequest(TeaModel):
    def __init__(self, internet_charge_type=None, owner_id=None, security_token=None):
        self.internet_charge_type = internet_charge_type  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCdnServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class OpenCdnServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCdnServiceResponseBody, self).to_map()
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


class OpenCdnServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenCdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenCdnServiceResponse, self).to_map()
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
            temp_model = OpenCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushObjectCacheRequest(TeaModel):
    def __init__(self, area=None, object_path=None, owner_id=None, security_token=None):
        self.area = area  # type: str
        self.object_path = object_path  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushObjectCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PushObjectCacheResponseBody(TeaModel):
    def __init__(self, push_task_id=None, request_id=None):
        self.push_task_id = push_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushObjectCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_task_id is not None:
            result['PushTaskId'] = self.push_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PushTaskId') is not None:
            self.push_task_id = m.get('PushTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushObjectCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushObjectCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushObjectCacheResponse, self).to_map()
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
            temp_model = PushObjectCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshObjectCachesRequest(TeaModel):
    def __init__(self, object_path=None, object_type=None, owner_id=None, security_token=None):
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshObjectCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RefreshObjectCachesResponseBody(TeaModel):
    def __init__(self, refresh_task_id=None, request_id=None):
        self.refresh_task_id = refresh_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshObjectCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshObjectCachesResponse, self).to_map()
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
            temp_model = RefreshObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestDescribeDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, domain_type=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestDescribeDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class TestDescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_l2value=None, domestic_value=None, dynamic_domestic_value=None,
                 dynamic_overseas_value=None, dynamic_value=None, l_2value=None, overseas_l2value=None, overseas_value=None,
                 static_domestic_value=None, static_overseas_value=None, static_value=None, time_stamp=None, value=None):
        self.domestic_l2value = domestic_l2value  # type: str
        self.domestic_value = domestic_value  # type: str
        self.dynamic_domestic_value = dynamic_domestic_value  # type: str
        self.dynamic_overseas_value = dynamic_overseas_value  # type: str
        self.dynamic_value = dynamic_value  # type: str
        self.l_2value = l_2value  # type: str
        self.overseas_l2value = overseas_l2value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.static_domestic_value = static_domestic_value  # type: str
        self.static_overseas_value = static_overseas_value  # type: str
        self.static_value = static_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestDescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_l2value is not None:
            result['DomesticL2Value'] = self.domestic_l2value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.dynamic_domestic_value is not None:
            result['DynamicDomesticValue'] = self.dynamic_domestic_value
        if self.dynamic_overseas_value is not None:
            result['DynamicOverseasValue'] = self.dynamic_overseas_value
        if self.dynamic_value is not None:
            result['DynamicValue'] = self.dynamic_value
        if self.l_2value is not None:
            result['L2Value'] = self.l_2value
        if self.overseas_l2value is not None:
            result['OverseasL2Value'] = self.overseas_l2value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.static_domestic_value is not None:
            result['StaticDomesticValue'] = self.static_domestic_value
        if self.static_overseas_value is not None:
            result['StaticOverseasValue'] = self.static_overseas_value
        if self.static_value is not None:
            result['StaticValue'] = self.static_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticL2Value') is not None:
            self.domestic_l2value = m.get('DomesticL2Value')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('DynamicDomesticValue') is not None:
            self.dynamic_domestic_value = m.get('DynamicDomesticValue')
        if m.get('DynamicOverseasValue') is not None:
            self.dynamic_overseas_value = m.get('DynamicOverseasValue')
        if m.get('DynamicValue') is not None:
            self.dynamic_value = m.get('DynamicValue')
        if m.get('L2Value') is not None:
            self.l_2value = m.get('L2Value')
        if m.get('OverseasL2Value') is not None:
            self.overseas_l2value = m.get('OverseasL2Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('StaticDomesticValue') is not None:
            self.static_domestic_value = m.get('StaticDomesticValue')
        if m.get('StaticOverseasValue') is not None:
            self.static_overseas_value = m.get('StaticOverseasValue')
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TestDescribeDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[TestDescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TestDescribeDomainBpsDataResponseBodyBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = TestDescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class TestDescribeDomainBpsDataResponseBody(TeaModel):
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 isp_name=None, isp_name_en=None, location_name=None, location_name_en=None, request_id=None,
                 start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: TestDescribeDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name = isp_name  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name = location_name  # type: str
        self.location_name_en = location_name_en  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(TestDescribeDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = TestDescribeDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class TestDescribeDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TestDescribeDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TestDescribeDomainBpsDataResponse, self).to_map()
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
            temp_model = TestDescribeDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


