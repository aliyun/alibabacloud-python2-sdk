# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDomainRequest(TeaModel):
    def __init__(self, account_id=None, domain_name=None):
        self.account_id = account_id  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class AddDomainResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDomainResponse, self).to_map()
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
            temp_model = AddDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, account_id=None, domain_name=None):
        self.account_id = account_id  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(self, account_id=None, page_number=None, page_size=None):
        self.account_id = account_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainsResponseBodyDomainsDomain(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomainsDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainsResponseBodyDomains(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: list[DescribeDomainsResponseBodyDomainsDomain]

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = DescribeDomainsResponseBodyDomainsDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponseBody, self).to_map()
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
            temp_model = DescribeDomainsResponseBodyDomains()
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


class DescribeDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponse, self).to_map()
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountInfoResponseBodyAccountInfo(TeaModel):
    def __init__(self, account_id=None, month_free_count=None, month_https_resolve_count=None,
                 month_resolve_count=None, sign_secret=None, signed_count=None, unsigned_count=None, unsigned_enabled=None):
        self.account_id = account_id  # type: str
        self.month_free_count = month_free_count  # type: int
        self.month_https_resolve_count = month_https_resolve_count  # type: int
        self.month_resolve_count = month_resolve_count  # type: int
        self.sign_secret = sign_secret  # type: str
        self.signed_count = signed_count  # type: long
        self.unsigned_count = unsigned_count  # type: long
        self.unsigned_enabled = unsigned_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountInfoResponseBodyAccountInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.month_free_count is not None:
            result['MonthFreeCount'] = self.month_free_count
        if self.month_https_resolve_count is not None:
            result['MonthHttpsResolveCount'] = self.month_https_resolve_count
        if self.month_resolve_count is not None:
            result['MonthResolveCount'] = self.month_resolve_count
        if self.sign_secret is not None:
            result['SignSecret'] = self.sign_secret
        if self.signed_count is not None:
            result['SignedCount'] = self.signed_count
        if self.unsigned_count is not None:
            result['UnsignedCount'] = self.unsigned_count
        if self.unsigned_enabled is not None:
            result['UnsignedEnabled'] = self.unsigned_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MonthFreeCount') is not None:
            self.month_free_count = m.get('MonthFreeCount')
        if m.get('MonthHttpsResolveCount') is not None:
            self.month_https_resolve_count = m.get('MonthHttpsResolveCount')
        if m.get('MonthResolveCount') is not None:
            self.month_resolve_count = m.get('MonthResolveCount')
        if m.get('SignSecret') is not None:
            self.sign_secret = m.get('SignSecret')
        if m.get('SignedCount') is not None:
            self.signed_count = m.get('SignedCount')
        if m.get('UnsignedCount') is not None:
            self.unsigned_count = m.get('UnsignedCount')
        if m.get('UnsignedEnabled') is not None:
            self.unsigned_enabled = m.get('UnsignedEnabled')
        return self


class GetAccountInfoResponseBody(TeaModel):
    def __init__(self, account_info=None, request_id=None):
        self.account_info = account_info  # type: GetAccountInfoResponseBodyAccountInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account_info:
            self.account_info.validate()

    def to_map(self):
        _map = super(GetAccountInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info is not None:
            result['AccountInfo'] = self.account_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountInfo') is not None:
            temp_model = GetAccountInfoResponseBodyAccountInfo()
            self.account_info = temp_model.from_map(m['AccountInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccountInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountInfoResponse, self).to_map()
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
            temp_model = GetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResolveCountSummaryRequest(TeaModel):
    def __init__(self, granularity=None, time_span=None):
        self.granularity = granularity  # type: str
        self.time_span = time_span  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResolveCountSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        return self


class GetResolveCountSummaryResponseBodyResolveSummary(TeaModel):
    def __init__(self, http=None, http_6=None, https=None, https_6=None):
        self.http = http  # type: long
        self.http_6 = http_6  # type: long
        self.https = https  # type: long
        self.https_6 = https_6  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResolveCountSummaryResponseBodyResolveSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['Http'] = self.http
        if self.http_6 is not None:
            result['Http6'] = self.http_6
        if self.https is not None:
            result['Https'] = self.https
        if self.https_6 is not None:
            result['Https6'] = self.https_6
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http') is not None:
            self.http = m.get('Http')
        if m.get('Http6') is not None:
            self.http_6 = m.get('Http6')
        if m.get('Https') is not None:
            self.https = m.get('Https')
        if m.get('Https6') is not None:
            self.https_6 = m.get('Https6')
        return self


class GetResolveCountSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, resolve_summary=None):
        self.request_id = request_id  # type: str
        self.resolve_summary = resolve_summary  # type: GetResolveCountSummaryResponseBodyResolveSummary

    def validate(self):
        if self.resolve_summary:
            self.resolve_summary.validate()

    def to_map(self):
        _map = super(GetResolveCountSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolve_summary is not None:
            result['ResolveSummary'] = self.resolve_summary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolveSummary') is not None:
            temp_model = GetResolveCountSummaryResponseBodyResolveSummary()
            self.resolve_summary = temp_model.from_map(m['ResolveSummary'])
        return self


class GetResolveCountSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResolveCountSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResolveCountSummaryResponse, self).to_map()
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
            temp_model = GetResolveCountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResolveStatisticsRequest(TeaModel):
    def __init__(self, domain_name=None, granularity=None, protocol_name=None, time_span=None):
        self.domain_name = domain_name  # type: str
        self.granularity = granularity  # type: str
        self.protocol_name = protocol_name  # type: str
        self.time_span = time_span  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResolveStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        return self


class GetResolveStatisticsResponseBodyDataPointsDataPoint(TeaModel):
    def __init__(self, count=None, time=None):
        self.count = count  # type: int
        self.time = time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResolveStatisticsResponseBodyDataPointsDataPoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetResolveStatisticsResponseBodyDataPoints(TeaModel):
    def __init__(self, data_point=None):
        self.data_point = data_point  # type: list[GetResolveStatisticsResponseBodyDataPointsDataPoint]

    def validate(self):
        if self.data_point:
            for k in self.data_point:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResolveStatisticsResponseBodyDataPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataPoint'] = []
        if self.data_point is not None:
            for k in self.data_point:
                result['DataPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_point = []
        if m.get('DataPoint') is not None:
            for k in m.get('DataPoint'):
                temp_model = GetResolveStatisticsResponseBodyDataPointsDataPoint()
                self.data_point.append(temp_model.from_map(k))
        return self


class GetResolveStatisticsResponseBody(TeaModel):
    def __init__(self, data_points=None, request_id=None):
        self.data_points = data_points  # type: GetResolveStatisticsResponseBodyDataPoints
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_points:
            self.data_points.validate()

    def to_map(self):
        _map = super(GetResolveStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_points is not None:
            result['DataPoints'] = self.data_points.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPoints') is not None:
            temp_model = GetResolveStatisticsResponseBodyDataPoints()
            self.data_points = temp_model.from_map(m['DataPoints'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResolveStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResolveStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResolveStatisticsResponse, self).to_map()
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
            temp_model = GetResolveStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsRequest, self).to_map()
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


class ListDomainsResponseBodyDomainInfosDomainInfo(TeaModel):
    def __init__(self, domain_name=None, resolved=None, resolved_6=None, resolved_https=None, resolved_https_6=None):
        self.domain_name = domain_name  # type: str
        self.resolved = resolved  # type: long
        self.resolved_6 = resolved_6  # type: long
        self.resolved_https = resolved_https  # type: long
        self.resolved_https_6 = resolved_https_6  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsResponseBodyDomainInfosDomainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resolved is not None:
            result['Resolved'] = self.resolved
        if self.resolved_6 is not None:
            result['Resolved6'] = self.resolved_6
        if self.resolved_https is not None:
            result['ResolvedHttps'] = self.resolved_https
        if self.resolved_https_6 is not None:
            result['ResolvedHttps6'] = self.resolved_https_6
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Resolved') is not None:
            self.resolved = m.get('Resolved')
        if m.get('Resolved6') is not None:
            self.resolved_6 = m.get('Resolved6')
        if m.get('ResolvedHttps') is not None:
            self.resolved_https = m.get('ResolvedHttps')
        if m.get('ResolvedHttps6') is not None:
            self.resolved_https_6 = m.get('ResolvedHttps6')
        return self


class ListDomainsResponseBodyDomainInfos(TeaModel):
    def __init__(self, domain_info=None):
        self.domain_info = domain_info  # type: list[ListDomainsResponseBodyDomainInfosDomainInfo]

    def validate(self):
        if self.domain_info:
            for k in self.domain_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBodyDomainInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainInfo'] = []
        if self.domain_info is not None:
            for k in self.domain_info:
                result['DomainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_info = []
        if m.get('DomainInfo') is not None:
            for k in m.get('DomainInfo'):
                temp_model = ListDomainsResponseBodyDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k))
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(self, domain_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domain_infos = domain_infos  # type: ListDomainsResponseBodyDomainInfos
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()
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
        if m.get('DomainInfos') is not None:
            temp_model = ListDomainsResponseBodyDomainInfos()
            self.domain_infos = temp_model.from_map(m['DomainInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainsResponse, self).to_map()
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
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


