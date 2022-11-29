# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateClientCertificateRequest(TeaModel):
    def __init__(self, after_time=None, algorithm=None, before_time=None, common_name=None, country=None, csr=None,
                 days=None, immediately=None, locality=None, months=None, organization=None, organization_unit=None,
                 parent_identifier=None, san_type=None, san_value=None, state=None, years=None):
        self.after_time = after_time  # type: long
        self.algorithm = algorithm  # type: str
        self.before_time = before_time  # type: long
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.csr = csr  # type: str
        self.days = days  # type: int
        self.immediately = immediately  # type: int
        self.locality = locality  # type: str
        self.months = months  # type: int
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.san_type = san_type  # type: int
        self.san_value = san_value  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.days is not None:
            result['Days'] = self.days
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.san_type is not None:
            result['SanType'] = self.san_type
        if self.san_value is not None:
            result['SanValue'] = self.san_value
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')
        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateClientCertificateResponseBody(TeaModel):
    def __init__(self, certificate_chain=None, identifier=None, parent_x509certificate=None, request_id=None,
                 root_x509certificate=None, x_509certificate=None):
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.parent_x509certificate = parent_x509certificate  # type: str
        self.request_id = request_id  # type: str
        self.root_x509certificate = root_x509certificate  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.parent_x509certificate is not None:
            result['ParentX509Certificate'] = self.parent_x509certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_x509certificate is not None:
            result['RootX509Certificate'] = self.root_x509certificate
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('ParentX509Certificate') is not None:
            self.parent_x509certificate = m.get('ParentX509Certificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootX509Certificate') is not None:
            self.root_x509certificate = m.get('RootX509Certificate')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClientCertificateResponse, self).to_map()
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
            temp_model = CreateClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClientCertificateWithCsrRequest(TeaModel):
    def __init__(self, after_time=None, algorithm=None, before_time=None, common_name=None, country=None, csr=None,
                 csr_1=None, days=None, immediately=None, locality=None, months=None, organization=None,
                 organization_unit=None, parent_identifier=None, san_type=None, san_value=None, state=None, years=None):
        self.after_time = after_time  # type: long
        self.algorithm = algorithm  # type: str
        self.before_time = before_time  # type: long
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.csr = csr  # type: str
        self.csr_1 = csr_1  # type: str
        self.days = days  # type: int
        self.immediately = immediately  # type: int
        self.locality = locality  # type: str
        self.months = months  # type: int
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.san_type = san_type  # type: int
        self.san_value = san_value  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientCertificateWithCsrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.csr_1 is not None:
            result['Csr1'] = self.csr_1
        if self.days is not None:
            result['Days'] = self.days
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.san_type is not None:
            result['SanType'] = self.san_type
        if self.san_value is not None:
            result['SanValue'] = self.san_value
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Csr1') is not None:
            self.csr_1 = m.get('Csr1')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')
        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateClientCertificateWithCsrResponseBody(TeaModel):
    def __init__(self, certificate_chain=None, identifier=None, parent_x509certificate=None, request_id=None,
                 root_x509certificate=None, x_509certificate=None):
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.parent_x509certificate = parent_x509certificate  # type: str
        self.request_id = request_id  # type: str
        self.root_x509certificate = root_x509certificate  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientCertificateWithCsrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.parent_x509certificate is not None:
            result['ParentX509Certificate'] = self.parent_x509certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_x509certificate is not None:
            result['RootX509Certificate'] = self.root_x509certificate
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('ParentX509Certificate') is not None:
            self.parent_x509certificate = m.get('ParentX509Certificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootX509Certificate') is not None:
            self.root_x509certificate = m.get('RootX509Certificate')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateClientCertificateWithCsrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClientCertificateWithCsrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClientCertificateWithCsrResponse, self).to_map()
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
            temp_model = CreateClientCertificateWithCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRevokeClientCertificateRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRevokeClientCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class CreateRevokeClientCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRevokeClientCertificateResponseBody, self).to_map()
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


class CreateRevokeClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRevokeClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRevokeClientCertificateResponse, self).to_map()
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
            temp_model = CreateRevokeClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRootCACertificateRequest(TeaModel):
    def __init__(self, algorithm=None, common_name=None, country_code=None, locality=None, organization=None,
                 organization_unit=None, state=None, years=None):
        self.algorithm = algorithm  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.locality = locality  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRootCACertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateRootCACertificateResponseBody(TeaModel):
    def __init__(self, certificate=None, certificate_chain=None, identifier=None, request_id=None):
        self.certificate = certificate  # type: str
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRootCACertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRootCACertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRootCACertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRootCACertificateResponse, self).to_map()
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
            temp_model = CreateRootCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerCertificateRequest(TeaModel):
    def __init__(self, after_time=None, algorithm=None, before_time=None, common_name=None, country=None, csr=None,
                 days=None, domain=None, immediately=None, locality=None, months=None, organization=None,
                 organization_unit=None, parent_identifier=None, state=None, years=None):
        self.after_time = after_time  # type: long
        self.algorithm = algorithm  # type: str
        self.before_time = before_time  # type: long
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.csr = csr  # type: str
        self.days = days  # type: int
        self.domain = domain  # type: str
        self.immediately = immediately  # type: int
        self.locality = locality  # type: str
        self.months = months  # type: int
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.days is not None:
            result['Days'] = self.days
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateServerCertificateResponseBody(TeaModel):
    def __init__(self, certificate_chain=None, identifier=None, parent_x509certificate=None, request_id=None,
                 root_x509certificate=None, x_509certificate=None):
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.parent_x509certificate = parent_x509certificate  # type: str
        self.request_id = request_id  # type: str
        self.root_x509certificate = root_x509certificate  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.parent_x509certificate is not None:
            result['ParentX509Certificate'] = self.parent_x509certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_x509certificate is not None:
            result['RootX509Certificate'] = self.root_x509certificate
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('ParentX509Certificate') is not None:
            self.parent_x509certificate = m.get('ParentX509Certificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootX509Certificate') is not None:
            self.root_x509certificate = m.get('RootX509Certificate')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateServerCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServerCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServerCertificateResponse, self).to_map()
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
            temp_model = CreateServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerCertificateWithCsrRequest(TeaModel):
    def __init__(self, after_time=None, algorithm=None, before_time=None, common_name=None, country=None, csr=None,
                 csr_1=None, days=None, domain=None, immediately=None, locality=None, months=None, organization=None,
                 organization_unit=None, parent_identifier=None, state=None, years=None):
        self.after_time = after_time  # type: long
        self.algorithm = algorithm  # type: str
        self.before_time = before_time  # type: long
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.csr = csr  # type: str
        self.csr_1 = csr_1  # type: str
        self.days = days  # type: int
        self.domain = domain  # type: str
        self.immediately = immediately  # type: int
        self.locality = locality  # type: str
        self.months = months  # type: int
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerCertificateWithCsrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.csr_1 is not None:
            result['Csr1'] = self.csr_1
        if self.days is not None:
            result['Days'] = self.days
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Csr1') is not None:
            self.csr_1 = m.get('Csr1')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateServerCertificateWithCsrResponseBody(TeaModel):
    def __init__(self, certificate_chain=None, identifier=None, parent_x509certificate=None, request_id=None,
                 root_x509certificate=None, x_509certificate=None):
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.parent_x509certificate = parent_x509certificate  # type: str
        self.request_id = request_id  # type: str
        self.root_x509certificate = root_x509certificate  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerCertificateWithCsrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.parent_x509certificate is not None:
            result['ParentX509Certificate'] = self.parent_x509certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_x509certificate is not None:
            result['RootX509Certificate'] = self.root_x509certificate
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('ParentX509Certificate') is not None:
            self.parent_x509certificate = m.get('ParentX509Certificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootX509Certificate') is not None:
            self.root_x509certificate = m.get('RootX509Certificate')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateServerCertificateWithCsrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServerCertificateWithCsrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServerCertificateWithCsrResponse, self).to_map()
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
            temp_model = CreateServerCertificateWithCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubCACertificateRequest(TeaModel):
    def __init__(self, algorithm=None, common_name=None, country_code=None, locality=None, organization=None,
                 organization_unit=None, parent_identifier=None, state=None, years=None):
        self.algorithm = algorithm  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.locality = locality  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.state = state  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubCACertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateSubCACertificateResponseBody(TeaModel):
    def __init__(self, certificate=None, certificate_chain=None, identifier=None, request_id=None):
        self.certificate = certificate  # type: str
        self.certificate_chain = certificate_chain  # type: str
        self.identifier = identifier  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubCACertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSubCACertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSubCACertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubCACertificateResponse, self).to_map()
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
            temp_model = CreateSubCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClientCertificateRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DeleteClientCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientCertificateResponseBody, self).to_map()
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


class DeleteClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClientCertificateResponse, self).to_map()
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
            temp_model = DeleteClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCACertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeCACertificateResponseBodyCertificate(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, certificate_type=None, common_name=None,
                 country_code=None, crl_status=None, crl_url=None, identifier=None, key_size=None, locality=None, md_5=None,
                 organization=None, organization_unit=None, parent_identifier=None, sans=None, serial_number=None, sha_2=None,
                 sign_algorithm=None, state=None, status=None, subject_dn=None, x_509certificate=None):
        self.after_date = after_date  # type: long
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: long
        self.certificate_type = certificate_type  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.crl_status = crl_status  # type: str
        self.crl_url = crl_url  # type: str
        self.identifier = identifier  # type: str
        self.key_size = key_size  # type: int
        self.locality = locality  # type: str
        self.md_5 = md_5  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.sans = sans  # type: str
        self.serial_number = serial_number  # type: str
        self.sha_2 = sha_2  # type: str
        self.sign_algorithm = sign_algorithm  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.subject_dn = subject_dn  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCACertificateResponseBodyCertificate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.crl_status is not None:
            result['CrlStatus'] = self.crl_status
        if self.crl_url is not None:
            result['CrlUrl'] = self.crl_url
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CrlStatus') is not None:
            self.crl_status = m.get('CrlStatus')
        if m.get('CrlUrl') is not None:
            self.crl_url = m.get('CrlUrl')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class DescribeCACertificateResponseBody(TeaModel):
    def __init__(self, certificate=None, request_id=None, years=None):
        self.certificate = certificate  # type: DescribeCACertificateResponseBodyCertificate
        self.request_id = request_id  # type: str
        self.years = years  # type: int

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        _map = super(DescribeCACertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = DescribeCACertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class DescribeCACertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCACertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCACertificateResponse, self).to_map()
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
            temp_model = DescribeCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateCountResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCACertificateCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCACertificateCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCACertificateCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCACertificateCountResponse, self).to_map()
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
            temp_model = DescribeCACertificateCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateListRequest(TeaModel):
    def __init__(self, current_page=None, show_size=None):
        self.current_page = current_page  # type: int
        self.show_size = show_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCACertificateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class DescribeCACertificateListResponseBodyCertificateList(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, certificate_type=None, common_name=None,
                 country_code=None, identifier=None, key_size=None, locality=None, md_5=None, organization=None,
                 organization_unit=None, parent_identifier=None, sans=None, serial_number=None, sha_2=None, sign_algorithm=None,
                 state=None, status=None, subject_dn=None, x_509certificate=None, years=None):
        self.after_date = after_date  # type: long
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: long
        self.certificate_type = certificate_type  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.identifier = identifier  # type: str
        self.key_size = key_size  # type: int
        self.locality = locality  # type: str
        self.md_5 = md_5  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.sans = sans  # type: str
        self.serial_number = serial_number  # type: str
        self.sha_2 = sha_2  # type: str
        self.sign_algorithm = sign_algorithm  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.subject_dn = subject_dn  # type: str
        self.x_509certificate = x_509certificate  # type: str
        self.years = years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCACertificateListResponseBodyCertificateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class DescribeCACertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list=None, current_page=None, page_count=None, request_id=None, show_size=None,
                 total_count=None):
        self.certificate_list = certificate_list  # type: list[DescribeCACertificateListResponseBodyCertificateList]
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCACertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = DescribeCACertificateListResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCACertificateListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCACertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCACertificateListResponse, self).to_map()
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
            temp_model = DescribeCACertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificatePrivateKeyRequest(TeaModel):
    def __init__(self, encrypted_code=None, identifier=None):
        self.encrypted_code = encrypted_code  # type: str
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificatePrivateKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_code is not None:
            result['EncryptedCode'] = self.encrypted_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedCode') is not None:
            self.encrypted_code = m.get('EncryptedCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeCertificatePrivateKeyResponseBody(TeaModel):
    def __init__(self, encrypted_data=None, request_id=None):
        self.encrypted_data = encrypted_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificatePrivateKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_data is not None:
            result['EncryptedData'] = self.encrypted_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedData') is not None:
            self.encrypted_data = m.get('EncryptedData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificatePrivateKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCertificatePrivateKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertificatePrivateKeyResponse, self).to_map()
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
            temp_model = DescribeCertificatePrivateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientCertificateRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeClientCertificateResponseBodyCertificate(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, certificate_type=None, common_name=None,
                 country_code=None, days=None, identifier=None, key_size=None, locality=None, md_5=None, organization=None,
                 organization_unit=None, parent_identifier=None, sans=None, serial_number=None, sha_2=None, sign_algorithm=None,
                 state=None, status=None, subject_dn=None, x_509certificate=None):
        self.after_date = after_date  # type: long
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: long
        self.certificate_type = certificate_type  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.days = days  # type: int
        self.identifier = identifier  # type: str
        self.key_size = key_size  # type: int
        self.locality = locality  # type: str
        self.md_5 = md_5  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.sans = sans  # type: str
        self.serial_number = serial_number  # type: str
        self.sha_2 = sha_2  # type: str
        self.sign_algorithm = sign_algorithm  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.subject_dn = subject_dn  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientCertificateResponseBodyCertificate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.days is not None:
            result['Days'] = self.days
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class DescribeClientCertificateResponseBody(TeaModel):
    def __init__(self, certificate=None, request_id=None):
        self.certificate = certificate  # type: DescribeClientCertificateResponseBodyCertificate
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        _map = super(DescribeClientCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = DescribeClientCertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClientCertificateResponse, self).to_map()
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
            temp_model = DescribeClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientCertificateStatusRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientCertificateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeClientCertificateStatusResponseBodyCertificateStatus(TeaModel):
    def __init__(self, revoke_time=None, serial_number=None, status=None):
        self.revoke_time = revoke_time  # type: long
        self.serial_number = serial_number  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientCertificateStatusResponseBodyCertificateStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.revoke_time is not None:
            result['RevokeTime'] = self.revoke_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RevokeTime') is not None:
            self.revoke_time = m.get('RevokeTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClientCertificateStatusResponseBody(TeaModel):
    def __init__(self, certificate_status=None, request_id=None):
        self.certificate_status = certificate_status  # type: list[DescribeClientCertificateStatusResponseBodyCertificateStatus]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_status:
            for k in self.certificate_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClientCertificateStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateStatus'] = []
        if self.certificate_status is not None:
            for k in self.certificate_status:
                result['CertificateStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_status = []
        if m.get('CertificateStatus') is not None:
            for k in m.get('CertificateStatus'):
                temp_model = DescribeClientCertificateStatusResponseBodyCertificateStatus()
                self.certificate_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClientCertificateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClientCertificateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClientCertificateStatusResponse, self).to_map()
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
            temp_model = DescribeClientCertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCAInstanceStatusRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCAInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCAInstanceStatusResponseBodyInstanceStatusList(TeaModel):
    def __init__(self, after_time=None, before_time=None, cert_issued_count=None, cert_total_count=None,
                 identifier=None, instance_id=None, status=None, type=None, use_expire_time=None):
        self.after_time = after_time  # type: long
        self.before_time = before_time  # type: long
        self.cert_issued_count = cert_issued_count  # type: int
        self.cert_total_count = cert_total_count  # type: int
        self.identifier = identifier  # type: str
        self.instance_id = instance_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.use_expire_time = use_expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCAInstanceStatusResponseBodyInstanceStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.cert_issued_count is not None:
            result['CertIssuedCount'] = self.cert_issued_count
        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.use_expire_time is not None:
            result['UseExpireTime'] = self.use_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CertIssuedCount') is not None:
            self.cert_issued_count = m.get('CertIssuedCount')
        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseExpireTime') is not None:
            self.use_expire_time = m.get('UseExpireTime')
        return self


class GetCAInstanceStatusResponseBody(TeaModel):
    def __init__(self, instance_status_list=None, request_id=None):
        self.instance_status_list = instance_status_list  # type: list[GetCAInstanceStatusResponseBodyInstanceStatusList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_status_list:
            for k in self.instance_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCAInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k in self.instance_status_list:
                result['InstanceStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k in m.get('InstanceStatusList'):
                temp_model = GetCAInstanceStatusResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCAInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCAInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCAInstanceStatusResponse, self).to_map()
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
            temp_model = GetCAInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientCertificateRequest(TeaModel):
    def __init__(self, current_page=None, show_size=None):
        self.current_page = current_page  # type: int
        self.show_size = show_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClientCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListClientCertificateResponseBodyCertificateList(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, certificate_type=None, common_name=None,
                 country_code=None, days=None, identifier=None, key_size=None, locality=None, md_5=None, organization=None,
                 organization_unit=None, parent_identifier=None, sans=None, serial_number=None, sha_2=None, sign_algorithm=None,
                 state=None, status=None, subject_dn=None, x_509certificate=None):
        self.after_date = after_date  # type: long
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: long
        self.certificate_type = certificate_type  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.days = days  # type: int
        self.identifier = identifier  # type: str
        self.key_size = key_size  # type: int
        self.locality = locality  # type: str
        self.md_5 = md_5  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.sans = sans  # type: str
        self.serial_number = serial_number  # type: str
        self.sha_2 = sha_2  # type: str
        self.sign_algorithm = sign_algorithm  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.subject_dn = subject_dn  # type: str
        self.x_509certificate = x_509certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClientCertificateResponseBodyCertificateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.days is not None:
            result['Days'] = self.days
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class ListClientCertificateResponseBody(TeaModel):
    def __init__(self, certificate_list=None, current_page=None, page_count=None, request_id=None, show_size=None,
                 total_count=None):
        self.certificate_list = certificate_list  # type: list[ListClientCertificateResponseBodyCertificateList]
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClientCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = ListClientCertificateResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClientCertificateResponse, self).to_map()
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
            temp_model = ListClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRevokeCertificateRequest(TeaModel):
    def __init__(self, current_page=None, show_size=None):
        self.current_page = current_page  # type: int
        self.show_size = show_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRevokeCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListRevokeCertificateResponseBodyCertificateList(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, certificate_type=None, common_name=None,
                 country_code=None, identifier=None, key_size=None, locality=None, md_5=None, organization=None,
                 organization_unit=None, parent_identifier=None, revoke_date=None, sans=None, serial_number=None, sha_2=None,
                 sign_algorithm=None, state=None, status=None, subject_dn=None):
        self.after_date = after_date  # type: str
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: str
        self.certificate_type = certificate_type  # type: str
        self.common_name = common_name  # type: str
        self.country_code = country_code  # type: str
        self.identifier = identifier  # type: str
        self.key_size = key_size  # type: int
        self.locality = locality  # type: str
        self.md_5 = md_5  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.revoke_date = revoke_date  # type: str
        self.sans = sans  # type: str
        self.serial_number = serial_number  # type: str
        self.sha_2 = sha_2  # type: str
        self.sign_algorithm = sign_algorithm  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.subject_dn = subject_dn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRevokeCertificateResponseBodyCertificateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.revoke_date is not None:
            result['RevokeDate'] = self.revoke_date
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('RevokeDate') is not None:
            self.revoke_date = m.get('RevokeDate')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        return self


class ListRevokeCertificateResponseBody(TeaModel):
    def __init__(self, certificate_list=None, current_page=None, page_count=None, request_id=None, show_size=None,
                 total_count=None):
        self.certificate_list = certificate_list  # type: list[ListRevokeCertificateResponseBodyCertificateList]
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRevokeCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = ListRevokeCertificateResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRevokeCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRevokeCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRevokeCertificateResponse, self).to_map()
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
            temp_model = ListRevokeCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCACertificateStatusRequest(TeaModel):
    def __init__(self, identifier=None, status=None):
        self.identifier = identifier  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCACertificateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCACertificateStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCACertificateStatusResponseBody, self).to_map()
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


class UpdateCACertificateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCACertificateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCACertificateStatusResponse, self).to_map()
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
            temp_model = UpdateCACertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


