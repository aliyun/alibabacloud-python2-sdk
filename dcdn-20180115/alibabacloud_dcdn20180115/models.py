# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDcdnDomainRequest(TeaModel):
    def __init__(self, check_url=None, domain_name=None, owner_account=None, owner_id=None, resource_group_id=None,
                 scope=None, security_token=None, sources=None, top_level_domain=None):
        self.check_url = check_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnDomainResponseBody, self).to_map()
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


class AddDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDcdnDomainResponse, self).to_map()
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
            temp_model = AddDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDcdnIpaDomainRequest(TeaModel):
    def __init__(self, check_url=None, domain_name=None, owner_account=None, owner_id=None, protocol=None,
                 resource_group_id=None, scope=None, security_token=None, sources=None, top_level_domain=None):
        self.check_url = check_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.protocol = protocol  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddDcdnIpaDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnIpaDomainResponseBody, self).to_map()
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


class AddDcdnIpaDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDcdnIpaDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDcdnIpaDomainResponse, self).to_map()
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
            temp_model = AddDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddDcdnDomainRequest(TeaModel):
    def __init__(self, check_url=None, domain_name=None, owner_account=None, owner_id=None, resource_group_id=None,
                 scope=None, security_token=None, sources=None, top_level_domain=None):
        self.check_url = check_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class BatchAddDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddDcdnDomainResponseBody, self).to_map()
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


class BatchAddDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchAddDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddDcdnDomainResponse, self).to_map()
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
            temp_model = BatchAddDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteDcdnDomainConfigsRequest(TeaModel):
    def __init__(self, domain_names=None, function_names=None, owner_account=None, owner_id=None,
                 security_token=None):
        self.domain_names = domain_names  # type: str
        self.function_names = function_names  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchDeleteDcdnDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDcdnDomainConfigsResponseBody, self).to_map()
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


class BatchDeleteDcdnDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDeleteDcdnDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteDcdnDomainConfigsResponse, self).to_map()
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
            temp_model = BatchDeleteDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnDomainCertificateRequest(TeaModel):
    def __init__(self, cert_name=None, cert_type=None, domain_name=None, owner_id=None, region=None, sslpri=None,
                 sslprotocol=None, sslpub=None, security_token=None):
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.sslpri = sslpri  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetDcdnDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainCertificateResponseBody, self).to_map()
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


class BatchSetDcdnDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetDcdnDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetDcdnDomainCertificateResponse, self).to_map()
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
            temp_model = BatchSetDcdnDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnDomainConfigsRequest(TeaModel):
    def __init__(self, domain_names=None, functions=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetDcdnDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainConfigsResponseBody, self).to_map()
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


class BatchSetDcdnDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetDcdnDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetDcdnDomainConfigsResponse, self).to_map()
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
            temp_model = BatchSetDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnIpaDomainConfigsRequest(TeaModel):
    def __init__(self, domain_names=None, functions=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnIpaDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetDcdnIpaDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnIpaDomainConfigsResponseBody, self).to_map()
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


class BatchSetDcdnIpaDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetDcdnIpaDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetDcdnIpaDomainConfigsResponse, self).to_map()
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
            temp_model = BatchSetDcdnIpaDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartDcdnDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStartDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDcdnDomainResponseBody, self).to_map()
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


class BatchStartDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStartDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartDcdnDomainResponse, self).to_map()
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
            temp_model = BatchStartDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopDcdnDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStopDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDcdnDomainResponseBody, self).to_map()
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


class BatchStopDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStopDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopDcdnDomainResponse, self).to_map()
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
            temp_model = BatchStopDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDcdnProjectExistRequest(TeaModel):
    def __init__(self, owner_id=None, project_name=None):
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDcdnProjectExistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CheckDcdnProjectExistResponseBodyContent(TeaModel):
    def __init__(self, exist=None):
        self.exist = exist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDcdnProjectExistResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        return self


class CheckDcdnProjectExistResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: CheckDcdnProjectExistResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CheckDcdnProjectExistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = CheckDcdnProjectExistResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDcdnProjectExistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckDcdnProjectExistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDcdnProjectExistResponse, self).to_map()
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
            temp_model = CheckDcdnProjectExistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitStagingRoutineCodeRequest(TeaModel):
    def __init__(self, code_description=None, name=None, owner_id=None):
        self.code_description = code_description  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitStagingRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CommitStagingRoutineCodeResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitStagingRoutineCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CommitStagingRoutineCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CommitStagingRoutineCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CommitStagingRoutineCodeResponse, self).to_map()
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
            temp_model = CommitStagingRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnCertificateSigningRequestRequest(TeaModel):
    def __init__(self, city=None, common_name=None, country=None, email=None, organization=None,
                 organization_unit=None, owner_id=None, sans=None, state=None):
        self.city = city  # type: str
        self.common_name = common_name  # type: str
        self.country = country  # type: str
        self.email = email  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.owner_id = owner_id  # type: long
        self.sans = sans  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnCertificateSigningRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.email is not None:
            result['Email'] = self.email
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sans is not None:
            result['SANs'] = self.sans
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SANs') is not None:
            self.sans = m.get('SANs')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class CreateDcdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(self, common_name=None, csr=None, pub_md_5=None, request_id=None):
        self.common_name = common_name  # type: str
        self.csr = csr  # type: str
        self.pub_md_5 = pub_md_5  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnCertificateSigningRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDcdnCertificateSigningRequestResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDcdnCertificateSigningRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDcdnCertificateSigningRequestResponse, self).to_map()
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
            temp_model = CreateDcdnCertificateSigningRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnDeliverTaskRequest(TeaModel):
    def __init__(self, deliver=None, domain_name=None, name=None, owner_id=None, reports=None, schedule=None):
        self.deliver = deliver  # type: str
        self.domain_name = domain_name  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.reports = reports  # type: str
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateDcdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDeliverTaskResponseBody, self).to_map()
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


class CreateDcdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDcdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDcdnDeliverTaskResponse, self).to_map()
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
            temp_model = CreateDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnSLSRealTimeLogDeliveryRequest(TeaModel):
    def __init__(self, business_type=None, data_center=None, domain_name=None, owner_id=None, project_name=None,
                 slslog_store=None, slsproject=None, slsregion=None, sampling_rate=None):
        self.business_type = business_type  # type: str
        self.data_center = data_center  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.slslog_store = slslog_store  # type: str
        self.slsproject = slsproject  # type: str
        self.slsregion = slsregion  # type: str
        self.sampling_rate = sampling_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnSLSRealTimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        return self


class CreateDcdnSLSRealTimeLogDeliveryResponseBodyContentDomains(TeaModel):
    def __init__(self, desc=None, domain_name=None, region=None, status=None):
        self.desc = desc  # type: str
        self.domain_name = domain_name  # type: str
        self.region = region  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnSLSRealTimeLogDeliveryResponseBodyContentDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDcdnSLSRealTimeLogDeliveryResponseBodyContent(TeaModel):
    def __init__(self, domains=None):
        self.domains = domains  # type: list[CreateDcdnSLSRealTimeLogDeliveryResponseBodyContentDomains]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDcdnSLSRealTimeLogDeliveryResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = CreateDcdnSLSRealTimeLogDeliveryResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class CreateDcdnSLSRealTimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: CreateDcdnSLSRealTimeLogDeliveryResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CreateDcdnSLSRealTimeLogDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = CreateDcdnSLSRealTimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDcdnSLSRealTimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDcdnSLSRealTimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDcdnSLSRealTimeLogDeliveryResponse, self).to_map()
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
            temp_model = CreateDcdnSLSRealTimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnSubTaskRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, report_ids=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.report_ids = report_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnSubTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        return self


class CreateDcdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnSubTaskResponseBody, self).to_map()
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


class CreateDcdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDcdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDcdnSubTaskResponse, self).to_map()
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
            temp_model = CreateDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoutineRequest(TeaModel):
    def __init__(self, description=None, env_conf=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.env_conf = env_conf  # type: dict[str, any]
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateRoutineShrinkRequest(TeaModel):
    def __init__(self, description=None, env_conf_shrink=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.env_conf_shrink = env_conf_shrink  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoutineShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateRoutineResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoutineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRoutineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRoutineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRoutineResponse, self).to_map()
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
            temp_model = CreateRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlrAndSlsProjectRequest(TeaModel):
    def __init__(self, owner_id=None, region=None):
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlrAndSlsProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateSlrAndSlsProjectResponseBodySlsInfo(TeaModel):
    def __init__(self, end_point=None, log_store=None, project=None, region=None):
        self.end_point = end_point  # type: str
        self.log_store = log_store  # type: str
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlrAndSlsProjectResponseBodySlsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateSlrAndSlsProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_info=None):
        self.request_id = request_id  # type: str
        self.sls_info = sls_info  # type: CreateSlrAndSlsProjectResponseBodySlsInfo

    def validate(self):
        if self.sls_info:
            self.sls_info.validate()

    def to_map(self):
        _map = super(CreateSlrAndSlsProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_info is not None:
            result['SlsInfo'] = self.sls_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsInfo') is not None:
            temp_model = CreateSlrAndSlsProjectResponseBodySlsInfo()
            self.sls_info = temp_model.from_map(m['SlsInfo'])
        return self


class CreateSlrAndSlsProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSlrAndSlsProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSlrAndSlsProjectResponse, self).to_map()
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
            temp_model = CreateSlrAndSlsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnDeliverTaskRequest(TeaModel):
    def __init__(self, deliver_id=None, owner_id=None):
        self.deliver_id = deliver_id  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteDcdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDeliverTaskResponseBody, self).to_map()
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


class DeleteDcdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnDeliverTaskResponse, self).to_map()
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
            temp_model = DeleteDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDomainResponseBody, self).to_map()
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


class DeleteDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnDomainResponse, self).to_map()
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
            temp_model = DeleteDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnIpaDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDcdnIpaDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaDomainResponseBody, self).to_map()
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


class DeleteDcdnIpaDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnIpaDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnIpaDomainResponse, self).to_map()
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
            temp_model = DeleteDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnIpaSpecificConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaSpecificConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDcdnIpaSpecificConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaSpecificConfigResponseBody, self).to_map()
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


class DeleteDcdnIpaSpecificConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnIpaSpecificConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnIpaSpecificConfigResponse, self).to_map()
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
            temp_model = DeleteDcdnIpaSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnRealTimeLogProjectRequest(TeaModel):
    def __init__(self, business_type=None, owner_id=None, project_name=None):
        self.business_type = business_type  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnRealTimeLogProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteDcdnRealTimeLogProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnRealTimeLogProjectResponseBody, self).to_map()
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


class DeleteDcdnRealTimeLogProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnRealTimeLogProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnRealTimeLogProjectResponse, self).to_map()
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
            temp_model = DeleteDcdnRealTimeLogProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSpecificConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDcdnSpecificConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificConfigResponseBody, self).to_map()
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


class DeleteDcdnSpecificConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnSpecificConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnSpecificConfigResponse, self).to_map()
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
            temp_model = DeleteDcdnSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSpecificStagingConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDcdnSpecificStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificStagingConfigResponseBody, self).to_map()
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


class DeleteDcdnSpecificStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnSpecificStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnSpecificStagingConfigResponse, self).to_map()
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
            temp_model = DeleteDcdnSpecificStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSubTaskRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSubTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteDcdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSubTaskResponseBody, self).to_map()
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


class DeleteDcdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDcdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDcdnSubTaskResponse, self).to_map()
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
            temp_model = DeleteDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineRequest(TeaModel):
    def __init__(self, name=None, owner_id=None):
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRoutineResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRoutineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRoutineResponse, self).to_map()
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
            temp_model = DeleteRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineCodeRevisionRequest(TeaModel):
    def __init__(self, name=None, owner_id=None, select_code_revision=None):
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class DeleteRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineCodeRevisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineCodeRevisionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRoutineCodeRevisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRoutineCodeRevisionResponse, self).to_map()
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
            temp_model = DeleteRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineConfEnvsRequest(TeaModel):
    def __init__(self, envs=None, name=None, owner_id=None):
        self.envs = envs  # type: dict[str, any]
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRoutineConfEnvsShrinkRequest(TeaModel):
    def __init__(self, envs_shrink=None, name=None, owner_id=None):
        self.envs_shrink = envs_shrink  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRoutineConfEnvsResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineConfEnvsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRoutineConfEnvsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsResponse, self).to_map()
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
            temp_model = DeleteRoutineConfEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnAclFieldsRequest(TeaModel):
    def __init__(self, lang=None, owner_id=None):
        self.lang = lang  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnAclFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnAclFieldsResponseBodyContent(TeaModel):
    def __init__(self, fields=None):
        self.fields = fields  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnAclFieldsResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        return self


class DescribeDcdnAclFieldsResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: list[DescribeDcdnAclFieldsResponseBodyContent]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnAclFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeDcdnAclFieldsResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnAclFieldsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnAclFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnAclFieldsResponse, self).to_map()
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
            temp_model = DescribeDcdnAclFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBgpBpsDataRequest(TeaModel):
    def __init__(self, end_time=None, interval=None, isp=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp = isp  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(self, in_=None, out=None, time_stamp=None):
        self.in_ = in_  # type: float
        self.out = out  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_ is not None:
            result['In'] = self.in_
        if self.out is not None:
            result['Out'] = self.out
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpBpsDataResponseBody(TeaModel):
    def __init__(self, bgp_data_interval=None, end_time=None, request_id=None, start_time=None):
        self.bgp_data_interval = bgp_data_interval  # type: list[DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval]
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bgp_data_interval:
            for k in self.bgp_data_interval:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnBgpBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnBgpBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnBgpBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBgpTrafficDataRequest(TeaModel):
    def __init__(self, end_time=None, interval=None, isp=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp = isp  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(self, in_=None, out=None, time_stamp=None):
        self.in_ = in_  # type: long
        self.out = out  # type: long
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_ is not None:
            result['In'] = self.in_
        if self.out is not None:
            result['Out'] = self.out
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpTrafficDataResponseBody(TeaModel):
    def __init__(self, bgp_data_interval=None, end_time=None, request_id=None, start_time=None):
        self.bgp_data_interval = bgp_data_interval  # type: list[DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval]
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bgp_data_interval:
            for k in self.bgp_data_interval:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnBgpTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnBgpTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnBgpTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBlockedRegionsRequest(TeaModel):
    def __init__(self, language=None, owner_id=None):
        self.language = language  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem(TeaModel):
    def __init__(self, continent=None, countries_and_regions=None, countries_and_regions_name=None):
        self.continent = continent  # type: str
        self.countries_and_regions = countries_and_regions  # type: str
        self.countries_and_regions_name = countries_and_regions_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continent is not None:
            result['Continent'] = self.continent
        if self.countries_and_regions is not None:
            result['CountriesAndRegions'] = self.countries_and_regions
        if self.countries_and_regions_name is not None:
            result['CountriesAndRegionsName'] = self.countries_and_regions_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')
        if m.get('CountriesAndRegions') is not None:
            self.countries_and_regions = m.get('CountriesAndRegions')
        if m.get('CountriesAndRegionsName') is not None:
            self.countries_and_regions_name = m.get('CountriesAndRegionsName')
        return self


class DescribeDcdnBlockedRegionsResponseBodyInfoList(TeaModel):
    def __init__(self, info_item=None):
        self.info_item = info_item  # type: list[DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem]

    def validate(self):
        if self.info_item:
            for k in self.info_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponseBodyInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InfoItem'] = []
        if self.info_item is not None:
            for k in self.info_item:
                result['InfoItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.info_item = []
        if m.get('InfoItem') is not None:
            for k in m.get('InfoItem'):
                temp_model = DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem()
                self.info_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnBlockedRegionsResponseBody(TeaModel):
    def __init__(self, info_list=None, request_id=None):
        self.info_list = info_list  # type: DescribeDcdnBlockedRegionsResponseBodyInfoList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_list is not None:
            result['InfoList'] = self.info_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InfoList') is not None:
            temp_model = DescribeDcdnBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m['InfoList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnBlockedRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnBlockedRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponse, self).to_map()
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
            temp_model = DescribeDcdnBlockedRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnCertificateDetailRequest(TeaModel):
    def __init__(self, cert_name=None, owner_id=None, security_token=None):
        self.cert_name = cert_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert=None, cert_id=None, cert_name=None, key=None, request_id=None):
        self.cert = cert  # type: str
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.key = key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateDetailResponse, self).to_map()
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
            temp_model = DescribeDcdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnCertificateListRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateListRequest, self).to_map()
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


class DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(self, cert_id=None, cert_name=None, common=None, fingerprint=None, issuer=None, last_time=None):
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.common = common  # type: str
        self.fingerprint = fingerprint  # type: str
        self.issuer = issuer  # type: str
        self.last_time = last_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert=None):
        self.cert = cert  # type: list[DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert]

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBodyCertificateListModelCertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k in m.get('Cert'):
                temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: DescribeDcdnCertificateListResponseBodyCertificateListModelCertList
        self.count = count  # type: int

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBodyCertificateListModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnCertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeDcdnCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponse, self).to_map()
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
            temp_model = DescribeDcdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnConfigGroupDetailRequest(TeaModel):
    def __init__(self, config_group_id=None, config_group_name=None, owner_id=None):
        self.config_group_id = config_group_id  # type: str
        self.config_group_name = config_group_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnConfigGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.config_group_name is not None:
            result['ConfigGroupName'] = self.config_group_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('ConfigGroupName') is not None:
            self.config_group_name = m.get('ConfigGroupName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnConfigGroupDetailResponseBody(TeaModel):
    def __init__(self, biz_name=None, config_group_id=None, config_group_name=None, create_time=None,
                 description=None, request_id=None, update_time=None):
        self.biz_name = biz_name  # type: str
        self.config_group_id = config_group_id  # type: str
        self.config_group_name = config_group_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnConfigGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.config_group_name is not None:
            result['ConfigGroupName'] = self.config_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('ConfigGroupName') is not None:
            self.config_group_name = m.get('ConfigGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDcdnConfigGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnConfigGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigGroupDetailResponse, self).to_map()
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
            temp_model = DescribeDcdnConfigGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnConfigOfVersionRequest(TeaModel):
    def __init__(self, function_id=None, function_name=None, group_id=None, owner_id=None, security_token=None,
                 version_id=None):
        self.function_id = function_id  # type: int
        self.function_name = function_name  # type: str
        self.group_id = group_id  # type: long
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigs(TeaModel):
    def __init__(self, version_config=None):
        self.version_config = version_config  # type: list[DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig]

    def validate(self):
        if self.version_config:
            for k in self.version_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBodyVersionConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VersionConfig'] = []
        if self.version_config is not None:
            for k in self.version_config:
                result['VersionConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.version_config = []
        if m.get('VersionConfig') is not None:
            for k in m.get('VersionConfig'):
                temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig()
                self.version_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnConfigOfVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, version_configs=None):
        self.request_id = request_id  # type: str
        self.version_configs = version_configs  # type: DescribeDcdnConfigOfVersionResponseBodyVersionConfigs

    def validate(self):
        if self.version_configs:
            self.version_configs.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_configs is not None:
            result['VersionConfigs'] = self.version_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionConfigs') is not None:
            temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigs()
            self.version_configs = temp_model.from_map(m['VersionConfigs'])
        return self


class DescribeDcdnConfigOfVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnConfigOfVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponse, self).to_map()
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
            temp_model = DescribeDcdnConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDeletedDomainsRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDeletedDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDcdnDeletedDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, domain_name=None, gmt_modified=None):
        self.domain_name = domain_name  # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDeletedDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeDcdnDeletedDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeDcdnDeletedDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDeletedDomainsResponseBodyDomains, self).to_map()
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
                temp_model = DescribeDcdnDeletedDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDeletedDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeDcdnDeletedDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnDeletedDomainsResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDeletedDomainsResponseBodyDomains()
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


class DescribeDcdnDeletedDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDeletedDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDeletedDomainsResponse, self).to_map()
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
            temp_model = DescribeDcdnDeletedDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDeliverListRequest(TeaModel):
    def __init__(self, deliver_id=None, owner_id=None):
        self.deliver_id = deliver_id  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDeliverListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnDeliverListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDeliverListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDeliverListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDeliverListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDeliverListResponse, self).to_map()
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
            temp_model = DescribeDcdnDeliverListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, bps=None, dynamic_http_bps=None, dynamic_https_bps=None, static_http_bps=None,
                 static_https_bps=None, time_stamp=None):
        self.bps = bps  # type: float
        self.dynamic_http_bps = dynamic_http_bps  # type: float
        self.dynamic_https_bps = dynamic_https_bps  # type: float
        self.static_http_bps = static_http_bps  # type: float
        self.static_https_bps = static_https_bps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.dynamic_http_bps is not None:
            result['DynamicHttpBps'] = self.dynamic_http_bps
        if self.dynamic_https_bps is not None:
            result['DynamicHttpsBps'] = self.dynamic_https_bps
        if self.static_http_bps is not None:
            result['StaticHttpBps'] = self.static_http_bps
        if self.static_https_bps is not None:
            result['StaticHttpsBps'] = self.static_https_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DynamicHttpBps') is not None:
            self.dynamic_http_bps = m.get('DynamicHttpBps')
        if m.get('DynamicHttpsBps') is not None:
            self.dynamic_https_bps = m.get('DynamicHttpsBps')
        if m.get('StaticHttpBps') is not None:
            self.static_http_bps = m.get('StaticHttpBps')
        if m.get('StaticHttpsBps') is not None:
            self.static_https_bps = m.get('StaticHttpsBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainBpsDataResponseBody(TeaModel):
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponseBody, self).to_map()
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
        return self


class DescribeDcdnDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainByCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, sslpub=None):
        self.owner_id = owner_id  # type: long
        self.sslpub = sslpub  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        return self


class DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_ca_is_legacy=None, cert_expire_time=None, cert_expired=None, cert_start_time=None,
                 cert_subject_common_name=None, cert_type=None, domain_list=None, domain_names=None, issuer=None):
        self.cert_ca_is_legacy = cert_ca_is_legacy  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_expired = cert_expired  # type: str
        self.cert_start_time = cert_start_time  # type: str
        self.cert_subject_common_name = cert_subject_common_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_list = domain_list  # type: str
        self.domain_names = domain_names  # type: str
        self.issuer = issuer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ca_is_legacy is not None:
            result['CertCaIsLegacy'] = self.cert_ca_is_legacy
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_expired is not None:
            result['CertExpired'] = self.cert_expired
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_subject_common_name is not None:
            result['CertSubjectCommonName'] = self.cert_subject_common_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCaIsLegacy') is not None:
            self.cert_ca_is_legacy = m.get('CertCaIsLegacy')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertExpired') is not None:
            self.cert_expired = m.get('CertExpired')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertSubjectCommonName') is not None:
            self.cert_subject_common_name = m.get('CertSubjectCommonName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class DescribeDcdnDomainByCertificateResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponseBodyCertInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainByCertificateResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeDcdnDomainByCertificateResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainByCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainByCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainByCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainCcActivityLogRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, page_number=None, page_size=None,
                 rule_name=None, start_time=None, trigger_object=None, value=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.rule_name = rule_name  # type: str
        self.start_time = start_time  # type: str
        self.trigger_object = trigger_object  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCcActivityLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnDomainCcActivityLogResponseBodyActivityLog(TeaModel):
    def __init__(self, action=None, domain_name=None, rule_name=None, time_stamp=None, trigger_object=None, ttl=None,
                 value=None):
        self.action = action  # type: str
        self.domain_name = domain_name  # type: str
        self.rule_name = rule_name  # type: str
        self.time_stamp = time_stamp  # type: str
        self.trigger_object = trigger_object  # type: str
        self.ttl = ttl  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCcActivityLogResponseBodyActivityLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnDomainCcActivityLogResponseBody(TeaModel):
    def __init__(self, activity_log=None, page_index=None, page_size=None, request_id=None, total=None):
        self.activity_log = activity_log  # type: list[DescribeDcdnDomainCcActivityLogResponseBodyActivityLog]
        self.page_index = page_index  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.activity_log:
            for k in self.activity_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCcActivityLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivityLog'] = []
        if self.activity_log is not None:
            for k in self.activity_log:
                result['ActivityLog'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.activity_log = []
        if m.get('ActivityLog') is not None:
            for k in m.get('ActivityLog'):
                temp_model = DescribeDcdnDomainCcActivityLogResponseBodyActivityLog()
                self.activity_log.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDcdnDomainCcActivityLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainCcActivityLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCcActivityLogResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainCcActivityLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainCertificateInfoRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_domain_name=None, cert_expire_time=None, cert_life=None, cert_name=None, cert_org=None,
                 cert_type=None, domain_name=None, sslprotocol=None, sslpub=None, status=None):
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponseBodyCertInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainCertificateInfoResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeDcdnDomainCertificateInfoResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainCertificateInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainCertificateInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainCnameRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnDomainCnameResponseBodyCnameDatasData(TeaModel):
    def __init__(self, cname=None, domain=None, status=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponseBodyCnameDatasData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnDomainCnameResponseBodyCnameDatas(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[DescribeDcdnDomainCnameResponseBodyCnameDatasData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponseBodyCnameDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDcdnDomainCnameResponseBodyCnameDatasData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainCnameResponseBody(TeaModel):
    def __init__(self, cname_datas=None, request_id=None):
        self.cname_datas = cname_datas  # type: DescribeDcdnDomainCnameResponseBodyCnameDatas
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_datas is not None:
            result['CnameDatas'] = self.cname_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnameDatas') is not None:
            temp_model = DescribeDcdnDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m['CnameDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainCnameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainCnameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainConfigsRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, function_names=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, domain_config=None):
        self.domain_config = domain_config  # type: list[DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig]

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainConfigsResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: DescribeDcdnDomainConfigsResponseBodyDomainConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainDetailRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailRequest, self).to_map()
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


class DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, content=None, enabled=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.enabled = enabled  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource, self).to_map()
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
        if self.weight is not None:
            result['Weight'] = self.weight
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
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBodyDomainDetailSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(self, cert_name=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, resource_group_id=None, sslprotocol=None, sslpub=None, scope=None,
                 sources=None):
        self.cert_name = cert_name  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.scope = scope  # type: str
        self.sources = sources  # type: DescribeDcdnDomainDetailResponseBodyDomainDetailSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBodyDomainDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
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
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
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
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnDomainDetailResponseBody(TeaModel):
    def __init__(self, domain_detail=None, request_id=None):
        self.domain_detail = domain_detail  # type: DescribeDcdnDomainDetailResponseBodyDomainDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataRequest, self).to_map()
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


class DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule(TeaModel):
    def __init__(self, byte_hit_rate=None, req_hit_rate=None, time_stamp=None):
        self.byte_hit_rate = byte_hit_rate  # type: float
        self.req_hit_rate = req_hit_rate  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHitRateDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, hit_rate_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.hit_rate_per_interval = hit_rate_per_interval  # type: DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.hit_rate_per_interval:
            self.hit_rate_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_rate_per_interval is not None:
            result['HitRatePerInterval'] = self.hit_rate_per_interval.to_map()
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
        if m.get('HitRatePerInterval') is not None:
            temp_model = DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval()
            self.hit_rate_per_interval = temp_model.from_map(m['HitRatePerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: int
        self.count = count  # type: float
        self.proportion = proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule, self).to_map()
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


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval(TeaModel):
    def __init__(self, http_code_data_module=None):
        self.http_code_data_module = http_code_data_module  # type: list[DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule]

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HttpCodeDataModule'] = []
        if self.http_code_data_module is not None:
            for k in self.http_code_data_module:
                result['HttpCodeDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.http_code_data_module = []
        if m.get('HttpCodeDataModule') is not None:
            for k in m.get('HttpCodeDataModule'):
                temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule(TeaModel):
    def __init__(self, http_code_data_per_interval=None, time_stamp=None):
        self.http_code_data_per_interval = http_code_data_per_interval  # type: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        if self.http_code_data_per_interval:
            self.http_code_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code_data_per_interval is not None:
            result['HttpCodeDataPerInterval'] = self.http_code_data_per_interval.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval()
            self.http_code_data_per_interval = temp_model.from_map(m['HttpCodeDataPerInterval'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, data_per_interval=None, domain_name=None, end_time=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.data_per_interval = data_per_interval  # type: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIpaBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, fix_time_gap=None, interval=None, isp_name_en=None,
                 location_name_en=None, owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataRequest, self).to_map()
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
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
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


class DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, ipa_bps=None, time_stamp=None):
        self.ipa_bps = ipa_bps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipa_bps is not None:
            result['IpaBps'] = self.ipa_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpaBps') is not None:
            self.ipa_bps = m.get('IpaBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIpaBpsDataResponseBody(TeaModel):
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataResponseBody, self).to_map()
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
        return self


class DescribeDcdnDomainIpaBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainIpaBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainIpaBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIpaTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, fix_time_gap=None, interval=None, isp_name_en=None,
                 location_name_en=None, owner_id=None, start_time=None, time_merge=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_merge = time_merge  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataRequest, self).to_map()
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
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
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


class DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, ipa_traffic=None, time_stamp=None):
        self.ipa_traffic = ipa_traffic  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipa_traffic is not None:
            result['IpaTraffic'] = self.ipa_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpaTraffic') is not None:
            self.ipa_traffic = m.get('IpaTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIpaTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataResponseBody, self).to_map()
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
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
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
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainIpaTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainIpaTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainIpaTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIspDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataRequest, self).to_map()
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


class DescribeDcdnDomainIspDataResponseBodyValueIspProportionData(TeaModel):
    def __init__(self, avg_object_size=None, avg_response_rate=None, avg_response_time=None, bps=None,
                 bytes_proportion=None, isp=None, isp_ename=None, proportion=None, qps=None, total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.isp = isp  # type: str
        self.isp_ename = isp_ename  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.total_bytes = total_bytes  # type: str
        self.total_query = total_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponseBodyValueIspProportionData, self).to_map()
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
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
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
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDcdnDomainIspDataResponseBodyValue(TeaModel):
    def __init__(self, isp_proportion_data=None):
        self.isp_proportion_data = isp_proportion_data  # type: list[DescribeDcdnDomainIspDataResponseBodyValueIspProportionData]

    def validate(self):
        if self.isp_proportion_data:
            for k in self.isp_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponseBodyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IspProportionData'] = []
        if self.isp_proportion_data is not None:
            for k in self.isp_proportion_data:
                result['IspProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.isp_proportion_data = []
        if m.get('IspProportionData') is not None:
            for k in m.get('IspProportionData'):
                temp_model = DescribeDcdnDomainIspDataResponseBodyValueIspProportionData()
                self.isp_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIspDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 value=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.value = value  # type: DescribeDcdnDomainIspDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainIspDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainIspDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainIspDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainIspDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainLogRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, page_number=None, page_size=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(self, end_time=None, log_name=None, log_path=None, log_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.log_name = log_name  # type: str
        self.log_path = log_path  # type: str
        self.log_size = log_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail, self).to_map()
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


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(self, log_info_detail=None):
        self.log_info_detail = log_info_detail  # type: list[DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail]

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfoDetail'] = []
        if self.log_info_detail is not None:
            for k in self.log_info_detail:
                result['LogInfoDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_info_detail = []
        if m.get('LogInfoDetail') is not None:
            for k in m.get('LogInfoDetail'):
                temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(self, page_index=None, page_size=None, total=None):
        self.page_index = page_index  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(self, log_count=None, log_infos=None, page_infos=None):
        self.log_count = log_count  # type: long
        self.log_infos = log_infos  # type: DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos
        self.page_infos = page_infos  # type: DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('PageInfos') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetails(TeaModel):
    def __init__(self, domain_log_detail=None):
        self.domain_log_detail = domain_log_detail  # type: list[DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail]

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetails, self).to_map()
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
                temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainLogResponseBody(TeaModel):
    def __init__(self, domain_log_details=None, domain_name=None, request_id=None):
        self.domain_log_details = domain_log_details  # type: DescribeDcdnDomainLogResponseBodyDomainLogDetails
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainMultiUsageDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataRequest, self).to_map()
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


class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(TeaModel):
    def __init__(self, domain=None, request=None, time_stamp=None, type=None):
        self.domain = domain  # type: str
        self.request = request  # type: long
        self.time_stamp = time_stamp  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.request is not None:
            result['Request'] = self.request
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval(TeaModel):
    def __init__(self, request_data_module=None):
        self.request_data_module = request_data_module  # type: list[DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule]

    def validate(self):
        if self.request_data_module:
            for k in self.request_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestDataModule'] = []
        if self.request_data_module is not None:
            for k in self.request_data_module:
                result['RequestDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_data_module = []
        if m.get('RequestDataModule') is not None:
            for k in m.get('RequestDataModule'):
                temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule()
                self.request_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule(TeaModel):
    def __init__(self, area=None, bps=None, domain=None, time_stamp=None, type=None):
        self.area = area  # type: str
        self.bps = bps  # type: float
        self.domain = domain  # type: str
        self.time_stamp = time_stamp  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval(TeaModel):
    def __init__(self, traffic_data_module=None):
        self.traffic_data_module = traffic_data_module  # type: list[DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule]

    def validate(self):
        if self.traffic_data_module:
            for k in self.traffic_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficDataModule'] = []
        if self.traffic_data_module is not None:
            for k in self.traffic_data_module:
                result['TrafficDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.traffic_data_module = []
        if m.get('TrafficDataModule') is not None:
            for k in m.get('TrafficDataModule'):
                temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule()
                self.traffic_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainMultiUsageDataResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, request_per_interval=None, start_time=None,
                 traffic_per_interval=None):
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.request_per_interval = request_per_interval  # type: DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval
        self.start_time = start_time  # type: str
        self.traffic_per_interval = traffic_per_interval  # type: DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval

    def validate(self):
        if self.request_per_interval:
            self.request_per_interval.validate()
        if self.traffic_per_interval:
            self.traffic_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_per_interval is not None:
            result['RequestPerInterval'] = self.request_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_per_interval is not None:
            result['TrafficPerInterval'] = self.traffic_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestPerInterval') is not None:
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m['RequestPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficPerInterval') is not None:
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval()
            self.traffic_per_interval = temp_model.from_map(m['TrafficPerInterval'])
        return self


class DescribeDcdnDomainMultiUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainMultiUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainOriginBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataRequest, self).to_map()
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


class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_http_origin_bps=None, dynamic_https_origin_bps=None, origin_bps=None,
                 static_http_origin_bps=None, static_https_origin_bps=None, time_stamp=None):
        self.dynamic_http_origin_bps = dynamic_http_origin_bps  # type: float
        self.dynamic_https_origin_bps = dynamic_https_origin_bps  # type: float
        self.origin_bps = origin_bps  # type: float
        self.static_http_origin_bps = static_http_origin_bps  # type: float
        self.static_https_origin_bps = static_https_origin_bps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_origin_bps is not None:
            result['DynamicHttpOriginBps'] = self.dynamic_http_origin_bps
        if self.dynamic_https_origin_bps is not None:
            result['DynamicHttpsOriginBps'] = self.dynamic_https_origin_bps
        if self.origin_bps is not None:
            result['OriginBps'] = self.origin_bps
        if self.static_http_origin_bps is not None:
            result['StaticHttpOriginBps'] = self.static_http_origin_bps
        if self.static_https_origin_bps is not None:
            result['StaticHttpsOriginBps'] = self.static_https_origin_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpOriginBps') is not None:
            self.dynamic_http_origin_bps = m.get('DynamicHttpOriginBps')
        if m.get('DynamicHttpsOriginBps') is not None:
            self.dynamic_https_origin_bps = m.get('DynamicHttpsOriginBps')
        if m.get('OriginBps') is not None:
            self.origin_bps = m.get('OriginBps')
        if m.get('StaticHttpOriginBps') is not None:
            self.static_http_origin_bps = m.get('StaticHttpOriginBps')
        if m.get('StaticHttpsOriginBps') is not None:
            self.static_https_origin_bps = m.get('StaticHttpsOriginBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainOriginBpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, origin_bps_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.origin_bps_data_per_interval = origin_bps_data_per_interval  # type: DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.origin_bps_data_per_interval:
            self.origin_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.origin_bps_data_per_interval is not None:
            result['OriginBpsDataPerInterval'] = self.origin_bps_data_per_interval.to_map()
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
        if m.get('OriginBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval()
            self.origin_bps_data_per_interval = temp_model.from_map(m['OriginBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainOriginBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainOriginBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainOriginBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainOriginTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataRequest, self).to_map()
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


class DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_http_origin_traffic=None, dynamic_https_origin_traffic=None, origin_traffic=None,
                 static_http_origin_traffic=None, static_https_origin_traffic=None, time_stamp=None):
        self.dynamic_http_origin_traffic = dynamic_http_origin_traffic  # type: float
        self.dynamic_https_origin_traffic = dynamic_https_origin_traffic  # type: float
        self.origin_traffic = origin_traffic  # type: float
        self.static_http_origin_traffic = static_http_origin_traffic  # type: float
        self.static_https_origin_traffic = static_https_origin_traffic  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_origin_traffic is not None:
            result['DynamicHttpOriginTraffic'] = self.dynamic_http_origin_traffic
        if self.dynamic_https_origin_traffic is not None:
            result['DynamicHttpsOriginTraffic'] = self.dynamic_https_origin_traffic
        if self.origin_traffic is not None:
            result['OriginTraffic'] = self.origin_traffic
        if self.static_http_origin_traffic is not None:
            result['StaticHttpOriginTraffic'] = self.static_http_origin_traffic
        if self.static_https_origin_traffic is not None:
            result['StaticHttpsOriginTraffic'] = self.static_https_origin_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpOriginTraffic') is not None:
            self.dynamic_http_origin_traffic = m.get('DynamicHttpOriginTraffic')
        if m.get('DynamicHttpsOriginTraffic') is not None:
            self.dynamic_https_origin_traffic = m.get('DynamicHttpsOriginTraffic')
        if m.get('OriginTraffic') is not None:
            self.origin_traffic = m.get('OriginTraffic')
        if m.get('StaticHttpOriginTraffic') is not None:
            self.static_http_origin_traffic = m.get('StaticHttpOriginTraffic')
        if m.get('StaticHttpsOriginTraffic') is not None:
            self.static_https_origin_traffic = m.get('StaticHttpsOriginTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, origin_traffic_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.origin_traffic_data_per_interval = origin_traffic_data_per_interval  # type: DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.origin_traffic_data_per_interval:
            self.origin_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.origin_traffic_data_per_interval is not None:
            result['OriginTrafficDataPerInterval'] = self.origin_traffic_data_per_interval.to_map()
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
        if m.get('OriginTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval()
            self.origin_traffic_data_per_interval = temp_model.from_map(m['OriginTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainOriginTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainOriginTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainOriginTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainPropertyRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnDomainPropertyResponseBody(TeaModel):
    def __init__(self, domain_name=None, protocol=None, request_id=None):
        self.domain_name = domain_name  # type: str
        self.protocol = protocol  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainPropertyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainPropertyResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainPvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataRequest, self).to_map()
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


class DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData, self).to_map()
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


class DescribeDcdnDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponseBodyPvDataInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainPvDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, pv_data_interval=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.pv_data_interval = pv_data_interval  # type: DescribeDcdnDomainPvDataResponseBodyPvDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
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
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeDcdnDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainPvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainPvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainQpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, acc=None, dynamic_http_acc=None, dynamic_http_qps=None, dynamic_https_acc=None,
                 dynamic_https_qps=None, qps=None, static_http_acc=None, static_http_qps=None, static_https_acc=None,
                 static_https_qps=None, time_stamp=None):
        self.acc = acc  # type: float
        self.dynamic_http_acc = dynamic_http_acc  # type: float
        self.dynamic_http_qps = dynamic_http_qps  # type: float
        self.dynamic_https_acc = dynamic_https_acc  # type: float
        self.dynamic_https_qps = dynamic_https_qps  # type: float
        self.qps = qps  # type: float
        self.static_http_acc = static_http_acc  # type: float
        self.static_http_qps = static_http_qps  # type: float
        self.static_https_acc = static_https_acc  # type: float
        self.static_https_qps = static_https_qps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.dynamic_http_acc is not None:
            result['DynamicHttpAcc'] = self.dynamic_http_acc
        if self.dynamic_http_qps is not None:
            result['DynamicHttpQps'] = self.dynamic_http_qps
        if self.dynamic_https_acc is not None:
            result['DynamicHttpsAcc'] = self.dynamic_https_acc
        if self.dynamic_https_qps is not None:
            result['DynamicHttpsQps'] = self.dynamic_https_qps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.static_http_acc is not None:
            result['StaticHttpAcc'] = self.static_http_acc
        if self.static_http_qps is not None:
            result['StaticHttpQps'] = self.static_http_qps
        if self.static_https_acc is not None:
            result['StaticHttpsAcc'] = self.static_https_acc
        if self.static_https_qps is not None:
            result['StaticHttpsQps'] = self.static_https_qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('DynamicHttpAcc') is not None:
            self.dynamic_http_acc = m.get('DynamicHttpAcc')
        if m.get('DynamicHttpQps') is not None:
            self.dynamic_http_qps = m.get('DynamicHttpQps')
        if m.get('DynamicHttpsAcc') is not None:
            self.dynamic_https_acc = m.get('DynamicHttpsAcc')
        if m.get('DynamicHttpsQps') is not None:
            self.dynamic_https_qps = m.get('DynamicHttpsQps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StaticHttpAcc') is not None:
            self.static_http_acc = m.get('StaticHttpAcc')
        if m.get('StaticHttpQps') is not None:
            self.static_http_qps = m.get('StaticHttpQps')
        if m.get('StaticHttpsAcc') is not None:
            self.static_https_acc = m.get('StaticHttpsAcc')
        if m.get('StaticHttpsQps') is not None:
            self.static_https_qps = m.get('StaticHttpsQps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainQpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, qps_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.qps_data_per_interval = qps_data_per_interval  # type: DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.qps_data_per_interval:
            self.qps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.qps_data_per_interval is not None:
            result['QpsDataPerInterval'] = self.qps_data_per_interval.to_map()
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
        if m.get('QpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval()
            self.qps_data_per_interval = temp_model.from_map(m['QpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainQpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, isp_name_en=None, location_name_en=None, owner_id=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
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
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
    def __init__(self, bps=None, time_stamp=None):
        self.bps = bps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(self, bps_model=None):
        self.bps_model = bps_model  # type: list[DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel]

    def validate(self):
        if self.bps_model:
            for k in self.bps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BpsModel'] = []
        if self.bps_model is not None:
            for k in self.bps_model:
                result['BpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bps_model = []
        if m.get('BpsModel') is not None:
            for k in m.get('BpsModel'):
                temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDcdnDomainRealTimeBpsDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataRequest, self).to_map()
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


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
    def __init__(self, byte_hit_rate=None, time_stamp=None):
        self.byte_hit_rate = byte_hit_rate  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(self, byte_hit_rate_data_model=None):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model  # type: list[DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel]

    def validate(self):
        if self.byte_hit_rate_data_model:
            for k in self.byte_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ByteHitRateDataModel'] = []
        if self.byte_hit_rate_data_model is not None:
            for k in self.byte_hit_rate_data_model:
                result['ByteHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.byte_hit_rate_data_model = []
        if m.get('ByteHitRateDataModel') is not None:
            for k in m.get('ByteHitRateDataModel'):
                temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeByteHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeDetailDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, field=None, isp_name_en=None, location_name_en=None,
                 merge=None, merge_loc_isp=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.merge = merge  # type: str
        self.merge_loc_isp = merge_loc_isp  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeDetailDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.merge is not None:
            result['Merge'] = self.merge
        if self.merge_loc_isp is not None:
            result['MergeLocIsp'] = self.merge_loc_isp
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
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('Merge') is not None:
            self.merge = m.get('Merge')
        if m.get('MergeLocIsp') is not None:
            self.merge_loc_isp = m.get('MergeLocIsp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeDetailDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeDetailDataResponseBody, self).to_map()
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


class DescribeDcdnDomainRealTimeDetailDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeDetailDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeDetailDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, isp_name_en=None, location_name_en=None, owner_id=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
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
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData, self).to_map()
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


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, real_time_code_proportion_data=None):
        self.real_time_code_proportion_data = real_time_code_proportion_data  # type: list[DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData]

    def validate(self):
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeCodeProportionData'] = []
        if self.real_time_code_proportion_data is not None:
            for k in self.real_time_code_proportion_data:
                result['RealTimeCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.real_time_code_proportion_data = []
        if m.get('RealTimeCodeProportionData') is not None:
            for k in m.get('RealTimeCodeProportionData'):
                temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData, self).to_map()
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
                temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, real_time_http_code_data=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_http_code_data = real_time_http_code_data  # type: DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
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
        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeQpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, isp_name_en=None, location_name_en=None, owner_id=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
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
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
    def __init__(self, qps=None, time_stamp=None):
        self.qps = qps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(self, qps_model=None):
        self.qps_model = qps_model  # type: list[DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel]

    def validate(self):
        if self.qps_model:
            for k in self.qps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QpsModel'] = []
        if self.qps_model is not None:
            for k in self.qps_model:
                result['QpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.qps_model = []
        if m.get('QpsModel') is not None:
            for k in m.get('QpsModel'):
                temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDcdnDomainRealTimeQpsDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataRequest, self).to_map()
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


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
    def __init__(self, req_hit_rate=None, time_stamp=None):
        self.req_hit_rate = req_hit_rate  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(self, req_hit_rate_data_model=None):
        self.req_hit_rate_data_model = req_hit_rate_data_model  # type: list[DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel]

    def validate(self):
        if self.req_hit_rate_data_model:
            for k in self.req_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReqHitRateDataModel'] = []
        if self.req_hit_rate_data_model is not None:
            for k in self.req_hit_rate_data_model:
                result['ReqHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.req_hit_rate_data_model = []
        if m.get('ReqHitRateDataModel') is not None:
            for k in m.get('ReqHitRateDataModel'):
                temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeReqHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataRequest, self).to_map()
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


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule, self).to_map()
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


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_src_bps_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval  # type: DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_bps_data_per_interval is not None:
            result['RealTimeSrcBpsDataPerInterval'] = self.real_time_src_bps_data_per_interval.to_map()
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
        if m.get('RealTimeSrcBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeSrcBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, isp_name_en=None, location_name_en=None, owner_id=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
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
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData, self).to_map()
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


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, real_time_src_code_proportion_data=None):
        self.real_time_src_code_proportion_data = real_time_src_code_proportion_data  # type: list[DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData]

    def validate(self):
        if self.real_time_src_code_proportion_data:
            for k in self.real_time_src_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeSrcCodeProportionData'] = []
        if self.real_time_src_code_proportion_data is not None:
            for k in self.real_time_src_code_proportion_data:
                result['RealTimeSrcCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.real_time_src_code_proportion_data = []
        if m.get('RealTimeSrcCodeProportionData') is not None:
            for k in m.get('RealTimeSrcCodeProportionData'):
                temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData()
                self.real_time_src_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData, self).to_map()
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
                temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, real_time_src_http_code_data=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_http_code_data = real_time_src_http_code_data  # type: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_http_code_data is not None:
            result['RealTimeSrcHttpCodeData'] = self.real_time_src_http_code_data.to_map()
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
        if m.get('RealTimeSrcHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataRequest, self).to_map()
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


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule, self).to_map()
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


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_src_traffic_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval  # type: DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_traffic_data_per_interval is not None:
            result['RealTimeSrcTrafficDataPerInterval'] = self.real_time_src_traffic_data_per_interval.to_map()
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
        if m.get('RealTimeSrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataRequest, self).to_map()
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


class DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule, self).to_map()
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


class DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_traffic_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval  # type: DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
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
        if m.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRealTimeTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRegionDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataRequest, self).to_map()
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


class DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(self, avg_object_size=None, avg_response_rate=None, avg_response_time=None, bps=None,
                 bytes_proportion=None, proportion=None, qps=None, region=None, region_ename=None, total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.total_bytes = total_bytes  # type: str
        self.total_query = total_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData, self).to_map()
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
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDcdnDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(self, region_proportion_data=None):
        self.region_proportion_data = region_proportion_data  # type: list[DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData]

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponseBodyValue, self).to_map()
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
                temp_model = DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRegionDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 value=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.value = value  # type: DescribeDcdnDomainRegionDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRegionDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainRegionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, function_names=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: list[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs]
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: list[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTopReferVisitRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, refer_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.refer_detail = refer_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(self, refer_list=None):
        self.refer_list = refer_list  # type: list[DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList]

    def validate(self):
        if self.refer_list:
            for k in self.refer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitResponseBodyTopReferList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReferList'] = []
        if self.refer_list is not None:
            for k in self.refer_list:
                result['ReferList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refer_list = []
        if m.get('ReferList') is not None:
            for k in m.get('ReferList'):
                temp_model = DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopReferVisitResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None, start_time=None, top_refer_list=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.top_refer_list = top_refer_list  # type: DescribeDcdnDomainTopReferVisitResponseBodyTopReferList

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopReferList') is not None:
            temp_model = DescribeDcdnDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeDcdnDomainTopReferVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainTopReferVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTopUrlVisitRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(self, all_url_list=None, domain_name=None, request_id=None, start_time=None, url_200list=None,
                 url_300list=None, url_400list=None, url_500list=None):
        self.all_url_list = all_url_list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.url_200list = url_200list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List
        self.url_300list = url_300list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List
        self.url_400list = url_400list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List
        self.url_500list = url_500list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List

    def validate(self):
        if self.all_url_list:
            self.all_url_list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_500list:
            self.url_500list.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url200List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDcdnDomainTopUrlVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainTopUrlVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_http_traffic=None, dynamic_https_traffic=None, static_http_traffic=None,
                 static_https_traffic=None, time_stamp=None, traffic=None):
        self.dynamic_http_traffic = dynamic_http_traffic  # type: float
        self.dynamic_https_traffic = dynamic_https_traffic  # type: float
        self.static_http_traffic = static_http_traffic  # type: float
        self.static_https_traffic = static_https_traffic  # type: float
        self.time_stamp = time_stamp  # type: str
        self.traffic = traffic  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_traffic is not None:
            result['DynamicHttpTraffic'] = self.dynamic_http_traffic
        if self.dynamic_https_traffic is not None:
            result['DynamicHttpsTraffic'] = self.dynamic_https_traffic
        if self.static_http_traffic is not None:
            result['StaticHttpTraffic'] = self.static_http_traffic
        if self.static_https_traffic is not None:
            result['StaticHttpsTraffic'] = self.static_https_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpTraffic') is not None:
            self.dynamic_http_traffic = m.get('DynamicHttpTraffic')
        if m.get('DynamicHttpsTraffic') is not None:
            self.dynamic_https_traffic = m.get('DynamicHttpsTraffic')
        if m.get('StaticHttpTraffic') is not None:
            self.static_http_traffic = m.get('StaticHttpTraffic')
        if m.get('StaticHttpsTraffic') is not None:
            self.static_https_traffic = m.get('StaticHttpsTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponseBody, self).to_map()
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
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
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
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainUsageDataRequest(TeaModel):
    def __init__(self, area=None, data_protocol=None, domain_name=None, end_time=None, field=None, interval=None,
                 owner_id=None, start_time=None):
        self.area = area  # type: str
        self.data_protocol = data_protocol  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.data_protocol is not None:
            result['DataProtocol'] = self.data_protocol
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DataProtocol') is not None:
            self.data_protocol = m.get('DataProtocol')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(self, peak_time=None, special_value=None, time_stamp=None, value=None):
        self.peak_time = peak_time  # type: str
        self.special_value = special_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUsageDataResponseBodyUsageDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.special_value is not None:
            result['SpecialValue'] = self.special_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('SpecialValue') is not None:
            self.special_value = m.get('SpecialValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnDomainUsageDataResponseBodyUsageDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainUsageDataResponseBodyUsageDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUsageDataResponseBodyUsageDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainUsageDataResponseBody(TeaModel):
    def __init__(self, area=None, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 start_time=None, type=None, usage_data_per_interval=None):
        self.area = area  # type: str
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.type = type  # type: str
        self.usage_data_per_interval = usage_data_per_interval  # type: DescribeDcdnDomainUsageDataResponseBodyUsageDataPerInterval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUsageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
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
        if self.type is not None:
            result['Type'] = self.type
        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
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
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsageDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        return self


class DescribeDcdnDomainUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUsageDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainUvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataRequest, self).to_map()
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


class DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData, self).to_map()
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


class DescribeDcdnDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponseBodyUvDataInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainUvDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 uv_data_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.uv_data_interval = uv_data_interval  # type: DescribeDcdnDomainUvDataResponseBodyUvDataInterval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponseBody, self).to_map()
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
            temp_model = DescribeDcdnDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeDcdnDomainUvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainUvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, websocket_bps=None):
        self.time_stamp = time_stamp  # type: str
        self.websocket_bps = websocket_bps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_bps is not None:
            result['WebsocketBps'] = self.websocket_bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketBps') is not None:
            self.websocket_bps = m.get('WebsocketBps')
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBody(TeaModel):
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataResponseBody, self).to_map()
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
        return self


class DescribeDcdnDomainWebsocketBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainWebsocketBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCodeHttpCodeDataModule(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: int
        self.count = count  # type: float
        self.proportion = proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCodeHttpCodeDataModule, self).to_map()
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


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCode(TeaModel):
    def __init__(self, http_code_data_module=None):
        self.http_code_data_module = http_code_data_module  # type: list[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCodeHttpCodeDataModule]

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HttpCodeDataModule'] = []
        if self.http_code_data_module is not None:
            for k in self.http_code_data_module:
                result['HttpCodeDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.http_code_data_module = []
        if m.get('HttpCodeDataModule') is not None:
            for k in m.get('HttpCodeDataModule'):
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCodeHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, websocket_http_code=None):
        self.time_stamp = time_stamp  # type: str
        self.websocket_http_code = websocket_http_code  # type: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCode

    def validate(self):
        if self.websocket_http_code:
            self.websocket_http_code.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_http_code is not None:
            result['WebsocketHttpCode'] = self.websocket_http_code.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketHttpCode') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModuleWebsocketHttpCode()
            self.websocket_http_code = temp_model.from_map(m['WebsocketHttpCode'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, http_code_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.http_code_data_per_interval = http_code_data_per_interval  # type: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.http_code_data_per_interval:
            self.http_code_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code_data_per_interval is not None:
            result['HttpCodeDataPerInterval'] = self.http_code_data_per_interval.to_map()
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
        if m.get('HttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyHttpCodeDataPerInterval()
            self.http_code_data_per_interval = temp_model.from_map(m['HttpCodeDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainWebsocketHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataRequest, self).to_map()
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
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, websocket_traffic=None):
        self.time_stamp = time_stamp  # type: str
        self.websocket_traffic = websocket_traffic  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_traffic is not None:
            result['WebsocketTraffic'] = self.websocket_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketTraffic') is not None:
            self.websocket_traffic = m.get('WebsocketTraffic')
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponseBody, self).to_map()
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
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
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
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnDomainWebsocketTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponse, self).to_map()
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
            temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnEsExceptionDataRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, rule_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnEsExceptionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnEsExceptionDataResponseBodyContents(TeaModel):
    def __init__(self, columns=None, name=None, points=None):
        self.columns = columns  # type: list[str]
        self.name = name  # type: str
        self.points = points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnEsExceptionDataResponseBodyContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns
        if self.name is not None:
            result['Name'] = self.name
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class DescribeDcdnEsExceptionDataResponseBody(TeaModel):
    def __init__(self, contents=None, request_id=None):
        self.contents = contents  # type: list[DescribeDcdnEsExceptionDataResponseBodyContents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnEsExceptionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeDcdnEsExceptionDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnEsExceptionDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnEsExceptionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnEsExceptionDataResponse, self).to_map()
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
            temp_model = DescribeDcdnEsExceptionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnEsExecuteDataRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, rule_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnEsExecuteDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnEsExecuteDataResponseBodyContents(TeaModel):
    def __init__(self, columns=None, name=None, points=None):
        self.columns = columns  # type: list[str]
        self.name = name  # type: str
        self.points = points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnEsExecuteDataResponseBodyContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns
        if self.name is not None:
            result['Name'] = self.name
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class DescribeDcdnEsExecuteDataResponseBody(TeaModel):
    def __init__(self, contents=None, request_id=None):
        self.contents = contents  # type: list[DescribeDcdnEsExecuteDataResponseBodyContents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnEsExecuteDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeDcdnEsExecuteDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnEsExecuteDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnEsExecuteDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnEsExecuteDataResponse, self).to_map()
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
            temp_model = DescribeDcdnEsExecuteDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnHttpsDomainListRequest(TeaModel):
    def __init__(self, keyword=None, owner_id=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_common_name=None, cert_expire_time=None, cert_name=None, cert_start_time=None,
                 cert_status=None, cert_type=None, cert_update_time=None, domain_name=None):
        self.cert_common_name = cert_common_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_start_time = cert_start_time  # type: str
        self.cert_status = cert_status  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_update_time = cert_update_time  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnHttpsDomainListResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponseBodyCertInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnHttpsDomainListResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None, total_count=None):
        self.cert_infos = cert_infos  # type: DescribeDcdnHttpsDomainListResponseBodyCertInfos
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDcdnHttpsDomainListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnHttpsDomainListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponse, self).to_map()
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
            temp_model = DescribeDcdnHttpsDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpInfoRequest(TeaModel):
    def __init__(self, ip=None, owner_id=None, security_token=None):
        self.ip = ip  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnIpInfoResponseBody(TeaModel):
    def __init__(self, dcdn_ip=None, isp=None, isp_ename=None, region=None, region_ename=None, request_id=None):
        self.dcdn_ip = dcdn_ip  # type: str
        self.isp = isp  # type: str
        self.isp_ename = isp_ename  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dcdn_ip is not None:
            result['DcdnIp'] = self.dcdn_ip
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DcdnIp') is not None:
            self.dcdn_ip = m.get('DcdnIp')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnIpInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnIpInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpInfoResponse, self).to_map()
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
            temp_model = DescribeDcdnIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaDomainConfigsRequest(TeaModel):
    def __init__(self, domain_name=None, function_names=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, domain_config=None):
        self.domain_config = domain_config  # type: list[DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig]

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainConfigsResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnIpaDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnIpaDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponse, self).to_map()
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
            temp_model = DescribeDcdnIpaDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaDomainDetailRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailRequest, self).to_map()
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


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, content=None, enabled=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.enabled = enabled  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource, self).to_map()
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
        if self.weight is not None:
            result['Weight'] = self.weight
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
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(self, cert_name=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, resource_group_id=None, sslprotocol=None, sslpub=None, scope=None,
                 sources=None):
        self.cert_name = cert_name  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.scope = scope  # type: str
        self.sources = sources  # type: DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBodyDomainDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
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
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
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
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnIpaDomainDetailResponseBody(TeaModel):
    def __init__(self, domain_detail=None, request_id=None):
        self.domain_detail = domain_detail  # type: DescribeDcdnIpaDomainDetailResponseBodyDomainDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnIpaDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnIpaDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponse, self).to_map()
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
            temp_model = DescribeDcdnIpaDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaServiceRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaServiceRequest, self).to_map()
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


class DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason, self).to_map()
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


class DescribeDcdnIpaServiceResponseBodyOperationLocks(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: list[DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason]

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaServiceResponseBodyOperationLocks, self).to_map()
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
                temp_model = DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaServiceResponseBody(TeaModel):
    def __init__(self, changing_affect_time=None, changing_charge_type=None, instance_id=None,
                 internet_charge_type=None, opening_time=None, operation_locks=None, request_id=None):
        self.changing_affect_time = changing_affect_time  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.opening_time = opening_time  # type: str
        self.operation_locks = operation_locks  # type: DescribeDcdnIpaServiceResponseBodyOperationLocks
        self.request_id = request_id  # type: str

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaServiceResponseBody, self).to_map()
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
            temp_model = DescribeDcdnIpaServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnIpaServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnIpaServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaServiceResponse, self).to_map()
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
            temp_model = DescribeDcdnIpaServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaUserDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnIpaUserDomainsRequest(TeaModel):
    def __init__(self, check_domain_show=None, domain_name=None, domain_search_type=None, domain_status=None,
                 func_filter=None, func_id=None, owner_id=None, page_number=None, page_size=None, resource_group_id=None,
                 security_token=None, tag=None):
        self.check_domain_show = check_domain_show  # type: bool
        self.domain_name = domain_name  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.domain_status = domain_status  # type: str
        self.func_filter = func_filter  # type: str
        self.func_id = func_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.tag = tag  # type: list[DescribeDcdnIpaUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        if self.func_id is not None:
            result['FuncId'] = self.func_id
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnIpaUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cname=None, description=None, domain_name=None, domain_status=None, gmt_created=None,
                 gmt_modified=None, resource_group_id=None, sslprotocol=None, sandbox=None, sources=None):
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sandbox = sandbox  # type: str
        self.sources = sources  # type: DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomains, self).to_map()
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
                temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaUserDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeDcdnIpaUserDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBody, self).to_map()
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
            temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomains()
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


class DescribeDcdnIpaUserDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnIpaUserDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponse, self).to_map()
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
            temp_model = DescribeDcdnIpaUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRealTimeDeliveryFieldRequest(TeaModel):
    def __init__(self, business_type=None, owner_id=None):
        self.business_type = business_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRealTimeDeliveryFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields(TeaModel):
    def __init__(self, description=None, field_name=None):
        self.description = description  # type: str
        self.field_name = field_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        return self


class DescribeDcdnRealTimeDeliveryFieldResponseBodyContent(TeaModel):
    def __init__(self, fields=None):
        self.fields = fields  # type: list[DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields]

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnRealTimeDeliveryFieldResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeDcdnRealTimeDeliveryFieldResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: DescribeDcdnRealTimeDeliveryFieldResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(DescribeDcdnRealTimeDeliveryFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = DescribeDcdnRealTimeDeliveryFieldResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnRealTimeDeliveryFieldResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnRealTimeDeliveryFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnRealTimeDeliveryFieldResponse, self).to_map()
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
            temp_model = DescribeDcdnRealTimeDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshQuotaRequest, self).to_map()
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


class DescribeDcdnRefreshQuotaResponseBody(TeaModel):
    def __init__(self, block_quota=None, block_remain=None, dir_quota=None, dir_remain=None, preload_quota=None,
                 preload_remain=None, regex_quota=None, regex_remain=None, request_id=None, url_quota=None, url_remain=None):
        self.block_quota = block_quota  # type: str
        self.block_remain = block_remain  # type: str
        self.dir_quota = dir_quota  # type: str
        self.dir_remain = dir_remain  # type: str
        self.preload_quota = preload_quota  # type: str
        self.preload_remain = preload_remain  # type: str
        self.regex_quota = regex_quota  # type: str
        self.regex_remain = regex_remain  # type: str
        self.request_id = request_id  # type: str
        self.url_quota = url_quota  # type: str
        self.url_remain = url_remain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshQuotaResponseBody, self).to_map()
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
        if self.regex_quota is not None:
            result['RegexQuota'] = self.regex_quota
        if self.regex_remain is not None:
            result['RegexRemain'] = self.regex_remain
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
        if m.get('RegexQuota') is not None:
            self.regex_quota = m.get('RegexQuota')
        if m.get('RegexRemain') is not None:
            self.regex_remain = m.get('RegexRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        return self


class DescribeDcdnRefreshQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnRefreshQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshQuotaResponse, self).to_map()
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
            temp_model = DescribeDcdnRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshTaskByIdRequest(TeaModel):
    def __init__(self, owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTaskByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTaskByIdResponseBodyTasks(TeaModel):
    def __init__(self, creation_time=None, description=None, object_path=None, object_type=None, process=None,
                 status=None, task_id=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.process = process  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTaskByIdResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTaskByIdResponseBody(TeaModel):
    def __init__(self, request_id=None, tasks=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[DescribeDcdnRefreshTaskByIdResponseBodyTasks]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTaskByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeDcdnRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDcdnRefreshTaskByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnRefreshTaskByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTaskByIdResponse, self).to_map()
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
            temp_model = DescribeDcdnRefreshTaskByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshTasksRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, object_path=None, object_type=None, owner_id=None,
                 page_number=None, page_size=None, security_token=None, start_time=None, status=None, task_id=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
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
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTasksResponseBodyTasksTask(TeaModel):
    def __init__(self, creation_time=None, description=None, object_path=None, object_type=None, process=None,
                 status=None, task_id=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.process = process  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponseBodyTasksTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[DescribeDcdnRefreshTasksResponseBodyTasksTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeDcdnRefreshTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeDcdnRefreshTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: DescribeDcdnRefreshTasksResponseBodyTasks
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tasks') is not None:
            temp_model = DescribeDcdnRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDcdnRefreshTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnRefreshTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponse, self).to_map()
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
            temp_model = DescribeDcdnRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRegionAndIspRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspRequest, self).to_map()
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


class DescribeDcdnRegionAndIspResponseBodyIspsIsp(TeaModel):
    def __init__(self, name_en=None, name_zh=None):
        self.name_en = name_en  # type: str
        self.name_zh = name_zh  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBodyIspsIsp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeDcdnRegionAndIspResponseBodyIsps(TeaModel):
    def __init__(self, isp=None):
        self.isp = isp  # type: list[DescribeDcdnRegionAndIspResponseBodyIspsIsp]

    def validate(self):
        if self.isp:
            for k in self.isp:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBodyIsps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isp'] = []
        if self.isp is not None:
            for k in self.isp:
                result['Isp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.isp = []
        if m.get('Isp') is not None:
            for k in m.get('Isp'):
                temp_model = DescribeDcdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k))
        return self


class DescribeDcdnRegionAndIspResponseBodyRegionsRegion(TeaModel):
    def __init__(self, name_en=None, name_zh=None):
        self.name_en = name_en  # type: str
        self.name_zh = name_zh  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeDcdnRegionAndIspResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeDcdnRegionAndIspResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeDcdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeDcdnRegionAndIspResponseBody(TeaModel):
    def __init__(self, isps=None, regions=None, request_id=None):
        self.isps = isps  # type: DescribeDcdnRegionAndIspResponseBodyIsps
        self.regions = regions  # type: DescribeDcdnRegionAndIspResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.isps:
            self.isps.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isps is not None:
            result['Isps'] = self.isps.to_map()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Isps') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
        if m.get('Regions') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnRegionAndIspResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnRegionAndIspResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponse, self).to_map()
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
            temp_model = DescribeDcdnRegionAndIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnReportRequest(TeaModel):
    def __init__(self, area=None, domain_name=None, end_time=None, http_code=None, is_overseas=None, owner_id=None,
                 report_id=None, start_time=None):
        self.area = area  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.http_code = http_code  # type: str
        self.is_overseas = is_overseas  # type: str
        self.owner_id = owner_id  # type: long
        self.report_id = report_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnReportResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnReportResponse, self).to_map()
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
            temp_model = DescribeDcdnReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnReportListRequest(TeaModel):
    def __init__(self, owner_id=None, report_id=None):
        self.owner_id = owner_id  # type: long
        self.report_id = report_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnReportListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class DescribeDcdnReportListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnReportListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnReportListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnReportListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnReportListResponse, self).to_map()
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
            temp_model = DescribeDcdnReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSLSRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, business_type=None, owner_id=None, project_name=None):
        self.business_type = business_type  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSLSRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent(TeaModel):
    def __init__(self, business_type=None, data_center=None, domain_name=None, field_name=None, project_name=None,
                 slslog_store=None, slsproject=None, slsregion=None, sampling_rate=None, type=None):
        self.business_type = business_type  # type: str
        self.data_center = data_center  # type: str
        self.domain_name = domain_name  # type: str
        self.field_name = field_name  # type: str
        self.project_name = project_name  # type: str
        self.slslog_store = slslog_store  # type: str
        self.slsproject = slsproject  # type: str
        self.slsregion = slsregion  # type: str
        self.sampling_rate = sampling_rate  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDcdnSLSRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(DescribeDcdnSLSRealtimeLogDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnSLSRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSLSRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSLSRealtimeLogDeliveryResponse, self).to_map()
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
            temp_model = DescribeDcdnSLSRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSMCertificateDetailRequest(TeaModel):
    def __init__(self, cert_identifier=None, owner_id=None, security_token=None):
        self.cert_identifier = cert_identifier  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnSMCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert_expire_time=None, cert_identifier=None, cert_name=None, cert_org=None, common_name=None,
                 encrypt_certificate=None, request_id=None, sans=None, sign_certificate=None):
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.common_name = common_name  # type: str
        self.encrypt_certificate = encrypt_certificate  # type: str
        self.request_id = request_id  # type: str
        self.sans = sans  # type: str
        self.sign_certificate = sign_certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')
        return self


class DescribeDcdnSMCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSMCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateDetailResponse, self).to_map()
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
            temp_model = DescribeDcdnSMCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSMCertificateListRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateListRequest, self).to_map()
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


class DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert_identifier=None, cert_name=None, common=None, issuer=None):
        self.cert_identifier = cert_identifier  # type: str
        self.cert_name = cert_name  # type: str
        self.common = common  # type: str
        self.issuer = issuer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class DescribeDcdnSMCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: list[DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList]
        self.count = count  # type: int

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateListResponseBodyCertificateListModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnSMCertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeDcdnSMCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeDcdnSMCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnSMCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSMCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSMCertificateListResponse, self).to_map()
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
            temp_model = DescribeDcdnSMCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSecFuncInfoRequest(TeaModel):
    def __init__(self, lang=None, owner_id=None, sec_func_type=None):
        self.lang = lang  # type: str
        self.owner_id = owner_id  # type: long
        self.sec_func_type = sec_func_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSecFuncInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func_type is not None:
            result['SecFuncType'] = self.sec_func_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFuncType') is not None:
            self.sec_func_type = m.get('SecFuncType')
        return self


class DescribeDcdnSecFuncInfoResponseBodyContent(TeaModel):
    def __init__(self, label=None, value=None):
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSecFuncInfoResponseBodyContent, self).to_map()
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


class DescribeDcdnSecFuncInfoResponseBody(TeaModel):
    def __init__(self, content=None, description=None, http_status=None, request_id=None, ret_code=None):
        self.content = content  # type: list[DescribeDcdnSecFuncInfoResponseBodyContent]
        self.description = description  # type: str
        self.http_status = http_status  # type: str
        self.request_id = request_id  # type: str
        self.ret_code = ret_code  # type: str

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnSecFuncInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeDcdnSecFuncInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        return self


class DescribeDcdnSecFuncInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSecFuncInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSecFuncInfoResponse, self).to_map()
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
            temp_model = DescribeDcdnSecFuncInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSecSpecInfoRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSecSpecInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs(TeaModel):
    def __init__(self, code=None, expr=None, value=None):
        self.code = code  # type: str
        self.expr = expr  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.expr is not None:
            result['Expr'] = self.expr
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Expr') is not None:
            self.expr = m.get('Expr')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnSecSpecInfoResponseBodySpecInfos(TeaModel):
    def __init__(self, rule_code=None, rule_configs=None):
        self.rule_code = rule_code  # type: str
        self.rule_configs = rule_configs  # type: list[DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs]

    def validate(self):
        if self.rule_configs:
            for k in self.rule_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnSecSpecInfoResponseBodySpecInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        result['RuleConfigs'] = []
        if self.rule_configs is not None:
            for k in self.rule_configs:
                result['RuleConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        self.rule_configs = []
        if m.get('RuleConfigs') is not None:
            for k in m.get('RuleConfigs'):
                temp_model = DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs()
                self.rule_configs.append(temp_model.from_map(k))
        return self


class DescribeDcdnSecSpecInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, spec_infos=None, version=None):
        self.request_id = request_id  # type: str
        self.spec_infos = spec_infos  # type: list[DescribeDcdnSecSpecInfoResponseBodySpecInfos]
        self.version = version  # type: str

    def validate(self):
        if self.spec_infos:
            for k in self.spec_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnSecSpecInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpecInfos'] = []
        if self.spec_infos is not None:
            for k in self.spec_infos:
                result['SpecInfos'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spec_infos = []
        if m.get('SpecInfos') is not None:
            for k in m.get('SpecInfos'):
                temp_model = DescribeDcdnSecSpecInfoResponseBodySpecInfos()
                self.spec_infos.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDcdnSecSpecInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSecSpecInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSecSpecInfoResponse, self).to_map()
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
            temp_model = DescribeDcdnSecSpecInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnServiceRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnServiceRequest, self).to_map()
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


class DescribeDcdnServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnServiceResponseBodyOperationLocksLockReason, self).to_map()
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


class DescribeDcdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: list[DescribeDcdnServiceResponseBodyOperationLocksLockReason]

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnServiceResponseBodyOperationLocks, self).to_map()
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
                temp_model = DescribeDcdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeDcdnServiceResponseBody(TeaModel):
    def __init__(self, changing_affect_time=None, changing_charge_type=None, instance_id=None,
                 internet_charge_type=None, opening_time=None, operation_locks=None, request_id=None, websocket_changing_time=None,
                 websocket_changing_type=None, websocket_type=None):
        self.changing_affect_time = changing_affect_time  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.opening_time = opening_time  # type: str
        self.operation_locks = operation_locks  # type: DescribeDcdnServiceResponseBodyOperationLocks
        self.request_id = request_id  # type: str
        self.websocket_changing_time = websocket_changing_time  # type: str
        self.websocket_changing_type = websocket_changing_type  # type: str
        self.websocket_type = websocket_type  # type: str

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super(DescribeDcdnServiceResponseBody, self).to_map()
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
        if self.websocket_changing_time is not None:
            result['WebsocketChangingTime'] = self.websocket_changing_time
        if self.websocket_changing_type is not None:
            result['WebsocketChangingType'] = self.websocket_changing_type
        if self.websocket_type is not None:
            result['WebsocketType'] = self.websocket_type
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
            temp_model = DescribeDcdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebsocketChangingTime') is not None:
            self.websocket_changing_time = m.get('WebsocketChangingTime')
        if m.get('WebsocketChangingType') is not None:
            self.websocket_changing_type = m.get('WebsocketChangingType')
        if m.get('WebsocketType') is not None:
            self.websocket_type = m.get('WebsocketType')
        return self


class DescribeDcdnServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnServiceResponse, self).to_map()
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
            temp_model = DescribeDcdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnStagingIpRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnStagingIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnStagingIpResponseBodyIPV4s(TeaModel):
    def __init__(self, ipv4=None):
        self.ipv4 = ipv4  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnStagingIpResponseBodyIPV4s, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')
        return self


class DescribeDcdnStagingIpResponseBody(TeaModel):
    def __init__(self, ipv4s=None, request_id=None):
        self.ipv4s = ipv4s  # type: DescribeDcdnStagingIpResponseBodyIPV4s
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        _map = super(DescribeDcdnStagingIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4s is not None:
            result['IPV4s'] = self.ipv4s.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IPV4s') is not None:
            temp_model = DescribeDcdnStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnStagingIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnStagingIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnStagingIpResponse, self).to_map()
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
            temp_model = DescribeDcdnStagingIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSubListRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSubListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnSubListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSubListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnSubListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnSubListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnSubListResponse, self).to_map()
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
            temp_model = DescribeDcdnSubListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnTagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[DescribeDcdnTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponseBodyTagResourcesTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesResponseBodyTagResourcesTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, tag=None):
        self.resource_id = resource_id  # type: str
        self.tag = tag  # type: list[DescribeDcdnTagResourcesResponseBodyTagResourcesTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[DescribeDcdnTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeDcdnTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnTagResourcesResponse, self).to_map()
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
            temp_model = DescribeDcdnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnTopDomainsByFlowRequest(TeaModel):
    def __init__(self, end_time=None, limit=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(self, domain_name=None, max_bps=None, max_bps_time=None, rank=None, total_access=None,
                 total_traffic=None, traffic_percent=None):
        self.domain_name = domain_name  # type: str
        self.max_bps = max_bps  # type: long
        self.max_bps_time = max_bps_time  # type: str
        self.rank = rank  # type: long
        self.total_access = total_access  # type: long
        self.total_traffic = total_traffic  # type: str
        self.traffic_percent = traffic_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain, self).to_map()
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


class DescribeDcdnTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(self, top_domain=None):
        self.top_domain = top_domain  # type: list[DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain]

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponseBodyTopDomains, self).to_map()
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
                temp_model = DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeDcdnTopDomainsByFlowResponseBody(TeaModel):
    def __init__(self, domain_count=None, domain_online_count=None, end_time=None, request_id=None, start_time=None,
                 top_domains=None):
        self.domain_count = domain_count  # type: long
        self.domain_online_count = domain_online_count  # type: long
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.top_domains = top_domains  # type: DescribeDcdnTopDomainsByFlowResponseBodyTopDomains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponseBody, self).to_map()
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
            temp_model = DescribeDcdnTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeDcdnTopDomainsByFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnTopDomainsByFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponse, self).to_map()
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
            temp_model = DescribeDcdnTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserBillHistoryRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(self, bandwidth=None, cdn_region=None, charge_type=None, count=None, flow=None):
        self.bandwidth = bandwidth  # type: float
        self.cdn_region = cdn_region  # type: str
        self.charge_type = charge_type  # type: str
        self.count = count  # type: float
        self.flow = flow  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(TeaModel):
    def __init__(self, billing_data_item=None):
        self.billing_data_item = billing_data_item  # type: list[DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem]

    def validate(self):
        if self.billing_data_item:
            for k in self.billing_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillingDataItem'] = []
        if self.billing_data_item is not None:
            for k in self.billing_data_item:
                result['BillingDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.billing_data_item = []
        if m.get('BillingDataItem') is not None:
            for k in m.get('BillingDataItem'):
                temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(TeaModel):
    def __init__(self, bill_time=None, bill_type=None, billing_data=None, dimension=None):
        self.bill_time = bill_time  # type: str
        self.bill_type = bill_type  # type: str
        self.billing_data = billing_data  # type: DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData
        self.dimension = dimension  # type: str

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillingData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryData(TeaModel):
    def __init__(self, bill_history_data_item=None):
        self.bill_history_data_item = bill_history_data_item  # type: list[DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem]

    def validate(self):
        if self.bill_history_data_item:
            for k in self.bill_history_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillHistoryDataItem'] = []
        if self.bill_history_data_item is not None:
            for k in self.bill_history_data_item:
                result['BillHistoryDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bill_history_data_item = []
        if m.get('BillHistoryDataItem') is not None:
            for k in m.get('BillHistoryDataItem'):
                temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillHistoryResponseBody(TeaModel):
    def __init__(self, bill_history_data=None, request_id=None):
        self.bill_history_data = bill_history_data  # type: DescribeDcdnUserBillHistoryResponseBodyBillHistoryData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_history_data is not None:
            result['BillHistoryData'] = self.bill_history_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillHistoryData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnUserBillHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserBillHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponse, self).to_map()
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
            temp_model = DescribeDcdnUserBillHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserBillTypeRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
    def __init__(self, bill_type=None, billing_cycle=None, dimension=None, end_time=None, product=None,
                 start_time=None):
        self.bill_type = bill_type  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.dimension = dimension  # type: str
        self.end_time = end_time  # type: str
        self.product = product  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.product is not None:
            result['Product'] = self.product
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnUserBillTypeResponseBodyBillTypeData(TeaModel):
    def __init__(self, bill_type_data_item=None):
        self.bill_type_data_item = bill_type_data_item  # type: list[DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem]

    def validate(self):
        if self.bill_type_data_item:
            for k in self.bill_type_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponseBodyBillTypeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillTypeDataItem'] = []
        if self.bill_type_data_item is not None:
            for k in self.bill_type_data_item:
                result['BillTypeDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bill_type_data_item = []
        if m.get('BillTypeDataItem') is not None:
            for k in m.get('BillTypeDataItem'):
                temp_model = DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillTypeResponseBody(TeaModel):
    def __init__(self, bill_type_data=None, request_id=None):
        self.bill_type_data = bill_type_data  # type: DescribeDcdnUserBillTypeResponseBodyBillTypeData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_type_data is not None:
            result['BillTypeData'] = self.bill_type_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillTypeData') is not None:
            temp_model = DescribeDcdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnUserBillTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserBillTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponse, self).to_map()
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
            temp_model = DescribeDcdnUserBillTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnUserDomainsRequest(TeaModel):
    def __init__(self, change_end_time=None, change_start_time=None, check_domain_show=None, coverage=None,
                 domain_name=None, domain_search_type=None, domain_status=None, owner_id=None, page_number=None, page_size=None,
                 resource_group_id=None, security_token=None, tag=None):
        self.change_end_time = change_end_time  # type: str
        self.change_start_time = change_start_time  # type: str
        self.check_domain_show = check_domain_show  # type: bool
        self.coverage = coverage  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.domain_status = domain_status  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.tag = tag  # type: list[DescribeDcdnUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.coverage is not None:
            result['Coverage'] = self.coverage
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cname=None, description=None, domain_name=None, domain_status=None, gmt_created=None,
                 gmt_modified=None, resource_group_id=None, sslprotocol=None, sandbox=None, sources=None):
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sandbox = sandbox  # type: str
        self.sources = sources  # type: DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnUserDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeDcdnUserDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomains, self).to_map()
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
                temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeDcdnUserDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBody, self).to_map()
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
            temp_model = DescribeDcdnUserDomainsResponseBodyDomains()
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


class DescribeDcdnUserDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponse, self).to_map()
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
            temp_model = DescribeDcdnUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserDomainsByFuncRequest(TeaModel):
    def __init__(self, domain_name=None, func_filter=None, func_id=None, owner_id=None, page_number=None,
                 page_size=None, resource_group_id=None):
        self.domain_name = domain_name  # type: str
        self.func_filter = func_filter  # type: str
        self.func_id = func_id  # type: int
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cname=None, description=None, domain_name=None, domain_status=None, gmt_created=None,
                 gmt_modified=None, resource_group_id=None, sandbox=None, sources=None, ssl_protocol=None):
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
        self.sources = sources  # type: DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources
        self.ssl_protocol = ssl_protocol  # type: str

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomains, self).to_map()
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
                temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsByFuncResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeDcdnUserDomainsByFuncResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBody, self).to_map()
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
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomains()
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


class DescribeDcdnUserDomainsByFuncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserDomainsByFuncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponse, self).to_map()
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
            temp_model = DescribeDcdnUserDomainsByFuncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserQuotaRequest, self).to_map()
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


class DescribeDcdnUserQuotaResponseBody(TeaModel):
    def __init__(self, block_quota=None, block_remain=None, domain_quota=None, preload_quota=None,
                 preload_remain=None, refresh_dir_quota=None, refresh_dir_remain=None, refresh_url_quota=None,
                 refresh_url_remain=None, request_id=None):
        self.block_quota = block_quota  # type: int
        self.block_remain = block_remain  # type: int
        self.domain_quota = domain_quota  # type: int
        self.preload_quota = preload_quota  # type: int
        self.preload_remain = preload_remain  # type: int
        self.refresh_dir_quota = refresh_dir_quota  # type: int
        self.refresh_dir_remain = refresh_dir_remain  # type: int
        self.refresh_url_quota = refresh_url_quota  # type: int
        self.refresh_url_remain = refresh_url_remain  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota
        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain
        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota
        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')
        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')
        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')
        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserQuotaResponse, self).to_map()
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
            temp_model = DescribeDcdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserRealTimeDeliveryFieldRequest(TeaModel):
    def __init__(self, business_type=None, owner_id=None):
        self.business_type = business_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserRealTimeDeliveryFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContentFields(TeaModel):
    def __init__(self, description=None, field_name=None, selected=None):
        self.description = description  # type: str
        self.field_name = field_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContentFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContent(TeaModel):
    def __init__(self, fields=None):
        self.fields = fields  # type: list[DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContentFields]

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContentFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserRealTimeDeliveryFieldResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserRealTimeDeliveryFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = DescribeDcdnUserRealTimeDeliveryFieldResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnUserRealTimeDeliveryFieldResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserRealTimeDeliveryFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserRealTimeDeliveryFieldResponse, self).to_map()
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
            temp_model = DescribeDcdnUserRealTimeDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, status=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(self, commodity_code=None, curr_capacity=None, display_name=None, end_time=None,
                 init_capacity=None, instance_id=None, start_time=None, status=None, template_name=None):
        self.commodity_code = commodity_code  # type: str
        self.curr_capacity = curr_capacity  # type: str
        self.display_name = display_name  # type: str
        self.end_time = end_time  # type: str
        self.init_capacity = init_capacity  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(self, resource_package_info=None):
        self.resource_package_info = resource_package_info  # type: list[DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo]

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k in self.resource_package_info:
                result['ResourcePackageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k in m.get('ResourcePackageInfo'):
                temp_model = DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserResourcePackageResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_package_infos=None):
        self.request_id = request_id  # type: str
        self.resource_package_infos = resource_package_infos  # type: DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePackageInfos') is not None:
            temp_model = DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeDcdnUserResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageResponse, self).to_map()
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
            temp_model = DescribeDcdnUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserSecDropRequest(TeaModel):
    def __init__(self, data=None, metric=None, owner_id=None, sec_func=None):
        self.data = data  # type: str
        self.metric = metric  # type: str
        self.owner_id = owner_id  # type: long
        self.sec_func = sec_func  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        return self


class DescribeDcdnUserSecDropResponseBody(TeaModel):
    def __init__(self, drops=None, msg=None, request_id=None, uuid_str=None):
        self.drops = drops  # type: int
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.uuid_str = uuid_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uuid_str is not None:
            result['UuidStr'] = self.uuid_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UuidStr') is not None:
            self.uuid_str = m.get('UuidStr')
        return self


class DescribeDcdnUserSecDropResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserSecDropResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropResponse, self).to_map()
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
            temp_model = DescribeDcdnUserSecDropResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserSecDropByMinuteRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, lang=None, object=None, owner_id=None, page_number=None,
                 page_size=None, rule_name=None, sec_func=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.lang = lang  # type: str
        self.object = object  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.rule_name = rule_name  # type: str
        self.sec_func = sec_func  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.object is not None:
            result['Object'] = self.object
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBodyRows(TeaModel):
    def __init__(self, domain=None, drops=None, object=None, rule_name=None, sec_func=None, tm_str=None):
        self.domain = domain  # type: str
        self.drops = drops  # type: int
        self.object = object  # type: str
        self.rule_name = rule_name  # type: str
        self.sec_func = sec_func  # type: str
        self.tm_str = tm_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteResponseBodyRows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.object is not None:
            result['Object'] = self.object
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.tm_str is not None:
            result['TmStr'] = self.tm_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('TmStr') is not None:
            self.tm_str = m.get('TmStr')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBody(TeaModel):
    def __init__(self, description=None, len=None, page_number=None, page_size=None, request_id=None, rows=None,
                 total_count=None):
        self.description = description  # type: str
        self.len = len  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.rows = rows  # type: list[DescribeDcdnUserSecDropByMinuteResponseBodyRows]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.len is not None:
            result['Len'] = self.len
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Len') is not None:
            self.len = m.get('Len')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = DescribeDcdnUserSecDropByMinuteResponseBodyRows()
                self.rows.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDcdnUserSecDropByMinuteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserSecDropByMinuteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteResponse, self).to_map()
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
            temp_model = DescribeDcdnUserSecDropByMinuteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserTagsRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnUserTagsResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnUserTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[DescribeDcdnUserTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDcdnUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnUserTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserTagsResponse, self).to_map()
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
            temp_model = DescribeDcdnUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnVerifyContentRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnVerifyContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnVerifyContentResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnVerifyContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnVerifyContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnVerifyContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnVerifyContentResponse, self).to_map()
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
            temp_model = DescribeDcdnVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnWafDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, region_id=None, resource_group_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnWafDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDcdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(self, acl_status=None, cc_status=None, domain=None, status=None, waf_status=None):
        self.acl_status = acl_status  # type: int
        self.cc_status = cc_status  # type: int
        self.domain = domain  # type: str
        self.status = status  # type: int
        self.waf_status = waf_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnWafDomainResponseBodyOutPutDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeDcdnWafDomainResponseBody(TeaModel):
    def __init__(self, out_put_domains=None, request_id=None, total_count=None):
        self.out_put_domains = out_put_domains  # type: list[DescribeDcdnWafDomainResponseBodyOutPutDomains]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.out_put_domains:
            for k in self.out_put_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnWafDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OutPutDomains'] = []
        if self.out_put_domains is not None:
            for k in self.out_put_domains:
                result['OutPutDomains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.out_put_domains = []
        if m.get('OutPutDomains') is not None:
            for k in m.get('OutPutDomains'):
                temp_model = DescribeDcdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDcdnWafDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnWafDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnWafDomainResponse, self).to_map()
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
            temp_model = DescribeDcdnWafDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnsecServiceRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnsecServiceRequest, self).to_map()
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


class DescribeDcdnsecServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnsecServiceResponseBodyOperationLocksLockReason, self).to_map()
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


class DescribeDcdnsecServiceResponseBodyOperationLocks(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason  # type: list[DescribeDcdnsecServiceResponseBodyOperationLocksLockReason]

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnsecServiceResponseBodyOperationLocks, self).to_map()
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
                temp_model = DescribeDcdnsecServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeDcdnsecServiceResponseBody(TeaModel):
    def __init__(self, changing_affect_time=None, changing_charge_type=None, domain_num=None, end_time=None,
                 flow_type=None, instance_id=None, internet_charge_type=None, operation_locks=None, request_id=None,
                 request_type=None, start_time=None, version=None):
        self.changing_affect_time = changing_affect_time  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.domain_num = domain_num  # type: str
        self.end_time = end_time  # type: str
        self.flow_type = flow_type  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.operation_locks = operation_locks  # type: DescribeDcdnsecServiceResponseBodyOperationLocks
        self.request_id = request_id  # type: str
        self.request_type = request_type  # type: str
        self.start_time = start_time  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super(DescribeDcdnsecServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.domain_num is not None:
            result['DomainNum'] = self.domain_num
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_type is not None:
            result['RequestType'] = self.request_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('DomainNum') is not None:
            self.domain_num = m.get('DomainNum')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeDcdnsecServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDcdnsecServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnsecServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnsecServiceResponse, self).to_map()
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
            temp_model = DescribeDcdnsecServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineRequest(TeaModel):
    def __init__(self, name=None, owner_id=None):
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRoutineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoutineResponse, self).to_map()
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
            temp_model = DescribeRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineCanaryEnvsRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineCanaryEnvsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineCanaryEnvsResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineCanaryEnvsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineCanaryEnvsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRoutineCanaryEnvsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoutineCanaryEnvsResponse, self).to_map()
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
            temp_model = DescribeRoutineCanaryEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineCodeRevisionRequest(TeaModel):
    def __init__(self, name=None, owner_id=None, select_code_revision=None):
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class DescribeRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineCodeRevisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineCodeRevisionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRoutineCodeRevisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoutineCodeRevisionResponse, self).to_map()
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
            temp_model = DescribeRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineSpecRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineSpecResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineSpecResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRoutineSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoutineSpecResponse, self).to_map()
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
            temp_model = DescribeRoutineSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineUserInfoRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineUserInfoResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineUserInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRoutineUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoutineUserInfoResponse, self).to_map()
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
            temp_model = DescribeRoutineUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDcdnIpaStatusRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnIpaStatusRequest, self).to_map()
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


class DescribeUserDcdnIpaStatusResponseBody(TeaModel):
    def __init__(self, enabled=None, in_debt=None, in_debt_overdue=None, on_service=None, request_id=None):
        self.enabled = enabled  # type: bool
        self.in_debt = in_debt  # type: bool
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnIpaStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserDcdnIpaStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserDcdnIpaStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserDcdnIpaStatusResponse, self).to_map()
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
            temp_model = DescribeUserDcdnIpaStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDcdnStatusRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnStatusRequest, self).to_map()
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


class DescribeUserDcdnStatusResponseBody(TeaModel):
    def __init__(self, enabled=None, in_debt=None, in_debt_overdue=None, on_service=None, request_id=None):
        self.enabled = enabled  # type: bool
        self.in_debt = in_debt  # type: bool
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserDcdnStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserDcdnStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserDcdnStatusResponse, self).to_map()
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
            temp_model = DescribeUserDcdnStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserErStatusRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserErStatusRequest, self).to_map()
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


class DescribeUserErStatusResponseBody(TeaModel):
    def __init__(self, enabled=None, in_debt=None, in_debt_overdue=None, on_service=None, request_id=None):
        self.enabled = enabled  # type: bool
        self.in_debt = in_debt  # type: bool
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserErStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserErStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserErStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserErStatusResponse, self).to_map()
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
            temp_model = DescribeUserErStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLogserviceStatusRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserLogserviceStatusRequest, self).to_map()
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


class DescribeUserLogserviceStatusResponseBody(TeaModel):
    def __init__(self, enabled=None, in_debt=None, in_debt_overdue=None, on_service=None, request_id=None):
        self.enabled = enabled  # type: bool
        self.in_debt = in_debt  # type: bool
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserLogserviceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserLogserviceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserLogserviceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserLogserviceStatusResponse, self).to_map()
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
            temp_model = DescribeUserLogserviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditRoutineConfRequest(TeaModel):
    def __init__(self, description=None, env_conf=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.env_conf = env_conf  # type: dict[str, any]
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditRoutineConfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EditRoutineConfShrinkRequest(TeaModel):
    def __init__(self, description=None, env_conf_shrink=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.env_conf_shrink = env_conf_shrink  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditRoutineConfShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EditRoutineConfResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditRoutineConfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditRoutineConfResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditRoutineConfResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditRoutineConfResponse, self).to_map()
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
            temp_model = EditRoutineConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDcdnRealTimeDeliveryProjectRequest(TeaModel):
    def __init__(self, business_type=None, domain_name=None, owner_id=None, page_number=None, page_size=None):
        self.business_type = business_type  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDcdnRealTimeDeliveryProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDcdnRealTimeDeliveryProjectResponseBodyContentProjects(TeaModel):
    def __init__(self, business_type=None, data_center=None, domain_name=None, field_name=None, project_name=None,
                 slslog_store=None, slsproject=None, slsregion=None, sampling_rate=None, type=None):
        self.business_type = business_type  # type: str
        self.data_center = data_center  # type: str
        self.domain_name = domain_name  # type: str
        self.field_name = field_name  # type: str
        self.project_name = project_name  # type: str
        self.slslog_store = slslog_store  # type: str
        self.slsproject = slsproject  # type: str
        self.slsregion = slsregion  # type: str
        self.sampling_rate = sampling_rate  # type: float
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDcdnRealTimeDeliveryProjectResponseBodyContentProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDcdnRealTimeDeliveryProjectResponseBodyContent(TeaModel):
    def __init__(self, projects=None):
        self.projects = projects  # type: list[ListDcdnRealTimeDeliveryProjectResponseBodyContentProjects]

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDcdnRealTimeDeliveryProjectResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListDcdnRealTimeDeliveryProjectResponseBodyContentProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListDcdnRealTimeDeliveryProjectResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None, total_count=None):
        self.content = content  # type: ListDcdnRealTimeDeliveryProjectResponseBodyContent
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListDcdnRealTimeDeliveryProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = ListDcdnRealTimeDeliveryProjectResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDcdnRealTimeDeliveryProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDcdnRealTimeDeliveryProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDcdnRealTimeDeliveryProjectResponse, self).to_map()
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
            temp_model = ListDcdnRealTimeDeliveryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDCdnDomainSchdmByPropertyRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, property=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.property = property  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDCdnDomainSchdmByPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.property is not None:
            result['Property'] = self.property
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        return self


class ModifyDCdnDomainSchdmByPropertyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDCdnDomainSchdmByPropertyResponseBody, self).to_map()
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


class ModifyDCdnDomainSchdmByPropertyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDCdnDomainSchdmByPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDCdnDomainSchdmByPropertyResponse, self).to_map()
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
            temp_model = ModifyDCdnDomainSchdmByPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDcdnServiceRequest(TeaModel):
    def __init__(self, bill_type=None, owner_id=None, security_token=None, websocket_bill_type=None):
        self.bill_type = bill_type  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.websocket_bill_type = websocket_bill_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDcdnServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.websocket_bill_type is not None:
            result['WebsocketBillType'] = self.websocket_bill_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('WebsocketBillType') is not None:
            self.websocket_bill_type = m.get('WebsocketBillType')
        return self


class OpenDcdnServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDcdnServiceResponseBody, self).to_map()
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


class OpenDcdnServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenDcdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenDcdnServiceResponse, self).to_map()
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
            temp_model = OpenDcdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadDcdnObjectCachesRequest(TeaModel):
    def __init__(self, area=None, object_path=None, owner_id=None, security_token=None):
        self.area = area  # type: str
        self.object_path = object_path  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreloadDcdnObjectCachesRequest, self).to_map()
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


class PreloadDcdnObjectCachesResponseBody(TeaModel):
    def __init__(self, preload_task_id=None, request_id=None):
        self.preload_task_id = preload_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreloadDcdnObjectCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preload_task_id is not None:
            result['PreloadTaskId'] = self.preload_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreloadTaskId') is not None:
            self.preload_task_id = m.get('PreloadTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreloadDcdnObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PreloadDcdnObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreloadDcdnObjectCachesResponse, self).to_map()
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
            temp_model = PreloadDcdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDcdnStagingConfigToProductionRequest(TeaModel):
    def __init__(self, domain_name=None, function_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_name = function_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishDcdnStagingConfigToProductionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class PublishDcdnStagingConfigToProductionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishDcdnStagingConfigToProductionResponseBody, self).to_map()
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


class PublishDcdnStagingConfigToProductionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishDcdnStagingConfigToProductionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishDcdnStagingConfigToProductionResponse, self).to_map()
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
            temp_model = PublishDcdnStagingConfigToProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRoutineCodeRevisionRequest(TeaModel):
    def __init__(self, envs=None, name=None, owner_id=None, select_code_revision=None):
        self.envs = envs  # type: dict[str, any]
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class PublishRoutineCodeRevisionShrinkRequest(TeaModel):
    def __init__(self, envs_shrink=None, name=None, owner_id=None, select_code_revision=None):
        self.envs_shrink = envs_shrink  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class PublishRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishRoutineCodeRevisionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishRoutineCodeRevisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionResponse, self).to_map()
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
            temp_model = PublishRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDcdnObjectCachesRequest(TeaModel):
    def __init__(self, object_path=None, object_type=None, owner_id=None, security_token=None):
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDcdnObjectCachesRequest, self).to_map()
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


class RefreshDcdnObjectCachesResponseBody(TeaModel):
    def __init__(self, refresh_task_id=None, request_id=None):
        self.refresh_task_id = refresh_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDcdnObjectCachesResponseBody, self).to_map()
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


class RefreshDcdnObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshDcdnObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshDcdnObjectCachesResponse, self).to_map()
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
            temp_model = RefreshDcdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackDcdnStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackDcdnStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class RollbackDcdnStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackDcdnStagingConfigResponseBody, self).to_map()
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


class RollbackDcdnStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RollbackDcdnStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackDcdnStagingConfigResponse, self).to_map()
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
            temp_model = RollbackDcdnStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnConfigOfVersionRequest(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_id=None, function_name=None, owner_account=None,
                 owner_id=None, security_token=None, version_id=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: str
        self.function_id = function_id  # type: long
        self.function_name = function_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnConfigOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            self.function_args = m.get('FunctionArgs')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetDcdnConfigOfVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnConfigOfVersionResponseBody, self).to_map()
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


class SetDcdnConfigOfVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnConfigOfVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnConfigOfVersionResponse, self).to_map()
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
            temp_model = SetDcdnConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainCSRCertificateRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, server_certificate=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.server_certificate = server_certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCSRCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        return self


class SetDcdnDomainCSRCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCSRCertificateResponseBody, self).to_map()
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


class SetDcdnDomainCSRCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnDomainCSRCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnDomainCSRCertificateResponse, self).to_map()
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
            temp_model = SetDcdnDomainCSRCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainCertificateRequest(TeaModel):
    def __init__(self, cert_name=None, cert_type=None, domain_name=None, force_set=None, owner_id=None, region=None,
                 sslpri=None, sslprotocol=None, sslpub=None, security_token=None):
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.force_set = force_set  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.sslpri = sslpri  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDcdnDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCertificateResponseBody, self).to_map()
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


class SetDcdnDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnDomainCertificateResponse, self).to_map()
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
            temp_model = SetDcdnDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainSMCertificateRequest(TeaModel):
    def __init__(self, cert_identifier=None, domain_name=None, owner_id=None, sslprotocol=None, security_token=None):
        self.cert_identifier = cert_identifier  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.sslprotocol = sslprotocol  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainSMCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDcdnDomainSMCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainSMCertificateResponseBody, self).to_map()
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


class SetDcdnDomainSMCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnDomainSMCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnDomainSMCertificateResponse, self).to_map()
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
            temp_model = SetDcdnDomainSMCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, functions=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.functions = functions  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetDcdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainStagingConfigResponseBody, self).to_map()
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


class SetDcdnDomainStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnDomainStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnDomainStagingConfigResponse, self).to_map()
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
            temp_model = SetDcdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnFullDomainsBlockIPRequest(TeaModel):
    def __init__(self, block_interval=None, iplist=None, operation_type=None, owner_id=None):
        self.block_interval = block_interval  # type: int
        self.iplist = iplist  # type: str
        self.operation_type = operation_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnFullDomainsBlockIPRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_interval is not None:
            result['BlockInterval'] = self.block_interval
        if self.iplist is not None:
            result['IPList'] = self.iplist
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockInterval') is not None:
            self.block_interval = m.get('BlockInterval')
        if m.get('IPList') is not None:
            self.iplist = m.get('IPList')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetDcdnFullDomainsBlockIPResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnFullDomainsBlockIPResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDcdnFullDomainsBlockIPResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnFullDomainsBlockIPResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnFullDomainsBlockIPResponse, self).to_map()
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
            temp_model = SetDcdnFullDomainsBlockIPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnUserConfigRequest(TeaModel):
    def __init__(self, configs=None, function_id=None, owner_account=None, owner_id=None, security_token=None):
        self.configs = configs  # type: str
        self.function_id = function_id  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnUserConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDcdnUserConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnUserConfigResponseBody, self).to_map()
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


class SetDcdnUserConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDcdnUserConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDcdnUserConfigResponse, self).to_map()
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
            temp_model = SetDcdnUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRoutineSubdomainRequest(TeaModel):
    def __init__(self, owner_id=None, subdomains=None):
        self.owner_id = owner_id  # type: long
        self.subdomains = subdomains  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRoutineSubdomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')
        return self


class SetRoutineSubdomainShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, subdomains_shrink=None):
        self.owner_id = owner_id  # type: long
        self.subdomains_shrink = subdomains_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRoutineSubdomainShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subdomains_shrink is not None:
            result['Subdomains'] = self.subdomains_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Subdomains') is not None:
            self.subdomains_shrink = m.get('Subdomains')
        return self


class SetRoutineSubdomainResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRoutineSubdomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRoutineSubdomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetRoutineSubdomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRoutineSubdomainResponse, self).to_map()
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
            temp_model = SetRoutineSubdomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDcdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnDomainRequest, self).to_map()
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


class StartDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnDomainResponseBody, self).to_map()
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


class StartDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDcdnDomainResponse, self).to_map()
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
            temp_model = StartDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDcdnIpaDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnIpaDomainRequest, self).to_map()
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


class StartDcdnIpaDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnIpaDomainResponseBody, self).to_map()
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


class StartDcdnIpaDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartDcdnIpaDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDcdnIpaDomainResponse, self).to_map()
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
            temp_model = StartDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDcdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnDomainRequest, self).to_map()
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


class StopDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnDomainResponseBody, self).to_map()
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


class StopDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDcdnDomainResponse, self).to_map()
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
            temp_model = StopDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDcdnIpaDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnIpaDomainRequest, self).to_map()
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


class StopDcdnIpaDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnIpaDomainResponseBody, self).to_map()
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


class StopDcdnIpaDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopDcdnIpaDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDcdnIpaDomainResponse, self).to_map()
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
            temp_model = StopDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagDcdnResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagDcdnResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagDcdnResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[TagDcdnResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagDcdnResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagDcdnResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagDcdnResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagDcdnResourcesResponseBody, self).to_map()
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


class TagDcdnResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagDcdnResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagDcdnResourcesResponse, self).to_map()
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
            temp_model = TagDcdnResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagDcdnResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_id=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagDcdnResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagDcdnResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagDcdnResourcesResponseBody, self).to_map()
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


class UntagDcdnResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagDcdnResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagDcdnResourcesResponse, self).to_map()
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
            temp_model = UntagDcdnResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnDeliverTaskRequest(TeaModel):
    def __init__(self, deliver=None, deliver_id=None, domain_name=None, name=None, owner_id=None, reports=None,
                 schedule=None):
        self.deliver = deliver  # type: str
        self.deliver_id = deliver_id  # type: long
        self.domain_name = domain_name  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.reports = reports  # type: str
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateDcdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDeliverTaskResponseBody, self).to_map()
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


class UpdateDcdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnDeliverTaskResponse, self).to_map()
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
            temp_model = UpdateDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, resource_group_id=None, security_token=None, sources=None,
                 top_level_domain=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateDcdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDomainResponseBody, self).to_map()
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


class UpdateDcdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnDomainResponse, self).to_map()
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
            temp_model = UpdateDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnIpaDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, resource_group_id=None, security_token=None, sources=None,
                 top_level_domain=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateDcdnIpaDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnIpaDomainResponseBody, self).to_map()
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


class UpdateDcdnIpaDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnIpaDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnIpaDomainResponse, self).to_map()
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
            temp_model = UpdateDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnSLSRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, data_center=None, domain_name=None, owner_id=None, project_name=None, slslog_store=None,
                 slsproject=None, slsregion=None, sampling_rate=None):
        self.data_center = data_center  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.slslog_store = slslog_store  # type: str
        self.slsproject = slsproject  # type: str
        self.slsregion = slsregion  # type: str
        self.sampling_rate = sampling_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnSLSRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center is not None:
            result['DataCenter'] = self.data_center
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        return self


class UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains(TeaModel):
    def __init__(self, desc=None, domain_name=None, region=None, status=None):
        self.desc = desc  # type: str
        self.domain_name = domain_name  # type: str
        self.region = region  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent(TeaModel):
    def __init__(self, domains=None):
        self.domains = domains  # type: list[UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class UpdateDcdnSLSRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(UpdateDcdnSLSRealtimeLogDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDcdnSLSRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnSLSRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnSLSRealtimeLogDeliveryResponse, self).to_map()
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
            temp_model = UpdateDcdnSLSRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnSubTaskRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, report_ids=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.report_ids = report_ids  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnSubTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
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
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class UpdateDcdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnSubTaskResponseBody, self).to_map()
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


class UpdateDcdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnSubTaskResponse, self).to_map()
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
            temp_model = UpdateDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnUserRealTimeDeliveryFieldRequest(TeaModel):
    def __init__(self, business_type=None, fields=None, owner_id=None):
        self.business_type = business_type  # type: str
        self.fields = fields  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnUserRealTimeDeliveryFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpdateDcdnUserRealTimeDeliveryFieldResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnUserRealTimeDeliveryFieldResponseBody, self).to_map()
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


class UpdateDcdnUserRealTimeDeliveryFieldResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDcdnUserRealTimeDeliveryFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDcdnUserRealTimeDeliveryFieldResponse, self).to_map()
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
            temp_model = UpdateDcdnUserRealTimeDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRoutineCodeRequest(TeaModel):
    def __init__(self, code_description=None, name=None, owner_id=None):
        self.code_description = code_description  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UploadRoutineCodeResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRoutineCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadRoutineCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadRoutineCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadRoutineCodeResponse, self).to_map()
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
            temp_model = UploadRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadStagingRoutineCodeRequest(TeaModel):
    def __init__(self, code_description=None, name=None, owner_id=None):
        self.code_description = code_description  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadStagingRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UploadStagingRoutineCodeResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadStagingRoutineCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadStagingRoutineCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadStagingRoutineCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadStagingRoutineCodeResponse, self).to_map()
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
            temp_model = UploadStagingRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDcdnDomainOwnerRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, verify_type=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.verify_type = verify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDcdnDomainOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyDcdnDomainOwnerResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDcdnDomainOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyDcdnDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyDcdnDomainOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyDcdnDomainOwnerResponse, self).to_map()
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
            temp_model = VerifyDcdnDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


