# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelCertificateForPackageRequestRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCertificateForPackageRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelCertificateForPackageRequestResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCertificateForPackageRequestResponseBody, self).to_map()
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


class CancelCertificateForPackageRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelCertificateForPackageRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelCertificateForPackageRequestResponse, self).to_map()
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
            temp_model = CancelCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequestRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelOrderRequestResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderRequestResponseBody, self).to_map()
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


class CancelOrderRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelOrderRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelOrderRequestResponse, self).to_map()
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
            temp_model = CancelOrderRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateForPackageRequestRequest(TeaModel):
    def __init__(self, company_name=None, csr=None, domain=None, email=None, phone=None, product_code=None,
                 username=None, validate_type=None):
        self.company_name = company_name  # type: str
        self.csr = csr  # type: str
        self.domain = domain  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.product_code = product_code  # type: str
        self.username = username  # type: str
        self.validate_type = validate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateForPackageRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateForPackageRequestResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateForPackageRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateForPackageRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCertificateForPackageRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateForPackageRequestResponse, self).to_map()
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
            temp_model = CreateCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequestRequest(TeaModel):
    def __init__(self, domain=None, email=None, phone=None, product_code=None, username=None, validate_type=None):
        self.domain = domain  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.product_code = product_code  # type: str
        self.username = username  # type: str
        self.validate_type = validate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateRequestResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCertificateRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateRequestResponse, self).to_map()
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
            temp_model = CreateCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateWithCsrRequestRequest(TeaModel):
    def __init__(self, csr=None, email=None, phone=None, product_code=None, username=None, validate_type=None):
        self.csr = csr  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.product_code = product_code  # type: str
        self.username = username  # type: str
        self.validate_type = validate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateWithCsrRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateWithCsrRequestResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateWithCsrRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateWithCsrRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCertificateWithCsrRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateWithCsrRequestResponse, self).to_map()
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
            temp_model = CreateCertificateWithCsrRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWHClientCertificateRequest(TeaModel):
    def __init__(self, after_time=None, algorithm=None, before_time=None, common_name=None, country=None, csr=None,
                 days=None, immediately=None, locality=None, months=None, organization=None, organization_unit=None,
                 parent_identifier=None, san_type=None, san_value=None, state=None, years=None):
        self.after_time = after_time  # type: long
        self.algorithm = algorithm  # type: str
        self.before_time = before_time  # type: long
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.csr = csr  # type: str
        self.days = days  # type: long
        self.immediately = immediately  # type: long
        self.locality = locality  # type: str
        self.months = months  # type: long
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.san_type = san_type  # type: long
        self.san_value = san_value  # type: str
        self.state = state  # type: str
        self.years = years  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWHClientCertificateRequest, self).to_map()
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


class CreateWHClientCertificateResponseBody(TeaModel):
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
        _map = super(CreateWHClientCertificateResponseBody, self).to_map()
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


class CreateWHClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWHClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWHClientCertificateResponse, self).to_map()
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
            temp_model = CreateWHClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptRequest(TeaModel):
    def __init__(self, algorithm=None, cert_identifier=None, ciphertext_blob=None, message_type=None):
        self.algorithm = algorithm  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.ciphertext_blob = ciphertext_blob  # type: str
        self.message_type = message_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class DecryptResponseBody(TeaModel):
    def __init__(self, cert_identifier=None, plaintext=None, request_id=None):
        self.cert_identifier = cert_identifier  # type: str
        self.plaintext = plaintext  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DecryptResponse, self).to_map()
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
            temp_model = DecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequestRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertificateRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteCertificateRequestResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertificateRequestResponseBody, self).to_map()
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


class DeleteCertificateRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCertificateRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCertificateRequestResponse, self).to_map()
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
            temp_model = DeleteCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePCACertRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePCACertRequest, self).to_map()
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


class DeletePCACertResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePCACertResponseBody, self).to_map()
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


class DeletePCACertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePCACertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePCACertResponse, self).to_map()
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
            temp_model = DeletePCACertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserCertificateRequest(TeaModel):
    def __init__(self, cert_id=None):
        self.cert_id = cert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class DeleteUserCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserCertificateResponseBody, self).to_map()
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


class DeleteUserCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserCertificateResponse, self).to_map()
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
            temp_model = DeleteUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateStateRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribeCertificateStateResponseBody(TeaModel):
    def __init__(self, certificate=None, content=None, domain=None, private_key=None, record_domain=None,
                 record_type=None, record_value=None, request_id=None, type=None, uri=None, validate_type=None):
        self.certificate = certificate  # type: str
        self.content = content  # type: str
        self.domain = domain  # type: str
        self.private_key = private_key  # type: str
        self.record_domain = record_domain  # type: str
        self.record_type = record_type  # type: str
        self.record_value = record_value  # type: str
        self.request_id = request_id  # type: str
        self.type = type  # type: str
        self.uri = uri  # type: str
        self.validate_type = validate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.content is not None:
            result['Content'] = self.content
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.record_domain is not None:
            result['RecordDomain'] = self.record_domain
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.record_value is not None:
            result['RecordValue'] = self.record_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RecordDomain') is not None:
            self.record_domain = m.get('RecordDomain')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class DescribeCertificateStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCertificateStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertificateStateResponse, self).to_map()
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
            temp_model = DescribeCertificateStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageStateRequest(TeaModel):
    def __init__(self, product_code=None):
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackageStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribePackageStateResponseBody(TeaModel):
    def __init__(self, issued_count=None, product_code=None, request_id=None, total_count=None, used_count=None):
        self.issued_count = issued_count  # type: long
        self.product_code = product_code  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.used_count = used_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackageStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issued_count is not None:
            result['IssuedCount'] = self.issued_count
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IssuedCount') is not None:
            self.issued_count = m.get('IssuedCount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribePackageStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePackageStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePackageStateResponse, self).to_map()
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
            temp_model = DescribePackageStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptRequest(TeaModel):
    def __init__(self, algorithm=None, cert_identifier=None, message_type=None, plaintext=None):
        self.algorithm = algorithm  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.message_type = message_type  # type: str
        self.plaintext = plaintext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptResponseBody(TeaModel):
    def __init__(self, cert_identifier=None, ciphertext_blob=None, request_id=None):
        self.cert_identifier = cert_identifier  # type: str
        self.ciphertext_blob = ciphertext_blob  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EncryptResponse, self).to_map()
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
            temp_model = EncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertWarehouseQuotaResponseBody(TeaModel):
    def __init__(self, request_id=None, total_quota=None, use_count=None):
        self.request_id = request_id  # type: str
        self.total_quota = total_quota  # type: long
        self.use_count = use_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCertWarehouseQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class GetCertWarehouseQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCertWarehouseQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCertWarehouseQuotaResponse, self).to_map()
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
            temp_model = GetCertWarehouseQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserCertificateDetailRequest(TeaModel):
    def __init__(self, cert_id=None):
        self.cert_id = cert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class GetUserCertificateDetailResponseBody(TeaModel):
    def __init__(self, buy_in_aliyun=None, cert=None, city=None, common=None, country=None, end_date=None,
                 expired=None, fingerprint=None, id=None, issuer=None, key=None, name=None, org_name=None, province=None,
                 request_id=None, sans=None, start_date=None):
        self.buy_in_aliyun = buy_in_aliyun  # type: bool
        self.cert = cert  # type: str
        self.city = city  # type: str
        self.common = common  # type: str
        self.country = country  # type: str
        self.end_date = end_date  # type: str
        self.expired = expired  # type: bool
        self.fingerprint = fingerprint  # type: str
        self.id = id  # type: long
        self.issuer = issuer  # type: str
        self.key = key  # type: str
        self.name = name  # type: str
        self.org_name = org_name  # type: str
        self.province = province  # type: str
        self.request_id = request_id  # type: str
        self.sans = sans  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_in_aliyun is not None:
            result['BuyInAliyun'] = self.buy_in_aliyun
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.city is not None:
            result['City'] = self.city
        if self.common is not None:
            result['Common'] = self.common
        if self.country is not None:
            result['Country'] = self.country
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.province is not None:
            result['Province'] = self.province
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyInAliyun') is not None:
            self.buy_in_aliyun = m.get('BuyInAliyun')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetUserCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserCertificateDetailResponse, self).to_map()
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
            temp_model = GetUserCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertRequest(TeaModel):
    def __init__(self, current_page=None, key_word=None, show_size=None, source_type=None, status=None,
                 warehouse_id=None):
        self.current_page = current_page  # type: long
        self.key_word = key_word  # type: str
        self.show_size = show_size  # type: long
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.warehouse_id = warehouse_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')
        return self


class ListCertResponseBodyCertList(TeaModel):
    def __init__(self, after_date=None, before_date=None, common_name=None, exist_private_key=None, identifier=None,
                 issuer=None, sans=None, source_type=None, status=None, wh_id=None, wh_instance_id=None):
        self.after_date = after_date  # type: long
        self.before_date = before_date  # type: long
        self.common_name = common_name  # type: str
        self.exist_private_key = exist_private_key  # type: bool
        self.identifier = identifier  # type: str
        self.issuer = issuer  # type: str
        self.sans = sans  # type: str
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.wh_id = wh_id  # type: long
        self.wh_instance_id = wh_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCertResponseBodyCertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.exist_private_key is not None:
            result['ExistPrivateKey'] = self.exist_private_key
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.wh_id is not None:
            result['WhId'] = self.wh_id
        if self.wh_instance_id is not None:
            result['WhInstanceId'] = self.wh_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('ExistPrivateKey') is not None:
            self.exist_private_key = m.get('ExistPrivateKey')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')
        if m.get('WhInstanceId') is not None:
            self.wh_instance_id = m.get('WhInstanceId')
        return self


class ListCertResponseBody(TeaModel):
    def __init__(self, cert_list=None, current_page=None, request_id=None, show_size=None, total_count=None):
        self.cert_list = cert_list  # type: list[ListCertResponseBodyCertList]
        self.current_page = current_page  # type: long
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = ListCertResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCertResponse, self).to_map()
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
            temp_model = ListCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertWarehouseRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, name=None, show_size=None, type=None):
        self.current_page = current_page  # type: long
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.show_size = show_size  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCertWarehouseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCertWarehouseResponseBodyCertWarehouseList(TeaModel):
    def __init__(self, end_time=None, instance_id=None, is_expired=None, name=None, pca_instance_id=None, qps=None,
                 type=None, wh_id=None):
        self.end_time = end_time  # type: long
        self.instance_id = instance_id  # type: str
        self.is_expired = is_expired  # type: bool
        self.name = name  # type: str
        self.pca_instance_id = pca_instance_id  # type: str
        self.qps = qps  # type: long
        self.type = type  # type: str
        self.wh_id = wh_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCertWarehouseResponseBodyCertWarehouseList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.name is not None:
            result['Name'] = self.name
        if self.pca_instance_id is not None:
            result['PcaInstanceId'] = self.pca_instance_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.type is not None:
            result['Type'] = self.type
        if self.wh_id is not None:
            result['WhId'] = self.wh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PcaInstanceId') is not None:
            self.pca_instance_id = m.get('PcaInstanceId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')
        return self


class ListCertWarehouseResponseBody(TeaModel):
    def __init__(self, cert_warehouse_list=None, current_page=None, request_id=None, show_size=None,
                 total_count=None):
        self.cert_warehouse_list = cert_warehouse_list  # type: list[ListCertWarehouseResponseBodyCertWarehouseList]
        self.current_page = current_page  # type: long
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        if self.cert_warehouse_list:
            for k in self.cert_warehouse_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCertWarehouseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertWarehouseList'] = []
        if self.cert_warehouse_list is not None:
            for k in self.cert_warehouse_list:
                result['CertWarehouseList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_warehouse_list = []
        if m.get('CertWarehouseList') is not None:
            for k in m.get('CertWarehouseList'):
                temp_model = ListCertWarehouseResponseBodyCertWarehouseList()
                self.cert_warehouse_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCertWarehouseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCertWarehouseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCertWarehouseResponse, self).to_map()
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
            temp_model = ListCertWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCertificateOrderRequest(TeaModel):
    def __init__(self, current_page=None, keyword=None, order_type=None, show_size=None, status=None):
        self.current_page = current_page  # type: long
        self.keyword = keyword  # type: str
        self.order_type = order_type  # type: str
        self.show_size = show_size  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserCertificateOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUserCertificateOrderResponseBodyCertificateOrderList(TeaModel):
    def __init__(self, algorithm=None, aliyun_order_id=None, buy_date=None, cert_end_time=None,
                 cert_start_time=None, cert_type=None, certificate_id=None, city=None, common_name=None, country=None, domain=None,
                 domain_count=None, domain_type=None, end_date=None, expired=None, fingerprint=None, instance_id=None,
                 issuer=None, name=None, order_id=None, org_name=None, partner_order_id=None, product_code=None,
                 product_name=None, province=None, root_brand=None, sans=None, serial_no=None, sha_2=None, source_type=None,
                 start_date=None, status=None, trustee_status=None, upload=None, wild_domain_count=None):
        self.algorithm = algorithm  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: long
        self.buy_date = buy_date  # type: long
        self.cert_end_time = cert_end_time  # type: long
        self.cert_start_time = cert_start_time  # type: long
        self.cert_type = cert_type  # type: str
        self.certificate_id = certificate_id  # type: long
        self.city = city  # type: str
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.domain = domain  # type: str
        self.domain_count = domain_count  # type: long
        self.domain_type = domain_type  # type: str
        self.end_date = end_date  # type: str
        self.expired = expired  # type: bool
        self.fingerprint = fingerprint  # type: str
        self.instance_id = instance_id  # type: str
        self.issuer = issuer  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: long
        self.org_name = org_name  # type: str
        self.partner_order_id = partner_order_id  # type: str
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.province = province  # type: str
        self.root_brand = root_brand  # type: str
        self.sans = sans  # type: str
        self.serial_no = serial_no  # type: str
        self.sha_2 = sha_2  # type: str
        self.source_type = source_type  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: str
        self.trustee_status = trustee_status  # type: str
        self.upload = upload  # type: bool
        self.wild_domain_count = wild_domain_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserCertificateOrderResponseBodyCertificateOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.buy_date is not None:
            result['BuyDate'] = self.buy_date
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.city is not None:
            result['City'] = self.city
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.partner_order_id is not None:
            result['PartnerOrderId'] = self.partner_order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.province is not None:
            result['Province'] = self.province
        if self.root_brand is not None:
            result['RootBrand'] = self.root_brand
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.trustee_status is not None:
            result['TrusteeStatus'] = self.trustee_status
        if self.upload is not None:
            result['Upload'] = self.upload
        if self.wild_domain_count is not None:
            result['WildDomainCount'] = self.wild_domain_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('BuyDate') is not None:
            self.buy_date = m.get('BuyDate')
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('PartnerOrderId') is not None:
            self.partner_order_id = m.get('PartnerOrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RootBrand') is not None:
            self.root_brand = m.get('RootBrand')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrusteeStatus') is not None:
            self.trustee_status = m.get('TrusteeStatus')
        if m.get('Upload') is not None:
            self.upload = m.get('Upload')
        if m.get('WildDomainCount') is not None:
            self.wild_domain_count = m.get('WildDomainCount')
        return self


class ListUserCertificateOrderResponseBody(TeaModel):
    def __init__(self, certificate_order_list=None, current_page=None, request_id=None, show_size=None,
                 total_count=None):
        self.certificate_order_list = certificate_order_list  # type: list[ListUserCertificateOrderResponseBodyCertificateOrderList]
        self.current_page = current_page  # type: long
        self.request_id = request_id  # type: str
        self.show_size = show_size  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        if self.certificate_order_list:
            for k in self.certificate_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserCertificateOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateOrderList'] = []
        if self.certificate_order_list is not None:
            for k in self.certificate_order_list:
                result['CertificateOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_order_list = []
        if m.get('CertificateOrderList') is not None:
            for k in m.get('CertificateOrderList'):
                temp_model = ListUserCertificateOrderResponseBodyCertificateOrderList()
                self.certificate_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserCertificateOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserCertificateOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserCertificateOrderResponse, self).to_map()
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
            temp_model = ListUserCertificateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewCertificateOrderForPackageRequestRequest(TeaModel):
    def __init__(self, csr=None, order_id=None):
        self.csr = csr  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewCertificateOrderForPackageRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewCertificateOrderForPackageRequestResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewCertificateOrderForPackageRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewCertificateOrderForPackageRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewCertificateOrderForPackageRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewCertificateOrderForPackageRequestResponse, self).to_map()
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
            temp_model = RenewCertificateOrderForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeWHClientCertificateRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeWHClientCertificateRequest, self).to_map()
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


class RevokeWHClientCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeWHClientCertificateResponseBody, self).to_map()
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


class RevokeWHClientCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeWHClientCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeWHClientCertificateResponse, self).to_map()
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
            temp_model = RevokeWHClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignRequest(TeaModel):
    def __init__(self, cert_identifier=None, message=None, message_type=None, signing_algorithm=None):
        self.cert_identifier = cert_identifier  # type: str
        self.message = message  # type: str
        self.message_type = message_type  # type: str
        self.signing_algorithm = signing_algorithm  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class SignResponseBody(TeaModel):
    def __init__(self, request_id=None, signature=None):
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class SignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SignResponse, self).to_map()
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
            temp_model = SignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadPCACertRequest(TeaModel):
    def __init__(self, cert=None, name=None, private_key=None, warehouse_id=None):
        self.cert = cert  # type: str
        self.name = name  # type: str
        self.private_key = private_key  # type: str
        self.warehouse_id = warehouse_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadPCACertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.name is not None:
            result['Name'] = self.name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')
        return self


class UploadPCACertResponseBody(TeaModel):
    def __init__(self, identifier=None, request_id=None):
        self.identifier = identifier  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadPCACertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadPCACertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadPCACertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadPCACertResponse, self).to_map()
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
            temp_model = UploadPCACertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadUserCertificateRequest(TeaModel):
    def __init__(self, cert=None, encrypt_cert=None, encrypt_private_key=None, key=None, name=None, sign_cert=None,
                 sign_private_key=None):
        self.cert = cert  # type: str
        self.encrypt_cert = encrypt_cert  # type: str
        self.encrypt_private_key = encrypt_private_key  # type: str
        self.key = key  # type: str
        self.name = name  # type: str
        self.sign_cert = sign_cert  # type: str
        self.sign_private_key = sign_private_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadUserCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.encrypt_cert is not None:
            result['EncryptCert'] = self.encrypt_cert
        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert
        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('EncryptCert') is not None:
            self.encrypt_cert = m.get('EncryptCert')
        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')
        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')
        return self


class UploadUserCertificateResponseBody(TeaModel):
    def __init__(self, cert_id=None, request_id=None):
        self.cert_id = cert_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadUserCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadUserCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadUserCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadUserCertificateResponse, self).to_map()
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
            temp_model = UploadUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRequest(TeaModel):
    def __init__(self, cert_identifier=None, message=None, message_type=None, signature_value=None,
                 signing_algorithm=None):
        self.cert_identifier = cert_identifier  # type: str
        self.message = message  # type: str
        self.message_type = message_type  # type: str
        self.signature_value = signature_value  # type: str
        self.signing_algorithm = signing_algorithm  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class VerifyResponseBody(TeaModel):
    def __init__(self, request_id=None, signature_valid=None):
        self.request_id = request_id  # type: str
        self.signature_valid = signature_valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class VerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyResponse, self).to_map()
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
            temp_model = VerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


