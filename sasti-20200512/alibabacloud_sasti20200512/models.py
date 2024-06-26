# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeDomainReportRequest(TeaModel):
    def __init__(self, domain=None, field=None, service_lang=None):
        self.domain = domain  # type: str
        self.field = field  # type: str
        self.service_lang = service_lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.field is not None:
            result['Field'] = self.field
        if self.service_lang is not None:
            result['ServiceLang'] = self.service_lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('ServiceLang') is not None:
            self.service_lang = m.get('ServiceLang')
        return self


class DescribeDomainReportResponseBody(TeaModel):
    def __init__(self, attack_cnt_by_threat_type=None, attack_preference_top_5=None, basic=None, confidence=None,
                 context=None, domain=None, group=None, intelligences=None, request_id=None, scenario=None, ssl_cert=None,
                 threat_level=None, threat_types=None, whois=None):
        self.attack_cnt_by_threat_type = attack_cnt_by_threat_type  # type: str
        self.attack_preference_top_5 = attack_preference_top_5  # type: str
        self.basic = basic  # type: str
        self.confidence = confidence  # type: str
        self.context = context  # type: str
        self.domain = domain  # type: str
        self.group = group  # type: str
        self.intelligences = intelligences  # type: str
        self.request_id = request_id  # type: str
        self.scenario = scenario  # type: str
        self.ssl_cert = ssl_cert  # type: str
        self.threat_level = threat_level  # type: str
        self.threat_types = threat_types  # type: str
        self.whois = whois  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_cnt_by_threat_type is not None:
            result['AttackCntByThreatType'] = self.attack_cnt_by_threat_type
        if self.attack_preference_top_5 is not None:
            result['AttackPreferenceTop5'] = self.attack_preference_top_5
        if self.basic is not None:
            result['Basic'] = self.basic
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.context is not None:
            result['Context'] = self.context
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group is not None:
            result['Group'] = self.group
        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.ssl_cert is not None:
            result['SslCert'] = self.ssl_cert
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types
        if self.whois is not None:
            result['Whois'] = self.whois
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackCntByThreatType') is not None:
            self.attack_cnt_by_threat_type = m.get('AttackCntByThreatType')
        if m.get('AttackPreferenceTop5') is not None:
            self.attack_preference_top_5 = m.get('AttackPreferenceTop5')
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('SslCert') is not None:
            self.ssl_cert = m.get('SslCert')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')
        if m.get('Whois') is not None:
            self.whois = m.get('Whois')
        return self


class DescribeDomainReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainReportResponse, self).to_map()
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
            temp_model = DescribeDomainReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileReportRequest(TeaModel):
    def __init__(self, field=None, file_hash=None, service_lang=None):
        self.field = field  # type: str
        self.file_hash = file_hash  # type: str
        self.service_lang = service_lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.service_lang is not None:
            result['ServiceLang'] = self.service_lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('ServiceLang') is not None:
            self.service_lang = m.get('ServiceLang')
        return self


class DescribeFileReportResponseBody(TeaModel):
    def __init__(self, basic=None, file_hash=None, intelligences=None, request_id=None, sandbox=None,
                 threat_level=None, threat_types=None):
        self.basic = basic  # type: str
        self.file_hash = file_hash  # type: str
        self.intelligences = intelligences  # type: str
        self.request_id = request_id  # type: str
        self.sandbox = sandbox  # type: str
        self.threat_level = threat_level  # type: str
        self.threat_types = threat_types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['Basic'] = self.basic
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')
        return self


class DescribeFileReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFileReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFileReportResponse, self).to_map()
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
            temp_model = DescribeFileReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpReportRequest(TeaModel):
    def __init__(self, field=None, ip=None, service_lang=None):
        self.field = field  # type: str
        self.ip = ip  # type: str
        self.service_lang = service_lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.service_lang is not None:
            result['ServiceLang'] = self.service_lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ServiceLang') is not None:
            self.service_lang = m.get('ServiceLang')
        return self


class DescribeIpReportResponseBody(TeaModel):
    def __init__(self, attack_cnt_by_threat_type=None, attack_preference_top_5=None, confidence=None, context=None,
                 group=None, intelligences=None, ip=None, request_id=None, scenario=None, threat_level=None,
                 threat_types=None, whois=None):
        self.attack_cnt_by_threat_type = attack_cnt_by_threat_type  # type: str
        self.attack_preference_top_5 = attack_preference_top_5  # type: str
        self.confidence = confidence  # type: str
        self.context = context  # type: str
        self.group = group  # type: str
        self.intelligences = intelligences  # type: str
        self.ip = ip  # type: str
        self.request_id = request_id  # type: str
        self.scenario = scenario  # type: str
        self.threat_level = threat_level  # type: str
        self.threat_types = threat_types  # type: str
        self.whois = whois  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_cnt_by_threat_type is not None:
            result['AttackCntByThreatType'] = self.attack_cnt_by_threat_type
        if self.attack_preference_top_5 is not None:
            result['AttackPreferenceTop5'] = self.attack_preference_top_5
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.context is not None:
            result['Context'] = self.context
        if self.group is not None:
            result['Group'] = self.group
        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types
        if self.whois is not None:
            result['Whois'] = self.whois
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackCntByThreatType') is not None:
            self.attack_cnt_by_threat_type = m.get('AttackCntByThreatType')
        if m.get('AttackPreferenceTop5') is not None:
            self.attack_preference_top_5 = m.get('AttackPreferenceTop5')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')
        if m.get('Whois') is not None:
            self.whois = m.get('Whois')
        return self


class DescribeIpReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpReportResponse, self).to_map()
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
            temp_model = DescribeIpReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


