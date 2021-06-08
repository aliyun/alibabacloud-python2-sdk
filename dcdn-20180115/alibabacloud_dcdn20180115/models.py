# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDcdnDomainRequest(TeaModel):
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None,
                 resource_group_id=None, sources=None, check_url=None, scope=None, top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sources = sources  # type: str
        self.check_url = check_url  # type: str
        self.scope = scope  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None,
                 resource_group_id=None, sources=None, check_url=None, scope=None, top_level_domain=None, protocol=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sources = sources  # type: str
        self.check_url = check_url  # type: str
        self.scope = scope  # type: str
        self.top_level_domain = top_level_domain  # type: str
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None,
                 resource_group_id=None, sources=None, check_url=None, scope=None, top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sources = sources  # type: str
        self.check_url = check_url  # type: str
        self.scope = scope  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_names=None,
                 function_names=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, cert_name=None, cert_type=None,
                 sslprotocol=None, sslpub=None, sslpri=None, region=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.sslpri = sslpri  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_names=None, functions=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_names=None, functions=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetDcdnIpaDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
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
    def __init__(self, owner_id=None, security_token=None, domain_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
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
    def __init__(self, owner_id=None, security_token=None, domain_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
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


class CommitStagingRoutineCodeRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, code_description=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.code_description = code_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitStagingRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
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
    def __init__(self, owner_id=None, common_name=None, sans=None, organization=None, organization_unit=None,
                 country=None, state=None, city=None, email=None):
        self.owner_id = owner_id  # type: long
        self.common_name = common_name  # type: str
        self.sans = sans  # type: str
        self.organization = organization  # type: str
        self.organization_unit = organization_unit  # type: str
        self.country = country  # type: str
        self.state = state  # type: str
        self.city = city  # type: str
        self.email = email  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnCertificateSigningRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.sans is not None:
            result['SANs'] = self.sans
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.country is not None:
            result['Country'] = self.country
        if self.state is not None:
            result['State'] = self.state
        if self.city is not None:
            result['City'] = self.city
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('SANs') is not None:
            self.sans = m.get('SANs')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class CreateDcdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(self, request_id=None, pub_md_5=None, csr=None, common_name=None):
        self.request_id = request_id  # type: str
        self.pub_md_5 = pub_md_5  # type: str
        self.csr = csr  # type: str
        self.common_name = common_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnCertificateSigningRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
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
    def __init__(self, owner_id=None, name=None, status=None, reports=None, domain_name=None, deliver=None,
                 schedule=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.status = status  # type: str
        self.reports = reports  # type: str
        self.domain_name = domain_name  # type: str
        self.deliver = deliver  # type: dict[str, any]
        self.schedule = schedule  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateDcdnDeliverTaskShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, status=None, reports=None, domain_name=None, deliver_shrink=None,
                 schedule_shrink=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.status = status  # type: str
        self.reports = reports  # type: str
        self.domain_name = domain_name  # type: str
        self.deliver_shrink = deliver_shrink  # type: str
        self.schedule_shrink = schedule_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDeliverTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver_shrink is not None:
            result['Deliver'] = self.deliver_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver_shrink = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
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


class CreateDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, region_id=None, field_id=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.region_id = region_id  # type: str
        self.field_id = field_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDomainOfflineLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.field_id is not None:
            result['FieldId'] = self.field_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')
        return self


class CreateDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnDomainOfflineLogDeliveryResponseBody, self).to_map()
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


class CreateDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDcdnDomainOfflineLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDcdnDomainOfflineLogDeliveryResponse, self).to_map()
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
            temp_model = CreateDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnSubTaskRequest(TeaModel):
    def __init__(self, owner_id=None, status=None, report_ids=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.status = status  # type: str
        self.report_ids = report_ids  # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDcdnSubTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, owner_id=None, name=None, description=None, env_conf=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.env_conf = env_conf  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        return self


class CreateRoutineShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, env_conf_shrink=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.env_conf_shrink = env_conf_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoutineShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
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


class DeleteDcdnDeliverTaskRequest(TeaModel):
    def __init__(self, owner_id=None, deliver_id=None):
        self.owner_id = owner_id  # type: long
        self.deliver_id = deliver_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, config_id=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.config_id = config_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnIpaSpecificConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
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


class DeleteDcdnSpecificConfigRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, config_id=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.config_id = config_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, config_id=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.config_id = config_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDcdnSpecificStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
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
    def __init__(self, owner_id=None, name=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, owner_id=None, name=None, select_code_revision=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, owner_id=None, name=None, envs=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.envs = envs  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.envs is not None:
            result['Envs'] = self.envs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        return self


class DeleteRoutineConfEnvsShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, envs_shrink=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.envs_shrink = envs_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoutineConfEnvsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
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


class DescribeDcdnBgpBpsDataRequest(TeaModel):
    def __init__(self, owner_id=None, isp=None, start_time=None, end_time=None, interval=None):
        self.owner_id = owner_id  # type: long
        self.isp = isp  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(self, out=None, in_=None, time_stamp=None):
        self.out = out  # type: float
        self.in_ = in_  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out is not None:
            result['Out'] = self.out
        if self.in_ is not None:
            result['In'] = self.in_
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpBpsDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, bgp_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.bgp_data_interval = bgp_data_interval  # type: list[DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval]

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
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
    def __init__(self, owner_id=None, isp=None, start_time=None, end_time=None, interval=None):
        self.owner_id = owner_id  # type: long
        self.isp = isp  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(self, out=None, in_=None, time_stamp=None):
        self.out = out  # type: long
        self.in_ = in_  # type: long
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out is not None:
            result['Out'] = self.out
        if self.in_ is not None:
            result['In'] = self.in_
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpTrafficDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, bgp_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.bgp_data_interval = bgp_data_interval  # type: list[DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval]

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
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
    def __init__(self, owner_id=None, language=None):
        self.owner_id = owner_id  # type: long
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem(TeaModel):
    def __init__(self, countries_and_regions=None, continent=None, countries_and_regions_name=None):
        self.countries_and_regions = countries_and_regions  # type: str
        self.continent = continent  # type: str
        self.countries_and_regions_name = countries_and_regions_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.countries_and_regions is not None:
            result['CountriesAndRegions'] = self.countries_and_regions
        if self.continent is not None:
            result['Continent'] = self.continent
        if self.countries_and_regions_name is not None:
            result['CountriesAndRegionsName'] = self.countries_and_regions_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountriesAndRegions') is not None:
            self.countries_and_regions = m.get('CountriesAndRegions')
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')
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
    def __init__(self, request_id=None, info_list=None):
        self.request_id = request_id  # type: str
        self.info_list = info_list  # type: DescribeDcdnBlockedRegionsResponseBodyInfoList

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnBlockedRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.info_list is not None:
            result['InfoList'] = self.info_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InfoList') is not None:
            temp_model = DescribeDcdnBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m['InfoList'])
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
    def __init__(self, owner_id=None, security_token=None, cert_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.cert_name = cert_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        return self


class DescribeDcdnCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert_name=None, key=None, cert=None, cert_id=None, request_id=None):
        self.cert_name = cert_name  # type: str
        self.key = key  # type: str
        self.cert = cert  # type: str
        self.cert_id = cert_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(self, last_time=None, fingerprint=None, cert_name=None, issuer=None, cert_id=None, common=None):
        self.last_time = last_time  # type: long
        self.fingerprint = fingerprint  # type: str
        self.cert_name = cert_name  # type: str
        self.issuer = issuer  # type: str
        self.cert_id = cert_id  # type: long
        self.common = common  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.common is not None:
            result['Common'] = self.common
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Common') is not None:
            self.common = m.get('Common')
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
    def __init__(self, count=None, cert_list=None):
        self.count = count  # type: int
        self.cert_list = cert_list  # type: DescribeDcdnCertificateListResponseBodyCertificateListModelCertList

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBodyCertificateListModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CertList') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        return self


class DescribeDcdnCertificateListResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_list_model=None):
        self.request_id = request_id  # type: str
        self.certificate_list_model = certificate_list_model  # type: DescribeDcdnCertificateListResponseBodyCertificateListModel

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeDcdnCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
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


class DescribeDcdnConfigOfVersionRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, version_id=None, function_id=None, function_name=None,
                 group_id=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.version_id = version_id  # type: str
        self.function_id = function_id  # type: int
        self.function_name = function_name  # type: str
        self.group_id = group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = status  # type: str
        self.config_id = config_id  # type: str
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
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


class DescribeDcdnDeliverListRequest(TeaModel):
    def __init__(self, owner_id=None, deliver_id=None, status=None):
        self.owner_id = owner_id  # type: long
        self.deliver_id = deliver_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDeliverListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, static_https_bps=None, bps=None, dynamic_https_bps=None,
                 dynamic_http_bps=None, static_http_bps=None):
        self.time_stamp = time_stamp  # type: str
        self.static_https_bps = static_https_bps  # type: float
        self.bps = bps  # type: float
        self.dynamic_https_bps = dynamic_https_bps  # type: float
        self.dynamic_http_bps = dynamic_http_bps  # type: float
        self.static_http_bps = static_http_bps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_bps is not None:
            result['StaticHttpsBps'] = self.static_https_bps
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.dynamic_https_bps is not None:
            result['DynamicHttpsBps'] = self.dynamic_https_bps
        if self.dynamic_http_bps is not None:
            result['DynamicHttpBps'] = self.dynamic_http_bps
        if self.static_http_bps is not None:
            result['StaticHttpBps'] = self.static_http_bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsBps') is not None:
            self.static_https_bps = m.get('StaticHttpsBps')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DynamicHttpsBps') is not None:
            self.dynamic_https_bps = m.get('DynamicHttpsBps')
        if m.get('DynamicHttpBps') is not None:
            self.dynamic_http_bps = m.get('DynamicHttpBps')
        if m.get('StaticHttpBps') is not None:
            self.static_http_bps = m.get('StaticHttpBps')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
    def __init__(self, cert_start_time=None, cert_expire_time=None, cert_ca_is_legacy=None,
                 cert_subject_common_name=None, cert_type=None, domain_names=None, cert_expired=None, issuer=None, domain_list=None):
        self.cert_start_time = cert_start_time  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_ca_is_legacy = cert_ca_is_legacy  # type: str
        self.cert_subject_common_name = cert_subject_common_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_names = domain_names  # type: str
        self.cert_expired = cert_expired  # type: str
        self.issuer = issuer  # type: str
        self.domain_list = domain_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_ca_is_legacy is not None:
            result['CertCaIsLegacy'] = self.cert_ca_is_legacy
        if self.cert_subject_common_name is not None:
            result['CertSubjectCommonName'] = self.cert_subject_common_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.cert_expired is not None:
            result['CertExpired'] = self.cert_expired
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertCaIsLegacy') is not None:
            self.cert_ca_is_legacy = m.get('CertCaIsLegacy')
        if m.get('CertSubjectCommonName') is not None:
            self.cert_subject_common_name = m.get('CertSubjectCommonName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('CertExpired') is not None:
            self.cert_expired = m.get('CertExpired')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
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
    def __init__(self, request_id=None, cert_infos=None):
        self.request_id = request_id  # type: str
        self.cert_infos = cert_infos  # type: DescribeDcdnDomainByCertificateResponseBodyCertInfos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainByCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
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


class DescribeDcdnDomainCertificateInfoRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, status=None, cert_life=None, cert_expire_time=None, sslpub=None, sslprotocol=None,
                 cert_type=None, cert_domain_name=None, cert_name=None, cert_org=None, domain_name=None):
        self.status = status  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.sslpub = sslpub  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, request_id=None, cert_infos=None):
        self.request_id = request_id  # type: str
        self.cert_infos = cert_infos  # type: DescribeDcdnDomainCertificateInfoResponseBodyCertInfos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCertificateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
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
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainCnameResponseBodyCnameDatasData(TeaModel):
    def __init__(self, status=None, domain=None, cname=None):
        self.status = status  # type: int
        self.domain = domain  # type: str
        self.cname = cname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponseBodyCnameDatasData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
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
    def __init__(self, request_id=None, cname_datas=None):
        self.request_id = request_id  # type: str
        self.cname_datas = cname_datas  # type: DescribeDcdnDomainCnameResponseBodyCnameDatas

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainCnameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname_datas is not None:
            result['CnameDatas'] = self.cname_datas.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CnameDatas') is not None:
            temp_model = DescribeDcdnDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m['CnameDatas'])
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
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
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = status  # type: str
        self.config_id = config_id  # type: str
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
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
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: DescribeDcdnDomainConfigsResponseBodyDomainConfigs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, type=None, weight=None, enabled=None, priority=None, port=None, content=None):
        self.type = type  # type: str
        self.weight = weight  # type: str
        self.enabled = enabled  # type: str
        self.priority = priority  # type: str
        self.port = port  # type: int
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, gmt_created=None, sslpub=None, description=None, sslprotocol=None, resource_group_id=None,
                 cert_name=None, scope=None, cname=None, domain_status=None, gmt_modified=None, domain_name=None, sources=None):
        self.gmt_created = gmt_created  # type: str
        self.sslpub = sslpub  # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.cert_name = cert_name  # type: str
        self.scope = scope  # type: str
        self.cname = cname  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: DescribeDcdnDomainDetailResponseBodyDomainDetailSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBodyDomainDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnDomainDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_detail=None):
        self.request_id = request_id  # type: str
        self.domain_detail = domain_detail  # type: DescribeDcdnDomainDetailResponseBodyDomainDetail

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, byte_hit_rate=None, req_hit_rate=None):
        self.time_stamp = time_stamp  # type: str
        self.byte_hit_rate = byte_hit_rate  # type: float
        self.req_hit_rate = req_hit_rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 hit_rate_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.hit_rate_per_interval = hit_rate_per_interval  # type: DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval

    def validate(self):
        if self.hit_rate_per_interval:
            self.hit_rate_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.hit_rate_per_interval is not None:
            result['HitRatePerInterval'] = self.hit_rate_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HitRatePerInterval') is not None:
            temp_model = DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval()
            self.hit_rate_per_interval = temp_model.from_map(m['HitRatePerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
    def __init__(self, code=None, proportion=None, count=None):
        self.code = code  # type: int
        self.proportion = proportion  # type: float
        self.count = count  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
    def __init__(self, time_stamp=None, http_code_data_per_interval=None):
        self.time_stamp = time_stamp  # type: str
        self.http_code_data_per_interval = http_code_data_per_interval  # type: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval

    def validate(self):
        if self.http_code_data_per_interval:
            self.http_code_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.http_code_data_per_interval is not None:
            result['HttpCodeDataPerInterval'] = self.http_code_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval()
            self.http_code_data_per_interval = temp_model.from_map(m['HttpCodeDataPerInterval'])
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.data_per_interval = data_per_interval  # type: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, time_merge=None,
                 interval=None, fix_time_gap=None, isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.time_merge = time_merge  # type: str
        self.interval = interval  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, time_merge=None,
                 interval=None, fix_time_gap=None, isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.time_merge = time_merge  # type: str
        self.interval = interval  # type: str
        self.fix_time_gap = fix_time_gap  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIpaTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainIspDataResponseBodyValueIspProportionData(TeaModel):
    def __init__(self, qps=None, total_query=None, total_bytes=None, avg_response_rate=None, avg_response_time=None,
                 proportion=None, avg_object_size=None, isp_ename=None, bps=None, isp=None, bytes_proportion=None):
        self.qps = qps  # type: str
        self.total_query = total_query  # type: str
        self.total_bytes = total_bytes  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.proportion = proportion  # type: str
        self.avg_object_size = avg_object_size  # type: str
        self.isp_ename = isp_ename  # type: str
        self.bps = bps  # type: str
        self.isp = isp  # type: str
        self.bytes_proportion = bytes_proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponseBodyValueIspProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 value=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.value = value  # type: DescribeDcdnDomainIspDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainIspDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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
    def __init__(self, owner_id=None, domain_name=None, page_size=None, page_number=None, start_time=None,
                 end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(self, end_time=None, log_size=None, start_time=None, log_name=None, log_path=None):
        self.end_time = end_time  # type: str
        self.log_size = log_size  # type: long
        self.start_time = start_time  # type: str
        self.log_name = log_name  # type: str
        self.log_path = log_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
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
    def __init__(self, domain_name=None, request_id=None, domain_log_details=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.domain_log_details = domain_log_details  # type: DescribeDcdnDomainLogResponseBodyDomainLogDetails

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(TeaModel):
    def __init__(self, type=None, time_stamp=None, domain=None, request=None):
        self.type = type  # type: str
        self.time_stamp = time_stamp  # type: str
        self.domain = domain  # type: str
        self.request = request  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Request') is not None:
            self.request = m.get('Request')
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
    def __init__(self, type=None, domain=None, time_stamp=None, area=None, bps=None):
        self.type = type  # type: str
        self.domain = domain  # type: str
        self.time_stamp = time_stamp  # type: str
        self.area = area  # type: str
        self.bps = bps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.area is not None:
            result['Area'] = self.area
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, request_per_interval=None,
                 traffic_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.request_per_interval = request_per_interval  # type: DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_per_interval is not None:
            result['RequestPerInterval'] = self.request_per_interval.to_map()
        if self.traffic_per_interval is not None:
            result['TrafficPerInterval'] = self.traffic_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestPerInterval') is not None:
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m['RequestPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_http_origin_bps=None, static_http_origin_bps=None, time_stamp=None,
                 static_https_origin_bps=None, origin_bps=None, dynamic_https_origin_bps=None):
        self.dynamic_http_origin_bps = dynamic_http_origin_bps  # type: float
        self.static_http_origin_bps = static_http_origin_bps  # type: float
        self.time_stamp = time_stamp  # type: str
        self.static_https_origin_bps = static_https_origin_bps  # type: float
        self.origin_bps = origin_bps  # type: float
        self.dynamic_https_origin_bps = dynamic_https_origin_bps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_origin_bps is not None:
            result['DynamicHttpOriginBps'] = self.dynamic_http_origin_bps
        if self.static_http_origin_bps is not None:
            result['StaticHttpOriginBps'] = self.static_http_origin_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_origin_bps is not None:
            result['StaticHttpsOriginBps'] = self.static_https_origin_bps
        if self.origin_bps is not None:
            result['OriginBps'] = self.origin_bps
        if self.dynamic_https_origin_bps is not None:
            result['DynamicHttpsOriginBps'] = self.dynamic_https_origin_bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpOriginBps') is not None:
            self.dynamic_http_origin_bps = m.get('DynamicHttpOriginBps')
        if m.get('StaticHttpOriginBps') is not None:
            self.static_http_origin_bps = m.get('StaticHttpOriginBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsOriginBps') is not None:
            self.static_https_origin_bps = m.get('StaticHttpsOriginBps')
        if m.get('OriginBps') is not None:
            self.origin_bps = m.get('OriginBps')
        if m.get('DynamicHttpsOriginBps') is not None:
            self.dynamic_https_origin_bps = m.get('DynamicHttpsOriginBps')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 origin_bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.origin_bps_data_per_interval = origin_bps_data_per_interval  # type: DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval

    def validate(self):
        if self.origin_bps_data_per_interval:
            self.origin_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.origin_bps_data_per_interval is not None:
            result['OriginBpsDataPerInterval'] = self.origin_bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('OriginBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval()
            self.origin_bps_data_per_interval = temp_model.from_map(m['OriginBpsDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_http_origin_traffic=None, static_https_origin_traffic=None, origin_traffic=None,
                 static_http_origin_traffic=None, dynamic_https_origin_traffic=None, time_stamp=None):
        self.dynamic_http_origin_traffic = dynamic_http_origin_traffic  # type: float
        self.static_https_origin_traffic = static_https_origin_traffic  # type: float
        self.origin_traffic = origin_traffic  # type: float
        self.static_http_origin_traffic = static_http_origin_traffic  # type: float
        self.dynamic_https_origin_traffic = dynamic_https_origin_traffic  # type: float
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
        if self.static_https_origin_traffic is not None:
            result['StaticHttpsOriginTraffic'] = self.static_https_origin_traffic
        if self.origin_traffic is not None:
            result['OriginTraffic'] = self.origin_traffic
        if self.static_http_origin_traffic is not None:
            result['StaticHttpOriginTraffic'] = self.static_http_origin_traffic
        if self.dynamic_https_origin_traffic is not None:
            result['DynamicHttpsOriginTraffic'] = self.dynamic_https_origin_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpOriginTraffic') is not None:
            self.dynamic_http_origin_traffic = m.get('DynamicHttpOriginTraffic')
        if m.get('StaticHttpsOriginTraffic') is not None:
            self.static_https_origin_traffic = m.get('StaticHttpsOriginTraffic')
        if m.get('OriginTraffic') is not None:
            self.origin_traffic = m.get('OriginTraffic')
        if m.get('StaticHttpOriginTraffic') is not None:
            self.static_http_origin_traffic = m.get('StaticHttpOriginTraffic')
        if m.get('DynamicHttpsOriginTraffic') is not None:
            self.dynamic_https_origin_traffic = m.get('DynamicHttpsOriginTraffic')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 origin_traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.origin_traffic_data_per_interval = origin_traffic_data_per_interval  # type: DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval

    def validate(self):
        if self.origin_traffic_data_per_interval:
            self.origin_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainOriginTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.origin_traffic_data_per_interval is not None:
            result['OriginTrafficDataPerInterval'] = self.origin_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('OriginTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval()
            self.origin_traffic_data_per_interval = temp_model.from_map(m['OriginTrafficDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainPropertyResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_name=None, protocol=None):
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 pv_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.pv_data_interval = pv_data_interval  # type: DescribeDcdnDomainPvDataResponseBodyPvDataInterval

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainPvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeDcdnDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, dynamic_https_acc=None, dynamic_http_acc=None, qps=None, static_https_acc=None,
                 static_http_qps=None, static_http_acc=None, dynamic_https_qps=None, acc=None, static_https_qps=None,
                 dynamic_http_qps=None, time_stamp=None):
        self.dynamic_https_acc = dynamic_https_acc  # type: float
        self.dynamic_http_acc = dynamic_http_acc  # type: float
        self.qps = qps  # type: float
        self.static_https_acc = static_https_acc  # type: float
        self.static_http_qps = static_http_qps  # type: float
        self.static_http_acc = static_http_acc  # type: float
        self.dynamic_https_qps = dynamic_https_qps  # type: float
        self.acc = acc  # type: float
        self.static_https_qps = static_https_qps  # type: float
        self.dynamic_http_qps = dynamic_http_qps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_https_acc is not None:
            result['DynamicHttpsAcc'] = self.dynamic_https_acc
        if self.dynamic_http_acc is not None:
            result['DynamicHttpAcc'] = self.dynamic_http_acc
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.static_https_acc is not None:
            result['StaticHttpsAcc'] = self.static_https_acc
        if self.static_http_qps is not None:
            result['StaticHttpQps'] = self.static_http_qps
        if self.static_http_acc is not None:
            result['StaticHttpAcc'] = self.static_http_acc
        if self.dynamic_https_qps is not None:
            result['DynamicHttpsQps'] = self.dynamic_https_qps
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.static_https_qps is not None:
            result['StaticHttpsQps'] = self.static_https_qps
        if self.dynamic_http_qps is not None:
            result['DynamicHttpQps'] = self.dynamic_http_qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicHttpsAcc') is not None:
            self.dynamic_https_acc = m.get('DynamicHttpsAcc')
        if m.get('DynamicHttpAcc') is not None:
            self.dynamic_http_acc = m.get('DynamicHttpAcc')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StaticHttpsAcc') is not None:
            self.static_https_acc = m.get('StaticHttpsAcc')
        if m.get('StaticHttpQps') is not None:
            self.static_http_qps = m.get('StaticHttpQps')
        if m.get('StaticHttpAcc') is not None:
            self.static_http_acc = m.get('StaticHttpAcc')
        if m.get('DynamicHttpsQps') is not None:
            self.dynamic_https_qps = m.get('DynamicHttpsQps')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('StaticHttpsQps') is not None:
            self.static_https_qps = m.get('StaticHttpsQps')
        if m.get('DynamicHttpQps') is not None:
            self.dynamic_http_qps = m.get('DynamicHttpQps')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 qps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.qps_data_per_interval = qps_data_per_interval  # type: DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval

    def validate(self):
        if self.qps_data_per_interval:
            self.qps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainQpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.qps_data_per_interval is not None:
            result['QpsDataPerInterval'] = self.qps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('QpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval()
            self.qps_data_per_interval = temp_model.from_map(m['QpsDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, isp_name_en=None, location_name_en=None, start_time=None,
                 end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: DescribeDcdnDomainRealTimeBpsDataResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeByteHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, field=None,
                 location_name_en=None, isp_name_en=None, merge=None, merge_loc_isp=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.location_name_en = location_name_en  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.merge = merge  # type: str
        self.merge_loc_isp = merge_loc_isp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeDetailDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.merge is not None:
            result['Merge'] = self.merge
        if self.merge_loc_isp is not None:
            result['MergeLocIsp'] = self.merge_loc_isp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Merge') is not None:
            self.merge = m.get('Merge')
        if m.get('MergeLocIsp') is not None:
            self.merge_loc_isp = m.get('MergeLocIsp')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, isp_name_en=None,
                 location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(self, code=None, proportion=None, count=None):
        self.code = code  # type: str
        self.proportion = proportion  # type: str
        self.count = count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 real_time_http_code_data=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_http_code_data = real_time_http_code_data  # type: DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
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
    def __init__(self, owner_id=None, domain_name=None, isp_name_en=None, location_name_en=None, start_time=None,
                 end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: DescribeDcdnDomainRealTimeQpsDataResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeQpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeReqHitRateDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 real_time_src_bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval  # type: DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_bps_data_per_interval is not None:
            result['RealTimeSrcBpsDataPerInterval'] = self.real_time_src_bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, isp_name_en=None,
                 location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
    def __init__(self, code=None, proportion=None, count=None):
        self.code = code  # type: str
        self.proportion = proportion  # type: str
        self.count = count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 real_time_src_http_code_data=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_src_http_code_data = real_time_src_http_code_data  # type: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_http_code_data is not None:
            result['RealTimeSrcHttpCodeData'] = self.real_time_src_http_code_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 real_time_src_traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval  # type: DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_traffic_data_per_interval is not None:
            result['RealTimeSrcTrafficDataPerInterval'] = self.real_time_src_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 real_time_traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval  # type: DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRealTimeTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(self, qps=None, total_query=None, total_bytes=None, region_ename=None, region=None,
                 avg_response_rate=None, avg_response_time=None, proportion=None, avg_object_size=None, bps=None,
                 bytes_proportion=None):
        self.qps = qps  # type: str
        self.total_query = total_query  # type: str
        self.total_bytes = total_bytes  # type: str
        self.region_ename = region_ename  # type: str
        self.region = region  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.proportion = proportion  # type: str
        self.avg_object_size = avg_object_size  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 value=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.value = value  # type: DescribeDcdnDomainRegionDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainRegionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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
    def __init__(self, owner_id=None, domain_name=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
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
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = status  # type: str
        self.config_id = config_id  # type: str
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: list[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs]

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
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: list[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs]

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, sort_by=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, visit_data=None, refer_detail=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.visit_data = visit_data  # type: str
        self.refer_detail = refer_detail  # type: str
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
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')
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
    def __init__(self, start_time=None, request_id=None, domain_name=None, top_refer_list=None):
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.top_refer_list = top_refer_list  # type: DescribeDcdnDomainTopReferVisitResponseBodyTopReferList

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTopReferVisitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, sort_by=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTopUrlVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(self, flow=None, url_detail=None, flow_proportion=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.url_detail = url_detail  # type: str
        self.flow_proportion = flow_proportion  # type: float
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
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
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
    def __init__(self, flow=None, url_detail=None, flow_proportion=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.url_detail = url_detail  # type: str
        self.flow_proportion = flow_proportion  # type: float
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
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
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
    def __init__(self, flow=None, url_detail=None, flow_proportion=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.url_detail = url_detail  # type: str
        self.flow_proportion = flow_proportion  # type: float
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
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
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
    def __init__(self, flow=None, url_detail=None, flow_proportion=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.url_detail = url_detail  # type: str
        self.flow_proportion = flow_proportion  # type: float
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
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
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
    def __init__(self, flow=None, url_detail=None, flow_proportion=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.url_detail = url_detail  # type: str
        self.flow_proportion = flow_proportion  # type: float
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
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
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
    def __init__(self, start_time=None, request_id=None, domain_name=None, all_url_list=None, url_200list=None,
                 url_300list=None, url_400list=None, url_500list=None):
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.all_url_list = all_url_list  # type: DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, static_http_traffic=None, dynamic_https_traffic=None, traffic=None,
                 dynamic_http_traffic=None, time_stamp=None, static_https_traffic=None):
        self.static_http_traffic = static_http_traffic  # type: float
        self.dynamic_https_traffic = dynamic_https_traffic  # type: float
        self.traffic = traffic  # type: float
        self.dynamic_http_traffic = dynamic_http_traffic  # type: float
        self.time_stamp = time_stamp  # type: str
        self.static_https_traffic = static_https_traffic  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_http_traffic is not None:
            result['StaticHttpTraffic'] = self.static_http_traffic
        if self.dynamic_https_traffic is not None:
            result['DynamicHttpsTraffic'] = self.dynamic_https_traffic
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.dynamic_http_traffic is not None:
            result['DynamicHttpTraffic'] = self.dynamic_http_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_traffic is not None:
            result['StaticHttpsTraffic'] = self.static_https_traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StaticHttpTraffic') is not None:
            self.static_http_traffic = m.get('StaticHttpTraffic')
        if m.get('DynamicHttpsTraffic') is not None:
            self.dynamic_https_traffic = m.get('DynamicHttpsTraffic')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('DynamicHttpTraffic') is not None:
            self.dynamic_http_traffic = m.get('DynamicHttpTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsTraffic') is not None:
            self.static_https_traffic = m.get('StaticHttpsTraffic')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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


class DescribeDcdnDomainUvDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 uv_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.uv_data_interval = uv_data_interval  # type: DescribeDcdnDomainUvDataResponseBodyUvDataInterval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
    def __init__(self, code=None, proportion=None, count=None):
        self.code = code  # type: int
        self.proportion = proportion  # type: float
        self.count = count  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval(TeaModel):
    def __init__(self, http_code_data_module=None):
        self.http_code_data_module = http_code_data_module  # type: list[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule]

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, websocket_http_code_data_per_interval=None):
        self.time_stamp = time_stamp  # type: str
        self.websocket_http_code_data_per_interval = websocket_http_code_data_per_interval  # type: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval

    def validate(self):
        if self.websocket_http_code_data_per_interval:
            self.websocket_http_code_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_http_code_data_per_interval is not None:
            result['WebsocketHttpCodeDataPerInterval'] = self.websocket_http_code_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketHttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval()
            self.websocket_http_code_data_per_interval = temp_model.from_map(m['WebsocketHttpCodeDataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval, self).to_map()
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
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.data_per_interval = data_per_interval  # type: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketHttpCodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
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
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, websocket_traffic=None, time_stamp=None):
        self.websocket_traffic = websocket_traffic  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.websocket_traffic is not None:
            result['WebsocketTraffic'] = self.websocket_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WebsocketTraffic') is not None:
            self.websocket_traffic = m.get('WebsocketTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDcdnDomainWebsocketTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
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


class DescribeDcdnHttpsDomainListRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None, keyword=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_start_time=None, cert_expire_time=None, cert_update_time=None, cert_type=None,
                 cert_name=None, cert_status=None, domain_name=None, cert_common_name=None):
        self.cert_start_time = cert_start_time  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_update_time = cert_update_time  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_status = cert_status  # type: str
        self.domain_name = domain_name  # type: str
        self.cert_common_name = cert_common_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
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
    def __init__(self, total_count=None, request_id=None, cert_infos=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.cert_infos = cert_infos  # type: DescribeDcdnHttpsDomainListResponseBodyCertInfos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDcdnHttpsDomainListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
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


class DescribeDcdnIpaDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
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
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = status  # type: str
        self.config_id = config_id  # type: str
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
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
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, type=None, weight=None, enabled=None, priority=None, port=None, content=None):
        self.type = type  # type: str
        self.weight = weight  # type: str
        self.enabled = enabled  # type: str
        self.priority = priority  # type: str
        self.port = port  # type: int
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, gmt_created=None, sslpub=None, description=None, sslprotocol=None, resource_group_id=None,
                 cert_name=None, scope=None, cname=None, domain_status=None, gmt_modified=None, domain_name=None, sources=None):
        self.gmt_created = gmt_created  # type: str
        self.sslpub = sslpub  # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.cert_name = cert_name  # type: str
        self.scope = scope  # type: str
        self.cname = cname  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBodyDomainDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnIpaDomainDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_detail=None):
        self.request_id = request_id  # type: str
        self.domain_detail = domain_detail  # type: DescribeDcdnIpaDomainDetailResponseBodyDomainDetail

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
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
    def __init__(self, changing_affect_time=None, request_id=None, changing_charge_type=None, opening_time=None,
                 internet_charge_type=None, instance_id=None, operation_locks=None):
        self.changing_affect_time = changing_affect_time  # type: str
        self.request_id = request_id  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.opening_time = opening_time  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.operation_locks = operation_locks  # type: DescribeDcdnIpaServiceResponseBodyOperationLocks

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeDcdnIpaServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
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


class DescribeDcdnIpaUserDomainsRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, page_size=None, page_number=None, domain_name=None,
                 domain_status=None, domain_search_type=None, check_domain_show=None, resource_group_id=None, func_id=None,
                 func_filter=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.check_domain_show = check_domain_show  # type: bool
        self.resource_group_id = resource_group_id  # type: str
        self.func_id = func_id  # type: str
        self.func_filter = func_filter  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, type=None, weight=None, priority=None, port=None, content=None):
        self.type = type  # type: str
        self.weight = weight  # type: str
        self.priority = priority  # type: str
        self.port = port  # type: int
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, gmt_created=None, description=None, sslprotocol=None, resource_group_id=None, sandbox=None,
                 domain_status=None, cname=None, gmt_modified=None, domain_name=None, sources=None):
        self.gmt_created = gmt_created  # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
        self.domain_status = domain_status  # type: str
        self.cname = cname  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, domains=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.domains = domains  # type: DescribeDcdnIpaUserDomainsResponseBodyDomains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnIpaUserDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
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


class DescribeDcdnIpInfoRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, ip=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeDcdnIpInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, region_ename=None, region=None, isp_ename=None, dcdn_ip=None, isp=None):
        self.request_id = request_id  # type: str
        self.region_ename = region_ename  # type: str
        self.region = region  # type: str
        self.isp_ename = isp_ename  # type: str
        self.dcdn_ip = dcdn_ip  # type: str
        self.isp = isp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnIpInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.dcdn_ip is not None:
            result['DcdnIp'] = self.dcdn_ip
        if self.isp is not None:
            result['ISP'] = self.isp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('DcdnIp') is not None:
            self.dcdn_ip = m.get('DcdnIp')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
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


class DescribeDcdnOfflineLogDeliveryRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRequest, self).to_map()
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


class DescribeDcdnOfflineLogDeliveryResponseBodyDomains(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryResponseBodyDomains, self).to_map()
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


class DescribeDcdnOfflineLogDeliveryResponseBodyRegions(TeaModel):
    def __init__(self, oss_id=None, oss_path_prefix=None, region_id=None, area_name=None, dla_table_name=None,
                 dla_vc_name=None, dla_db_name=None, region_name=None, area_id=None, is_overseas=None, oss_bucket_name=None,
                 oss_endpoint=None):
        self.oss_id = oss_id  # type: int
        self.oss_path_prefix = oss_path_prefix  # type: str
        self.region_id = region_id  # type: str
        self.area_name = area_name  # type: str
        self.dla_table_name = dla_table_name  # type: str
        self.dla_vc_name = dla_vc_name  # type: str
        self.dla_db_name = dla_db_name  # type: str
        self.region_name = region_name  # type: str
        self.area_id = area_id  # type: str
        self.is_overseas = is_overseas  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_endpoint = oss_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_id is not None:
            result['OssId'] = self.oss_id
        if self.oss_path_prefix is not None:
            result['OssPathPrefix'] = self.oss_path_prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.dla_table_name is not None:
            result['DlaTableName'] = self.dla_table_name
        if self.dla_vc_name is not None:
            result['DlaVcName'] = self.dla_vc_name
        if self.dla_db_name is not None:
            result['DlaDbName'] = self.dla_db_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssId') is not None:
            self.oss_id = m.get('OssId')
        if m.get('OssPathPrefix') is not None:
            self.oss_path_prefix = m.get('OssPathPrefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('DlaTableName') is not None:
            self.dla_table_name = m.get('DlaTableName')
        if m.get('DlaVcName') is not None:
            self.dla_vc_name = m.get('DlaVcName')
        if m.get('DlaDbName') is not None:
            self.dla_db_name = m.get('DlaDbName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        return self


class DescribeDcdnOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None, fields=None, domains=None, regions=None):
        self.request_id = request_id  # type: str
        self.fields = fields  # type: list[str]
        self.domains = domains  # type: list[DescribeDcdnOfflineLogDeliveryResponseBodyDomains]
        self.regions = regions  # type: list[DescribeDcdnOfflineLogDeliveryResponseBodyRegions]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fields is not None:
            result['Fields'] = self.fields
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDcdnOfflineLogDeliveryResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeDcdnOfflineLogDeliveryResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnOfflineLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryResponse, self).to_map()
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
            temp_model = DescribeDcdnOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryFieldRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryFieldRequest, self).to_map()
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


class DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields(TeaModel):
    def __init__(self, description=None, field_id=None, field_name=None):
        self.description = description  # type: str
        self.field_id = field_id  # type: str
        self.field_name = field_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.field_id is not None:
            result['FieldId'] = self.field_id
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        return self


class DescribeDcdnOfflineLogDeliveryFieldResponseBody(TeaModel):
    def __init__(self, request_id=None, fields=None):
        self.request_id = request_id  # type: str
        self.fields = fields  # type: list[DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields]

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryFieldResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnOfflineLogDeliveryFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryFieldResponse, self).to_map()
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
            temp_model = DescribeDcdnOfflineLogDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryRegionsRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRegionsRequest, self).to_map()
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


class DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos(TeaModel):
    def __init__(self, is_overseas=None, region_name=None, oss_endpoint=None, region_id=None):
        self.is_overseas = is_overseas  # type: str
        self.region_name = region_name  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas(TeaModel):
    def __init__(self, area_name=None, area_id=None, region_infos=None):
        self.area_name = area_name  # type: str
        self.area_id = area_id  # type: str
        self.region_infos = region_infos  # type: list[DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos]

    def validate(self):
        if self.region_infos:
            for k in self.region_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        result['RegionInfos'] = []
        if self.region_infos is not None:
            for k in self.region_infos:
                result['RegionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        self.region_infos = []
        if m.get('RegionInfos') is not None:
            for k in m.get('RegionInfos'):
                temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos()
                self.region_infos.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, areas=None):
        self.request_id = request_id  # type: str
        self.areas = areas  # type: list[DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas]

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnOfflineLogDeliveryRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryRegionsResponse, self).to_map()
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
            temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryStatusRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryStatusRequest, self).to_map()
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


class DescribeDcdnOfflineLogDeliveryStatusResponseBody(TeaModel):
    def __init__(self, open_status=None, request_id=None):
        self.open_status = open_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnOfflineLogDeliveryStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDcdnOfflineLogDeliveryStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDcdnOfflineLogDeliveryStatusResponse, self).to_map()
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
            temp_model = DescribeDcdnOfflineLogDeliveryStatusResponseBody()
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
    def __init__(self, block_quota=None, preload_remain=None, request_id=None, block_remain=None, dir_remain=None,
                 url_remain=None, dir_quota=None, url_quota=None, preload_quota=None):
        self.block_quota = block_quota  # type: str
        self.preload_remain = preload_remain  # type: str
        self.request_id = request_id  # type: str
        self.block_remain = block_remain  # type: str
        self.dir_remain = dir_remain  # type: str
        self.url_remain = url_remain  # type: str
        self.dir_quota = dir_quota  # type: str
        self.url_quota = url_quota  # type: str
        self.preload_quota = preload_quota  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
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
    def __init__(self, status=None, creation_time=None, object_type=None, process=None, description=None,
                 object_path=None, task_id=None):
        self.status = status  # type: str
        self.creation_time = creation_time  # type: str
        self.object_type = object_type  # type: str
        self.process = process  # type: str
        self.description = description  # type: str
        self.object_path = object_path  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTaskByIdResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTaskByIdResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, tasks=None):
        self.total_count = total_count  # type: long
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[DescribeDcdnRefreshTaskByIdResponseBodyTasks]

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeDcdnRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
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
    def __init__(self, owner_id=None, security_token=None, task_id=None, object_path=None, page_number=None,
                 object_type=None, domain_name=None, status=None, page_size=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.task_id = task_id  # type: str
        self.object_path = object_path  # type: str
        self.page_number = page_number  # type: int
        self.object_type = object_type  # type: str
        self.domain_name = domain_name  # type: str
        self.status = status  # type: str
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnRefreshTasksResponseBodyTasksTask(TeaModel):
    def __init__(self, status=None, creation_time=None, object_type=None, process=None, description=None,
                 object_path=None, task_id=None):
        self.status = status  # type: str
        self.creation_time = creation_time  # type: str
        self.object_type = object_type  # type: str
        self.process = process  # type: str
        self.description = description  # type: str
        self.object_path = object_path  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponseBodyTasksTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
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
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, tasks=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.tasks = tasks  # type: DescribeDcdnRefreshTasksResponseBodyTasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeDcdnRefreshTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tasks') is not None:
            temp_model = DescribeDcdnRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
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


class DescribeDcdnRegionAndIspResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None, isps=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: DescribeDcdnRegionAndIspResponseBodyRegions
        self.isps = isps  # type: DescribeDcdnRegionAndIspResponseBodyIsps

    def validate(self):
        if self.regions:
            self.regions.validate()
        if self.isps:
            self.isps.validate()

    def to_map(self):
        _map = super(DescribeDcdnRegionAndIspResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.isps is not None:
            result['Isps'] = self.isps.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('Isps') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
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
    def __init__(self, owner_id=None, domain_name=None, report_id=None, area=None, is_overseas=None, http_code=None,
                 start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.report_id = report_id  # type: long
        self.area = area  # type: str
        self.is_overseas = is_overseas  # type: str
        self.http_code = http_code  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.area is not None:
            result['Area'] = self.area
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, owner_id=None, report_id=None, status=None, permission=None):
        self.owner_id = owner_id  # type: long
        self.report_id = report_id  # type: long
        self.status = status  # type: str
        self.permission = permission  # type: str

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
        if self.status is not None:
            result['Status'] = self.status
        if self.permission is not None:
            result['Permission'] = self.permission
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
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


class DescribeDcdnSecFuncInfoRequest(TeaModel):
    def __init__(self, owner_id=None, sec_func_type=None, lang=None):
        self.owner_id = owner_id  # type: long
        self.sec_func_type = sec_func_type  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSecFuncInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func_type is not None:
            result['SecFuncType'] = self.sec_func_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFuncType') is not None:
            self.sec_func_type = m.get('SecFuncType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
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
    def __init__(self, request_id=None, description=None, ret_code=None, http_status=None, content=None):
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.ret_code = ret_code  # type: str
        self.http_status = http_status  # type: str
        self.content = content  # type: list[DescribeDcdnSecFuncInfoResponseBodyContent]

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeDcdnSecFuncInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k))
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
    def __init__(self, websocket_changing_time=None, websocket_changing_type=None, changing_affect_time=None,
                 changing_charge_type=None, request_id=None, opening_time=None, internet_charge_type=None, websocket_type=None,
                 instance_id=None, operation_locks=None):
        self.websocket_changing_time = websocket_changing_time  # type: str
        self.websocket_changing_type = websocket_changing_type  # type: str
        self.changing_affect_time = changing_affect_time  # type: str
        self.changing_charge_type = changing_charge_type  # type: str
        self.request_id = request_id  # type: str
        self.opening_time = opening_time  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.websocket_type = websocket_type  # type: str
        self.instance_id = instance_id  # type: str
        self.operation_locks = operation_locks  # type: DescribeDcdnServiceResponseBodyOperationLocks

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super(DescribeDcdnServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.websocket_changing_time is not None:
            result['WebsocketChangingTime'] = self.websocket_changing_time
        if self.websocket_changing_type is not None:
            result['WebsocketChangingType'] = self.websocket_changing_type
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.websocket_type is not None:
            result['WebsocketType'] = self.websocket_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WebsocketChangingTime') is not None:
            self.websocket_changing_time = m.get('WebsocketChangingTime')
        if m.get('WebsocketChangingType') is not None:
            self.websocket_changing_type = m.get('WebsocketChangingType')
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('WebsocketType') is not None:
            self.websocket_type = m.get('WebsocketType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeDcdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
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
    def __init__(self, request_id=None, ipv4s=None):
        self.request_id = request_id  # type: str
        self.ipv4s = ipv4s  # type: DescribeDcdnStagingIpResponseBodyIPV4s

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        _map = super(DescribeDcdnStagingIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ipv4s is not None:
            result['IPV4s'] = self.ipv4s.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IPV4s') is not None:
            temp_model = DescribeDcdnStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
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
    def __init__(self, owner_id=None, status=None):
        self.owner_id = owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnSubListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, owner_id=None, resource_type=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, owner_id=None, start_time=None, end_time=None, limit=None):
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(self, max_bps=None, rank=None, total_access=None, traffic_percent=None, domain_name=None,
                 total_traffic=None, max_bps_time=None):
        self.max_bps = max_bps  # type: long
        self.rank = rank  # type: long
        self.total_access = total_access  # type: long
        self.traffic_percent = traffic_percent  # type: str
        self.domain_name = domain_name  # type: str
        self.total_traffic = total_traffic  # type: str
        self.max_bps_time = max_bps_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
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
    def __init__(self, domain_online_count=None, end_time=None, start_time=None, request_id=None, domain_count=None,
                 top_domains=None):
        self.domain_online_count = domain_online_count  # type: long
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_count = domain_count  # type: long
        self.top_domains = top_domains  # type: DescribeDcdnTopDomainsByFlowResponseBodyTopDomains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnTopDomainsByFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
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
    def __init__(self, owner_id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(self, flow=None, bandwidth=None, count=None, cdn_region=None, charge_type=None):
        self.flow = flow  # type: float
        self.bandwidth = bandwidth  # type: float
        self.count = count  # type: float
        self.cdn_region = cdn_region  # type: str
        self.charge_type = charge_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.count is not None:
            result['Count'] = self.count
        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
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
    def __init__(self, dimension=None, bill_type=None, bill_time=None, billing_data=None):
        self.dimension = dimension  # type: str
        self.bill_type = bill_type  # type: str
        self.bill_time = bill_time  # type: str
        self.billing_data = billing_data  # type: DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time
        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')
        if m.get('BillingData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
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
    def __init__(self, request_id=None, bill_history_data=None):
        self.request_id = request_id  # type: str
        self.bill_history_data = bill_history_data  # type: DescribeDcdnUserBillHistoryResponseBodyBillHistoryData

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bill_history_data is not None:
            result['BillHistoryData'] = self.bill_history_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BillHistoryData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
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
    def __init__(self, owner_id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
    def __init__(self, end_time=None, start_time=None, billing_cycle=None, product=None, bill_type=None,
                 dimension=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.product = product  # type: str
        self.bill_type = bill_type  # type: str
        self.dimension = dimension  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product is not None:
            result['Product'] = self.product
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
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
    def __init__(self, request_id=None, bill_type_data=None):
        self.request_id = request_id  # type: str
        self.bill_type_data = bill_type_data  # type: DescribeDcdnUserBillTypeResponseBodyBillTypeData

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserBillTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bill_type_data is not None:
            result['BillTypeData'] = self.bill_type_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BillTypeData') is not None:
            temp_model = DescribeDcdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
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
    def __init__(self, owner_id=None, security_token=None, page_size=None, page_number=None, domain_name=None,
                 domain_status=None, domain_search_type=None, check_domain_show=None, resource_group_id=None,
                 change_start_time=None, change_end_time=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.check_domain_show = check_domain_show  # type: bool
        self.resource_group_id = resource_group_id  # type: str
        self.change_start_time = change_start_time  # type: str
        self.change_end_time = change_end_time  # type: str
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, type=None, weight=None, priority=None, port=None, content=None):
        self.type = type  # type: str
        self.weight = weight  # type: str
        self.priority = priority  # type: str
        self.port = port  # type: int
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, gmt_created=None, description=None, sslprotocol=None, resource_group_id=None, sandbox=None,
                 domain_status=None, cname=None, gmt_modified=None, domain_name=None, sources=None):
        self.gmt_created = gmt_created  # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
        self.domain_status = domain_status  # type: str
        self.cname = cname  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, domains=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.domains = domains  # type: DescribeDcdnUserDomainsResponseBodyDomains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
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
    def __init__(self, owner_id=None, func_id=None, page_number=None, page_size=None, resource_group_id=None):
        self.owner_id = owner_id  # type: long
        self.func_id = func_id  # type: int
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, type=None, weight=None, priority=None, port=None, content=None):
        self.type = type  # type: str
        self.weight = weight  # type: str
        self.priority = priority  # type: str
        self.port = port  # type: int
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, gmt_created=None, ssl_protocol=None, description=None, resource_group_id=None, sandbox=None,
                 domain_status=None, cname=None, gmt_modified=None, cdn_type=None, domain_name=None, sources=None):
        self.gmt_created = gmt_created  # type: str
        self.ssl_protocol = ssl_protocol  # type: str
        self.description = description  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
        self.domain_status = domain_status  # type: str
        self.cname = cname  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.cdn_type = cdn_type  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
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
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, domains=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.domains = domains  # type: DescribeDcdnUserDomainsByFuncResponseBodyDomains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeDcdnUserDomainsByFuncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
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
    def __init__(self, block_quota=None, refresh_url_remain=None, domain_quota=None, block_remain=None,
                 preload_remain=None, request_id=None, refresh_url_quota=None, preload_quota=None, refresh_dir_quota=None,
                 refresh_dir_remain=None):
        self.block_quota = block_quota  # type: int
        self.refresh_url_remain = refresh_url_remain  # type: int
        self.domain_quota = domain_quota  # type: int
        self.block_remain = block_remain  # type: int
        self.preload_remain = preload_remain  # type: int
        self.request_id = request_id  # type: str
        self.refresh_url_quota = refresh_url_quota  # type: int
        self.preload_quota = preload_quota  # type: int
        self.refresh_dir_quota = refresh_dir_quota  # type: int
        self.refresh_dir_remain = refresh_dir_remain  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain
        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota
        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')
        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')
        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')
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


class DescribeDcdnUserResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(self, end_time=None, status=None, display_name=None, start_time=None, commodity_code=None,
                 curr_capacity=None, init_capacity=None, instance_id=None, template_name=None):
        self.end_time = end_time  # type: str
        self.status = status  # type: str
        self.display_name = display_name  # type: str
        self.start_time = start_time  # type: str
        self.commodity_code = commodity_code  # type: str
        self.curr_capacity = curr_capacity  # type: str
        self.init_capacity = init_capacity  # type: str
        self.instance_id = instance_id  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
    def __init__(self, owner_id=None, data=None, sec_func=None, metric=None):
        self.owner_id = owner_id  # type: long
        self.data = data  # type: str
        self.sec_func = sec_func  # type: str
        self.metric = metric  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.data is not None:
            result['Data'] = self.data
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.metric is not None:
            result['Metric'] = self.metric
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        return self


class DescribeDcdnUserSecDropResponseBody(TeaModel):
    def __init__(self, msg=None, request_id=None, drops=None, uuid_str=None):
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.drops = drops  # type: int
        self.uuid_str = uuid_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.uuid_str is not None:
            result['UuidStr'] = self.uuid_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
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
    def __init__(self, owner_id=None, sec_func=None, rule_name=None, object=None, domain_name=None, start_time=None,
                 end_time=None, page_size=None, page_number=None, lang=None):
        self.owner_id = owner_id  # type: long
        self.sec_func = sec_func  # type: str
        self.rule_name = rule_name  # type: str
        self.object = object  # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.object is not None:
            result['Object'] = self.object
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBodyRows(TeaModel):
    def __init__(self, domain=None, tm_str=None, drops=None, object=None, sec_func=None, rule_name=None):
        self.domain = domain  # type: str
        self.tm_str = tm_str  # type: str
        self.drops = drops  # type: int
        self.object = object  # type: str
        self.sec_func = sec_func  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnUserSecDropByMinuteResponseBodyRows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.tm_str is not None:
            result['TmStr'] = self.tm_str
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.object is not None:
            result['Object'] = self.object
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TmStr') is not None:
            self.tm_str = m.get('TmStr')
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBody(TeaModel):
    def __init__(self, request_id=None, description=None, len=None, page_number=None, page_size=None,
                 total_count=None, rows=None):
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.len = len  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.rows = rows  # type: list[DescribeDcdnUserSecDropByMinuteResponseBodyRows]

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.len is not None:
            result['Len'] = self.len
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Len') is not None:
            self.len = m.get('Len')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = DescribeDcdnUserSecDropByMinuteResponseBodyRows()
                self.rows.append(temp_model.from_map(k))
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
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnVerifyContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, region_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDcdnWafDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(self, acl_status=None, status=None, domain=None, cc_status=None, waf_status=None):
        self.acl_status = acl_status  # type: int
        self.status = status  # type: int
        self.domain = domain  # type: str
        self.cc_status = cc_status  # type: int
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
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeDcdnWafDomainResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, out_put_domains=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.out_put_domains = out_put_domains  # type: list[DescribeDcdnWafDomainResponseBodyOutPutDomains]

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OutPutDomains'] = []
        if self.out_put_domains is not None:
            for k in self.out_put_domains:
                result['OutPutDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.out_put_domains = []
        if m.get('OutPutDomains') is not None:
            for k in m.get('OutPutDomains'):
                temp_model = DescribeDcdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
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


class DescribeRoutineRequest(TeaModel):
    def __init__(self, owner_id=None, name=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, owner_id=None, name=None, select_code_revision=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.select_code_revision = select_code_revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, in_debt=None, on_service=None, request_id=None, in_debt_overdue=None, enabled=None):
        self.in_debt = in_debt  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnIpaStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
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
    def __init__(self, in_debt=None, on_service=None, request_id=None, in_debt_overdue=None, enabled=None):
        self.in_debt = in_debt  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDcdnStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
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
    def __init__(self, in_debt=None, on_service=None, request_id=None, in_debt_overdue=None, enabled=None):
        self.in_debt = in_debt  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserErStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
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
    def __init__(self, in_debt=None, on_service=None, request_id=None, in_debt_overdue=None, enabled=None):
        self.in_debt = in_debt  # type: bool
        self.on_service = on_service  # type: bool
        self.request_id = request_id  # type: str
        self.in_debt_overdue = in_debt_overdue  # type: bool
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserLogserviceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
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


class DisableDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDcdnDomainOfflineLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DisableDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDcdnDomainOfflineLogDeliveryResponseBody, self).to_map()
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


class DisableDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableDcdnDomainOfflineLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableDcdnDomainOfflineLogDeliveryResponse, self).to_map()
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
            temp_model = DisableDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDcdnOfflineLogDeliveryRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDcdnOfflineLogDeliveryRequest, self).to_map()
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


class DisableDcdnOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDcdnOfflineLogDeliveryResponseBody, self).to_map()
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


class DisableDcdnOfflineLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableDcdnOfflineLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableDcdnOfflineLogDeliveryResponse, self).to_map()
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
            temp_model = DisableDcdnOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditRoutineConfRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, env_conf=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.env_conf = env_conf  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditRoutineConfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        return self


class EditRoutineConfShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, env_conf_shrink=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.env_conf_shrink = env_conf_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditRoutineConfShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
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


class EnableDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableDcdnDomainOfflineLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class EnableDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableDcdnDomainOfflineLogDeliveryResponseBody, self).to_map()
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


class EnableDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableDcdnDomainOfflineLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableDcdnDomainOfflineLogDeliveryResponse, self).to_map()
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
            temp_model = EnableDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDCdnDomainSchdmByPropertyRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, property=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.property = property  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDCdnDomainSchdmByPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.property is not None:
            result['Property'] = self.property
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, security_token=None, bill_type=None, websocket_bill_type=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.bill_type = bill_type  # type: str
        self.websocket_bill_type = websocket_bill_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDcdnServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.websocket_bill_type is not None:
            result['WebsocketBillType'] = self.websocket_bill_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
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
    def __init__(self, owner_id=None, security_token=None, object_path=None, area=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.object_path = object_path  # type: str
        self.area = area  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreloadDcdnObjectCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.area is not None:
            result['Area'] = self.area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('Area') is not None:
            self.area = m.get('Area')
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
    def __init__(self, owner_id=None, domain_name=None, function_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.function_name = function_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishDcdnStagingConfigToProductionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
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
    def __init__(self, owner_id=None, name=None, select_code_revision=None, envs=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.select_code_revision = select_code_revision  # type: str
        self.envs = envs  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        if self.envs is not None:
            result['Envs'] = self.envs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        return self


class PublishRoutineCodeRevisionShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, select_code_revision=None, envs_shrink=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.select_code_revision = select_code_revision  # type: str
        self.envs_shrink = envs_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRoutineCodeRevisionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
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
    def __init__(self, owner_id=None, security_token=None, object_path=None, object_type=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDcdnObjectCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
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
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackDcdnStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, owner_account=None, security_token=None, version_id=None, config_id=None,
                 function_id=None, function_name=None, function_args=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.security_token = security_token  # type: str
        self.version_id = version_id  # type: str
        self.config_id = config_id  # type: str
        self.function_id = function_id  # type: long
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnConfigOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            self.function_args = m.get('FunctionArgs')
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


class SetDcdnDomainCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, cert_name=None, cert_type=None,
                 sslprotocol=None, sslpub=None, sslpri=None, region=None, force_set=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.sslpri = sslpri  # type: str
        self.region = region  # type: str
        self.force_set = force_set  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
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


class SetDcdnDomainCSRCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, server_certificate=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.server_certificate = server_certificate  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainCSRCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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


class SetDcdnDomainStagingConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, functions=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.functions = functions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDcdnDomainStagingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
    def __init__(self, owner_id=None, resource_type=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, owner_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagDcdnResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, owner_id=None, deliver_id=None, name=None, status=None, reports=None, domain_name=None,
                 deliver=None, schedule=None):
        self.owner_id = owner_id  # type: long
        self.deliver_id = deliver_id  # type: long
        self.name = name  # type: str
        self.status = status  # type: str
        self.reports = reports  # type: str
        self.domain_name = domain_name  # type: str
        self.deliver = deliver  # type: dict[str, any]
        self.schedule = schedule  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDeliverTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateDcdnDeliverTaskShrinkRequest(TeaModel):
    def __init__(self, owner_id=None, deliver_id=None, name=None, status=None, reports=None, domain_name=None,
                 deliver_shrink=None, schedule_shrink=None):
        self.owner_id = owner_id  # type: long
        self.deliver_id = deliver_id  # type: long
        self.name = name  # type: str
        self.status = status  # type: str
        self.reports = reports  # type: str
        self.domain_name = domain_name  # type: str
        self.deliver_shrink = deliver_shrink  # type: str
        self.schedule_shrink = schedule_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDeliverTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver_shrink is not None:
            result['Deliver'] = self.deliver_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver_shrink = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, sources=None, resource_group_id=None,
                 top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
    def __init__(self, owner_id=None, security_token=None, domain_name=None, sources=None, resource_group_id=None,
                 top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.sources = sources  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnIpaDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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


class UpdateDcdnSubTaskRequest(TeaModel):
    def __init__(self, owner_id=None, status=None, report_ids=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.status = status  # type: str
        self.report_ids = report_ids  # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDcdnSubTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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


class UploadRoutineCodeRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, code_description=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.code_description = code_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
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
    def __init__(self, owner_id=None, name=None, code_description=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.code_description = code_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadStagingRoutineCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
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
    def __init__(self, owner_id=None, domain_name=None, verify_type=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.verify_type = verify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDcdnDomainOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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


